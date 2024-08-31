from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse
from django.db.models.functions import Lower
from django.contrib.auth.models import User
from datetime import datetime
class Genre(models.Model):
    name = models.CharField(max_length=225,unique=True)
    def __str__(self):
         return self.name
    class Meta:
         constraints = [
            UniqueConstraint(
                Lower('name'),
                name='first_name_unique',
            ),
        ] 
    def get_absolute_url(self):
        return reverse("genre_detail", args=[str(self.name)])
class Author(models.Model):
     fullname = models.CharField(max_length=127)
     birth_date = models.DateField(null=True, blank=True)
     image = models.URLField(null=True,blank=True)
     class Meta:
         constraints = [
            UniqueConstraint(
                Lower('fullname'),
                name='fullname_unique',
            ),
        ]
     def __str__(self):
         return self.fullname
     def get_absolute_url(self):
         return reverse("author_detail", args=[self.fullname])
      
          
class Book(models.Model):
     title = models.CharField(max_length=225)
     author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True,related_name='books')
     pages = models.PositiveIntegerField()
     genre = models.ManyToManyField(Genre,related_name='genres')
     published_at = models.DateTimeField(auto_now_add=True)
     image = models.URLField(blank=True,null=True)
     description = models.TextField()

     def __str__(self):
          return f'{self.title} {self.author}' 
     
     def get_absolute_url(self):
          return reverse('book_detail', args=[self.id])
    
     def get_borrow_url(self):
        return reverse("book-borrow", args=[f"{self.author.fullname}/{self.title}"])

     def get_genres(self):
        return [genre.name for genre in self.genre.all()]
    
     @property
     def instances(self):
        return BookInstace.objects.filter(book__exact=self.id)
    
     @property
     def available_instances(self):
       return [v for v in self.instances.all() if v.status==BookInstancStatus.Available]
   
     def borrow(self, user: User, due_time: datetime):
        availables = self.available_instances
        if len(availables) < 1:
            raise Exception(f"{str(self)} has no available instance to borrow")

        availables[0].borrow(user, due_time)

class BookInstancStatus:
    Available = "available"
    Borrowed = "borrowed"
    Maintainance = "maintainance"

class BookInstance(models.Model):
    book = models.ForeignKey(Book,on_delete=models.RESTRICT,null=True)
    borrower = models.ForeignKey(User,on_delete=models.RESTRICT,null=True,blank=True)
    borrow_due_time = models.DateField(null=True, blank=True)
    maintain_due_time = models.DateField(null=True, blank=True)
    @property
    def status(self):
        if self.borrower or self.borrow_due_time:
            return BookInstancStatus.Borrowed
        if self.maintain_due_time:
            return BookInstancStatus.Maintainance
        return BookInstancStatus.Available
    @property
    def is_available(self):
        return self.status == BookInstancStatus.Available
    def instance_of(self):
        return f'{self.book.title}by {self.book.author.fullname}'
    
    def get_absolute_url(self):
        return reverse("book_instance", args=[f'{self.id}'])
    
        def borrow(self, borrower: User, due_time: datetime):
            if not self.is_availabe:
                raise Exception(f"{BookInstace.id} is not available")

        self.borrower = borrower
        self.borrow_due_time = due_time
        self.save()
    
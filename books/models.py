from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse
from django.db.models.functions import Lower
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
        return reverse("genre_detail", args=[self.name])
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

     def get_genres(self):
        return [genre.name for genre in self.genre.all()]
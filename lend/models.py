from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    CATEGORY_CHOICE= (
        ('cat1','cat1'), ('cat3','cat3'), ('cat2','cat2'),
    )

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICE)
    author = models.CharField(max_length=50)
    description = models.TextField()
    published_at =models. DateTimeField(auto_now_add=True)
    pages = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
         return self.name


class BookInstace(models.Model):
       STATUS_CHOICES = (
        ('a', 'Available'),
        ('o', 'On loan'),
        ('r', 'Reserved'),
        ('m', 'Maintenance'),
        ('l', 'Lost'),
    )

       status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='a')

    
       book = models.ForeignKey(Book, on_delete=models.CASCADE)
       added_at = models.DateTimeField(auto_now_add=True)
       def __str__(self):
            return self.status


class Member(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.TextField()
    mobile_number = models.PositiveIntegerField()
    join_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.first_name


class Lend(models.Model):
    member = models.ForeignKey(Member, on_delete= models.CASCADE)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(auto_now=True)
    instance = models.ForeignKey(BookInstace,on_delete=models.CASCADE)

    def __str__(self):
         return self.member.last_name



class Comment(models.Model):
    text = models.TextField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    written_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.book.name




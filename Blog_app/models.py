
from django.db import models

# Create your models here.

class Author (models.Model):
    name = models.CharField(max_length = 255, null = False)
    description = models.CharField(max_length = 300, null = True)

    def __str__(self):
        return self.name

class Category (models.Model):
    name = models.CharField(max_length = 200, null = False)

    def __str__(self):
        return self.name

class Post  (models.Model):

    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(null= False)
    date_posted = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=300, null=True)
    likes = models.IntegerField(null=True)
    dislikes = models.IntegerField(null=True)
    Author_post = models.ForeignKey(to=Author, null=True, on_delete=models.CASCADE)
    post_category = models.ForeignKey(to=Category, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']
    

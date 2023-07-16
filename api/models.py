from django.db import models

# Create your models here.


class Genre(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.title


class Movie(models.Model):
    title=models.CharField(max_length=200)
    year=models.PositiveIntegerField()
    poster=models.ImageField(null=True,blank=True,upload_to='images/')
    disk_image=models.ImageField(null=True,blank=True,upload_to='images/')
    imdb=models.FloatField()
    story=models.TextField()
    gener=models.ManyToManyField(Genre)
    def __str__(self) -> str:
        return self.title



class ListMovie(models.Model):
    title=models.CharField(max_length=200)
    list=models.ManyToManyField(Movie)
    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    text=models.TextField()
    movie=models.ForeignKey(Movie,related_name='comment',on_delete=models.CASCADE)



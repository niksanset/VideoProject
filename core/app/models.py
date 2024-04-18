from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.title}'
        
        
class Director(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    avatar = models.ImageField(blank=True)
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return f'{self.name}'
    
class Media(models.Model):
    title = models.CharField(max_length=30)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE,null=True)
    add_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}'
    
class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_updated = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.media} - {self.created_at}'
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField()
    media = models.ForeignKey(Media, on_delete=models.CASCADE,null=True)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField()
    media = models.ForeignKey(Media, on_delete=models.CASCADE,null=True)
 


    
    

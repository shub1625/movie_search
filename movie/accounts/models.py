from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MovieUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=150,unique=True)
    email  = models.EmailField(null=True)
    profile_pic = models.ImageField(upload_to='photos/%Y-%m-%d/',blank=True)
    def __str__(self):
        return self.username
    
class Movie(models.Model):
    RATING = (
       (1,1),
       (2,2),
       (3,3),
       (4,4),
       (5,5)
        
    )
    username = models.ForeignKey(MovieUser,null =True , blank =True ,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    language = models.CharField(max_length=100)
    year = models.IntegerField(null=True,default=1996)
    rating = models.IntegerField(null=True, choices=RATING)
    movie_pic = models.ImageField(upload_to='photos/movies/',blank=True)

    def __str__(self):
        return self.title
    
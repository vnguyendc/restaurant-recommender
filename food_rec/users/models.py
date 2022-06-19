from django.db import models

from restaurants.models import Restaurant

# Create your models here.
class User(models.Model):
    '''
    User table
    - userID
    - name
    - email
    - lastLogin
    - numSearches
    - [likedRestaurants]
    '''
    name = models.CharField(max_length=40, default=None)
    email = models.EmailField()
    lastLogin = models.DateField()
    numSearches = models.IntegerField()
    likedRestaurants = models.ManyToManyField(
        Restaurant,
        verbose_name='list of liked restaurants'
    )

    def __str__(self):
        return self.name

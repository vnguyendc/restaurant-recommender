from tabnanny import verbose
from django.db import models

pricingRangeChoices = [
        ("$", "Cheap"),
        ("$$", "Moderate"),
        ("$$$", "Expensive"),
        ("$$$$", "Very Expensive")
    ]

class Restaurant(models.Model):
    '''
    Restaurant table
    - restID
    - name
    - location
    - rating
    - pricing
    - categories
    - ambianceType: TODO
    '''
    
    name = models.CharField(max_length=60)
    latitude = models.FloatField(max_length=32)
    longitude = models.FloatField(max_length=32)
    pricing = models.CharField(max_length=4, choices=pricingRangeChoices)
    categories = models.CharField(max_length=100)


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
    name = models.CharField(max_length=40)
    email = models.EmailField()
    lastLogin = models.DateField()
    numSearches = models.IntegerField()
    likedRestaurants = models.ManyToManyField(
        Restaurant,
        verbose_name='list of liked restaurants'
    )

class Preference(models.Model):
    '''
    Preferences table
    - prefID
    - userID: fk
    - ratingThreshold
    - pricingRange
    - cuisineKeyword
    - ambianceType: TODO
    - distance
    '''
    

    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name = "related user"
    )
    ratingThreshold = models.FloatField()
    pricingRange = models.CharField(max_length=4, choices=pricingRangeChoices)
    cuisineKeyword = models.CharField(max_length=60)
    # ambianceType = models.CharField(max_length)
    distance = models.IntegerField()
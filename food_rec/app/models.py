from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

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

    name = models.CharField(max_length=60, default=None)
    latitude = models.FloatField(max_length=32)
    longitude = models.FloatField(max_length=32)
    rating = models.FloatField(max_length=32, default=None)
    pricing = models.CharField(max_length=4, choices=pricingRangeChoices)
    categories = models.ManyToManyField(
        'Tag',
        verbose_name="keyword list"
    )

    def __str__(self):
        return self.name

class Tag(models.Model):
    '''
    Tags table
    - tagID
    - name
    '''

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Preference(models.Model):
    '''
    Preferences table
    - prefID
    - name
    - userID: fk
    - ratingThreshold
    - pricingRange
    - keywords
    - ambianceType: TODO
    - location
    - distance
    '''

    # name = models.CharField(max_length=60, default=None)
    # user = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     verbose_name="related user"
    # )
    # rating_threshold = models.FloatField()
    pricing_range = models.CharField(max_length=4, choices=pricingRangeChoices)
    keywords = models.ManyToManyField(
        Tag,
        verbose_name="keyword list"
    )
    # ambianceType = models.CharField(max_length)
    location = models.CharField(max_length=40)
    distance = models.IntegerField()

    def __str__(self):
        return self.name







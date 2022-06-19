from django.db import models

from app.models import pricingRangeChoices
from tags.models import Tag

# Create your models here.
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
        Tag,
        verbose_name="keyword list"
    )

    def __str__(self):
        return self.name

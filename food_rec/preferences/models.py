from django.db import models

from app.models import pricingRangeChoices
from users.models import User
from tags.models import Tag

# Create your models here.
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

    name = models.CharField(max_length=60, default=None)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="related user"
    )
    rating_threshold = models.FloatField()
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

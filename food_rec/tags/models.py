from django.db import models

# Create your models here.
class Tag(models.Model):
    '''
    Tags table
    - tagID
    - name
    '''

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
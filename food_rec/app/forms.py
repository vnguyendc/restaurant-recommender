from django import forms
from .models import Preference, Tag


# class PreferenceForm(forms.Form):
    
#     # rating threshold

#     # location

#     # distance

#     # keywords

#     # pricing range

#     class Meta:
#         model = Preference
#         fields = ['name', 'rating_threshold', 'location', 'distance', 'keywords', 'pricing_range']
    

class KeywordForm(forms.Form):
    keywords = forms.CharField(max_length=100)
class PriceRangeForm(forms.Form):
    pricingRangeChoices = [
        ("$", "Cheap"),
        ("$$", "Moderate"),
        ("$$$", "Expensive"),
        ("$$$$", "Very Expensive")
    ]
    pricing_range = forms.MultipleChoiceField(choices=pricingRangeChoices)

class LocationForm(forms.Form):

    location = forms.CharField(max_length=200)
    distance = forms.CharField(max_length=10)    
            
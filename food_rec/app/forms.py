from django import forms
from .models import Preference, Tag


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
            
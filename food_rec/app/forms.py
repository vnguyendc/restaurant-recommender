from django import forms
from .models import Preference, Tag

class PreferenceForm(forms.ModelForm):
    
    # rating threshold

    # location

    # distance

    # keywords

    # pricing range

    class Meta:
        model = Preference
        fields = ['name', 'rating_threshold', 'location', 'distance', 'keywords', 'pricing_range']
    
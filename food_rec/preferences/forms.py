from django import forms
from .models import Preference
from tags.models import Tag

class PreferenceForm(forms.ModelForm):
    
    # rating threshold

    # location

    # distance

    # keywords

    # pricing range

    class Meta:
        model = Preference
        fields = ['rating_threshold', 'location', 'distance', 'keywords', 'pricing_range']
    
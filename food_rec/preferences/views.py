from django.shortcuts import render
from .forms import PreferenceForm
from .models import Preference

'''
view to create:
- GET list of preferences by user
- POST a new preference by user
- POST edit an existing preference
- Delete a preference
'''

# Create your views here.
def preference_list(request):
    preferences = Preference.objects.all()
    context = {'preferences': preferences}

    return render(request, 'preferences/home.html', context)

def add_preference(request):
    if request.method == 'POST':
        form = PreferenceForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = PreferenceForm()

    context = {'form': form}

    return render(request, 'preferences/create.html', context)

def edit_preference(request):
    context = {}
    return render(request, 'preferences/edit.html', context)

def delete_preference(request):
    return
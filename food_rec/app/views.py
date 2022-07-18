from django.shortcuts import render
from django.http import HttpResponse

from .forms import PreferenceForm
from .models import Preference

# Create your views here.
def index(request):
    context = {'name': request.user}
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'registration/login.html')


# PREFERENCES VIEWS


def preference_list(request):
    preferences = Preference.objects.all()
    context = {'preferences': preferences}

    return render(request, 'preferences/show.html', context)

def preference(request):
    context = {}
    return render(request, '')

def create_preference(request):
    # if request.method == 'POST':
    #     form = PreferenceForm(request.POST)

    #     if form.is_valid():
    #         form.user = request.user
    #         form.save()
    # else:
    #     form = PreferenceForm()

    form = PreferenceForm(request.POST or None)
    if form.is_valid():
        # optionally we can access form data with form.cleaned_data['first_name']
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        # return HttpResponse('Preference created successfully!')
        

    context = {'form': form}

    return render(request, 'preferences/create.html', context)

def edit_preference(request):
    context = {}
    return render(request, 'preferences/edit.html', context)

def delete_preference(request):
    return


'''
#### RESTAURANT VIEWS
    - get a preference
    - do a search based on that preference
    - get search results with list of restaurants
    - view list of restaurants
'''

def restaurants(request):
    return HttpResponse('Restaurant View')
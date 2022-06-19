from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'name': 'Vinh'}
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'registration/login.html')

def setPreferenceView(request):
    return render(request, 'setPreference.html')
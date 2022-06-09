from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'name': 'Vinh'}
    return render(request, 'hello/index.html', context)

def login(request):
    return render(request, 'login.html')

def setPreferenceView(request):
    return render(request, 'setPreference.html')
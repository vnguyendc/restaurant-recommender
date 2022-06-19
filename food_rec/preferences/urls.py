from django.urls import path
from preferences import views as preference_views

app_name = 'preferences'

urlpatterns= [
    path('', preference_views.preference_list, name='home'),
    path('create/', preference_views.add_preference, name='create')
]
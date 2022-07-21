from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("preference/<str:pk>", views.preference, name="preference"),
    path('create-preference/', views.create_preference, {'step': None}, name='create-preference'),
    path('step/<int:step>', views.create_preference)
    # path('all-preferences/', views.preference_list, name='all-preferences')
]
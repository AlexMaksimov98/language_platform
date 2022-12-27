from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllCasesView.as_view(), name='all-cases'),
    path('<slug>', views.TopicView.as_view(), name='case'), 
    path('<slug:slug_topic>/<slug:slug_exercise>', views.ExerciseView.as_view(), name='exercise')
]

from django.forms import ModelForm
from .models import *

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['correct_answer']
    
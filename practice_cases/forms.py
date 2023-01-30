from django import forms
from django.forms import ModelForm
from .models import *

class ExerciseForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['correct_answer'].widget.attrs.update({'id': 'correct_answer'})
        

    class Meta:
        model = Exercise
        fields = ['correct_answer'] 

    
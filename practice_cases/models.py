from django.db import models
from django.urls import reverse

class Case(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    cases = models.ForeignKey(Case, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    sentence = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=50, blank=True)
    topic_type = models.ForeignKey(Topic, on_delete=models.CASCADE)
    initial_form = models.CharField(max_length=100, blank=True)
    translation = models.CharField(max_length=200, blank=True)
    second_part = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return f'{self.sentence}{self.correct_answer} {self.second_part}'
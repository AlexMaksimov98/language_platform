from django.db import models

class GrammarSection(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return self.name

class GrammarTopic(models.Model):
    name = models.CharField(max_length=50)
    grammar_section_name = models.ForeignKey(GrammarSection, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

class GrammarTheorySection(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    type = models.ForeignKey(GrammarTopic, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=True)
    rule = models.CharField(max_length=500, blank=True)
    questions = models.CharField(max_length=50, blank=True)
    functions = models.CharField(max_length=500, blank=True)
    examples = models.CharField(max_length=500, blank=True)

    def __str__(self):
         return self.title
    

from django.views import View
from django.shortcuts import render
from .models import *


class AllGrammarTopicsView(View):
    def get(self, request):
        all_topics = GrammarSection.objects.all()
        return render(request, 'grammar_section/all_topics.html', {
            'grammar_topics': all_topics
        })

class GrammarTopicView(View):
    def get(self, request, **kwargs):
        subtopics = GrammarTopic.objects.filter(grammar_section_name__slug=kwargs['slug']).all()
        return render(request, 'grammar_section/grammar_topic.html',{
            'subtopics': subtopics
        })
    
class GrammarTheoryView(View):
    def get(self, request, **kwargs):
        chosen_topic = GrammarTheorySection.objects.filter(slug=kwargs['topic_name']).first()
        return render(request, 'grammar_section/theory_section.html', {
            'language_section': str(chosen_topic.type.grammar_section_name),
            'title': chosen_topic.title,
            'description': chosen_topic.description,
            'rule': chosen_topic.rule     
        })
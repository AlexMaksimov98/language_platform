import time
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *


class AllCasesView(View):

    def get(self, request):
        return render(request, 'practice_cases/all-cases.html', {
            'cases': Case.objects.all()
        })


class TopicView(View):

    def get(self, request, **kwargs):
        return render(request, 'practice_cases/case.html', {
            'topics': Topic.objects.filter(cases__slug=kwargs['slug']).all()
        })


class ExerciseView(View):

    def get(self, request, **kwargs):
        data = Exercise.objects.filter(topic_type__slug=kwargs['slug_exercise']).all()
        sentence_index = request.session.setdefault('sentence_index', 0)
        score = request.session.setdefault('score', 0)
        sentences = request.session.setdefault('sentences', {})
        for item in data:
            sentences[item.sentence] = item.correct_answer
        length = request.session.setdefault('length', len(sentences))
        if length == sentence_index:
            return render(request, 'practice_cases/exercise.html', {
                'message': 'You have just completed the test',
                'score': score,
                'length': length, 
            })
        chosen_sentence = request.session.get('chosen_sentence', list(sentences.keys())[sentence_index])
        return render(request, 'practice_cases/exercise.html', {
                'sentence': chosen_sentence,
                'form': ExerciseForm(),
                'score': score,
                'length': length
        })

    def post(self, request, **kwargs):
        form = ExerciseForm(request.POST)
        sentence_index = request.session.get('sentence_index')
        sentences = request.session.get('sentences')
        if form.is_valid():
            if 'check_answer' in request.POST:
                answered_ending = form.cleaned_data['correct_answer']
                correct_ending = request.session.get('correct_ending', list(sentences.values())[sentence_index])
                if answered_ending == correct_ending:
                    request.session['score'] += 1
                request.session['sentence_index'] += 1
            elif 'finish' in request.POST:
                score = request.session.get('score')
                length = request.session.get('length')
                keys = ['sentence_index', 'score', 'sentences', 'length']
                for key in keys:
                    del request.session[key]
                return render(request, 'practice_cases/all-cases.html', {
                    'message': 'You have just completed the test without reaching the end',
                    'score': score,
                    'length': length
                })
            elif 'return_homepage' in request.POST:
                keys = ['sentence_index', 'score', 'sentences', 'length']
                for key in keys:
                    del request.session[key]
                return redirect(reverse('homepage'))
            elif 'next' in request.POST:
                request.session['sentence_index'] += 1
        return HttpResponseRedirect(self.request.path_info)

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
            'topics': Topic.objects.filter(cases__slug=kwargs['slug']).all(),
            'case_name': Case.objects.filter(slug=kwargs['slug']).first()
        })


class ExerciseView(View):

    def get(self, request, **kwargs):
        data = request.session.setdefault('exercises_data', list(Exercise.objects.filter(topic_type__slug=kwargs['slug_exercise']).all().order_by('?').values('sentence', 'correct_answer', 'initial_form', 'second_part', 'translation')))
        id = request.session.setdefault('sentence_id', 0)
        score = request.session.setdefault('score', 0)
        sentences = request.session.setdefault('sentences', {})
        for i in range(0, len(data)):
            sentences[i] = {
                'sentence': data[i]['sentence'],
                'correct_answer': data[i]['correct_answer'],
                'translation': data[i]['translation'],
                'initial_form': data[i]['initial_form'],
                'second_part': data[i]['second_part']
            }
        length = request.session.setdefault('length', len(sentences))
        if length == id:
            return render(request, 'practice_cases/exercise.html', {
                'message': 'You have just completed the test!',
                'score': score,
                'length': length,
            })
        else:
            if 'adjectives' in kwargs['slug_exercise'] or 'possessives' in kwargs['slug_exercise']:
                chosen_sentence = request.session.get('chosen_sentence', sentences[id]['sentence'])
                sentence_translation = request.session.get('sentence_translation', sentences[id]['translation'])
                initial_form = request.session.get('initial_form', sentences[id]['initial_form'])
                correct_answer = request.session.get('correct_answer', sentences[id]['correct_answer'])
                second_part = request.session.get('second_part', sentences[id]['second_part'])
                return render(request, 'practice_cases/exercise.html', {
                    'sentence': chosen_sentence,
                    'form': ExerciseForm(),
                    'score': score,
                    'length': length,
                    'translation': sentence_translation,
                    'initial_form': initial_form,
                    'correct_answer': correct_answer,
                    'second_part': second_part
            })
            else:
                chosen_sentence = request.session.get('chosen_sentence', sentences[id]['sentence'])
                sentence_translation = request.session.get('sentence_translation', sentences[id]['translation'])
                correct_answer = request.session.get('correct_answer', sentences[id]['correct_answer'])
                initial_form = request.session.get('initial_form', sentences[id]['initial_form'])
                second_part = request.session.get('second_part', sentences[id]['second_part'])
                return render(request, 'practice_cases/exercise.html', {
                    'sentence': chosen_sentence,
                    'form': ExerciseForm(),
                    'score': score,
                    'length': length,
                    'translation': sentence_translation,
                    'correct_answer': correct_answer,
                    'second_part': second_part,
                    'initial_form': initial_form
            })



    def post(self, request, **kwargs):
        form = ExerciseForm(request.POST)
        id = request.session.get('sentence_id')
        sentences = request.session.get('sentences')
        if form.is_valid():
            if 'check_answer' in request.POST:
                answered_ending = form.cleaned_data['correct_answer']
                correct_answer = sentences[str(id)]['correct_answer']
                if answered_ending == correct_answer:
                    request.session['score'] += 1
                request.session['sentence_id'] += 1
                print(answered_ending, correct_answer)
                time.sleep(3)
            elif 'finish' in request.POST:
                score = request.session.get('score')
                length = request.session.get('length')
                keys = ['score', 'sentences', 'length', 'sentence_id', 'exercises_data']
                for key in keys:
                    del request.session[key]
                return render(request, 'practice_cases/all-cases.html', {
                    'message': 'You have just completed the test without reaching the end :(',
                    'score': score,
                    'length': length
                })
            elif 'return_homepage' in request.POST:
                keys = ['score', 'sentences', 'length', 'sentence_id', 'exercises_data']
                for key in keys:
                    del request.session[key]
                return redirect(reverse('homepage'))
            elif 'next' in request.POST:
                request.session['sentence_id'] += 1
        return HttpResponseRedirect(self.request.path_info)
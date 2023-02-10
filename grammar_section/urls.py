from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllGrammarTopicsView.as_view(), name='all_grammar_topics'),
    path('<slug>', views.GrammarTopicView.as_view(), name='grammar_topic'),
    path('<slug>/<topic_name>', views.GrammarTheoryView.as_view(), name='grammar_theory')
]

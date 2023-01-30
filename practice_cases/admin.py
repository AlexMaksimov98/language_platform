from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import *

class CaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ExerciseAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('sentence', 'correct_answer', 'topic_type', 'initial_form', 'translation', 'second_part')

admin.site.register(Case, CaseAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Exercise, ExerciseAdmin)

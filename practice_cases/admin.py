from django.contrib import admin
from .models import *

class CaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Case, CaseAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Exercise)

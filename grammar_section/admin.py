from django.contrib import admin
from .models import *

class GrammarSectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} 

class GrammarTopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class GrammarTheorySectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(GrammarSection, GrammarSectionAdmin)
admin.site.register(GrammarTopic, GrammarTopicAdmin)
admin.site.register(GrammarTheorySection, GrammarTheorySectionAdmin)
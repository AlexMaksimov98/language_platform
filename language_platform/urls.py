from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('cases/', include('practice_cases.urls')),
    path('grammar/', include('grammar_section.urls'))
]

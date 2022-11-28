from django.views.generic import TemplateView, FormView, View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from .forms import NewUserForm


class HomepageView(TemplateView):
    template_name = 'main_app/homepage.html'

class LoginView(FormView):
    template_name = 'main_app/login.html'
    form_class = AuthenticationForm
    success_url = '/'   
    
    def form_valid(self, form):
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request=self.request, user=user)
            return redirect('/')
        return super().form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class RegisterView(FormView):
    template_name = 'main_app/register.html'
    form_class = NewUserForm
    success_url = '/login'

    def form_valid(self, form: NewUserForm):
        user = form.save()
        return super().form_valid(form)
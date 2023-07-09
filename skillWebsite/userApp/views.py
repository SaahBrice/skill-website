from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import LecturerSignupForm, SecretarySignupForm
from .models import User, Lecturer, Secretary
from django.views.generic import CreateView
from django import forms
from django.contrib import messages

# Create your views here.



class SecretarySignupView(CreateView):
    model = User
    form_class = SecretarySignupForm
    template_name = 'signup/secretary.html'
    def get_context_data(self, **kwargs):
        kwargs['usertype']=1
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.data_save()
        authenticated_user = authenticate(username=form.cleaned_data.get('username'), password= form.cleaned_data.get('password1'))
        if authenticated_user is not None:
            #login(self.request, authenticated_user)
            return redirect('home')
    def form_invalid(self, form):
        error_message = "There was an error in the form data. Please correct the errors and try again."
        form.add_error(None, error_message)
        return self.render_to_response(self.get_context_data(form=form))

class LecturerSignupView(CreateView):
    model = User
    form_class = LecturerSignupForm
    template_name = 'signup/lecturer.html'
    def get_context_data(self, **kwargs):
        kwargs['usertype']=2
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.data_save()
        authenticated_user = authenticate(username=form.cleaned_data.get('username'), password= form.cleaned_data.get('password1'))
        if authenticated_user is not None:
            login(self.request, authenticated_user)
            return redirect('home')
    def form_invalid(self, form):
        error_message = "There was an error in the form data. Please correct the errors and try again."
        form.add_error(None, error_message)
        return self.render_to_response(self.get_context_data(form=form))



def login_user(request):
    if request.method == 'POST':
        _username = request.POST['name']
        _password = request.POST['message']
        user = authenticate(username = _username, password = _password)
        if user is not None:
            if user.usertype ==1:
                login(request, user)
                return redirect(reverse_lazy('user_home'))
        
        #form= AuthenticationForm(data=request.POST)
        ##if form.is_valid():
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=password)
            #if user is not None:
                #if user.usertype == 1:
                    #login(request, user)
                    #return redirect(reverse_lazy('user_home'))
                #elif user.usertype == 2:
                    #login(request, user)
                    #return redirect(reverse_lazy('home'))
        else:
            messages.success(request, "Nom d'utilisateur ou mot de passe incorrect. Reessayez svp!")
            return redirect('login_user')
    return render(request, 'signup/login.html')


def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('home'))
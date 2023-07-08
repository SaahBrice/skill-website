from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import LecturerSignupForm, SecretarySignupForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        print(request.POST['username'])
        print(request.POST['password'])

    print('HELLO')
    _user = authenticate(username = request.POST['username'], password = request.POST['password'])
    if _user is not None:
        print('logged in')
    else:
        print('an error occured')
    return redirect('home')




class SecretarySignupView(CreateView):
    model = User
    form_class = SecretarySignupForm
    template_name = 'signup/Secretary.html'
    def get_context_data(self, **kwargs):
        kwargs['usertype']=2
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.data_save()
        authenticated_user = authenticate(username=form.cleaned_data.get('username'), password= form.cleaned_data.get('password1'))
        if authenticated_user is not None:
            login(self.request, authenticated_user)
            return redirect(reverse_lazy('consumer_dashboard'))
    def form_invalid(self, form):
        error_message = "There was an error in the form data. Please correct the errors and try again."
        form.add_error(None, error_message)
        return self.render_to_response(self.get_context_data(form=form))
    
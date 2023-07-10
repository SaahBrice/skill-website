from django.shortcuts import render
from .forms import CaptchaTestForm, UploadFilesForm
# Create your views here.


def home(request):
    return render(request, 'frontPages/index.html')


def formationCarte(request):
    return render(request, 'frontPages/meetings.html')

def formationNormal(request):
    return render(request, 'frontPages/meetings.html')

def userHome(request):
    return render(request, 'frontPages/user-home.html')

def apply(request):
    _file = UploadFilesForm
    _captcha = CaptchaTestForm
    context ={
        'file':_file,
        'captcha':_captcha,
    }
    return render(request, 'frontPages/documents.html', context)


def carte(request):
    return render(request, 'frontPages/carte.html')
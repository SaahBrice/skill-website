from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'frontPages/index.html')


def formationCarte(request):
    return render(request, 'frontPages/meetings.html')

def formationNormal(request):
    return render(request, 'frontPages/meetings.html')

def userHome(request):
    return render(request, 'frontPages/user-home.html')
from django.shortcuts import render, redirect
from .forms import CaptchaTestForm, UploadFilesForm, ModuleForm
from django.contrib import messages
from .models import DocumentPostuler, Module
# Create your views here.


def home(request):
    return render(request, 'frontPages/index.html')


def delete_module(request, id):
    module = Module.objects.get(pk = id).delete()
    return redirect('module')

def module(request):
    modules = Module.objects.all()
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('module')
        else:
            print('hello ')
    else:
        module_form = ModuleForm()
    context = {
        'modules': modules,
        'module_form': module_form,
    }
    return render(request, 'frontPages/module.html', context)


def formationCarte(request):
    return render(request, 'frontPages/meetings.html')

def formationNormal(request):
    return render(request, 'frontPages/meetings.html')

def userHome(request):
    documents = DocumentPostuler.objects.all()
    context = {
        'documents': documents
    }
    return render(request, 'frontPages/user-home.html', context)

def apply(request):
    _file = UploadFilesForm(prefix='file_upload')
    _captcha = CaptchaTestForm(prefix='captcha')
    context ={
        'file':_file,
        'captcha':_captcha,
    }
    if request.method == 'POST':
        captcha = CaptchaTestForm(request.POST, prefix='captcha')
        file_form = UploadFilesForm(request.POST, request.FILES, prefix='file_upload')
        if captcha.is_valid():
            if file_form.is_valid():
                file_form.save()
                messages.add_message(request, messages.SUCCESS, 'Merci! Vos document ont ete envoyer')
                return redirect('apply')
            else:
                messages.add_message(request, messages.ERROR, 'Ola! Il y a un problème avec vos documents. Vérifiez que leur taille est inférieure à 5 Mo. Si le problème persiste, veuillez nous contacter. ') 
        else:
            messages.add_message(request, messages.ERROR, 'Ola! Reponse teste robot incorrect. SVP veillez reessayer.')
    return render(request, 'frontPages/documents.html', context)


def carte(request):
    return render(request, 'frontPages/carte.html')
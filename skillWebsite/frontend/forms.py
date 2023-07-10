from django import forms
from .models import DocumentPostuler
from captcha.fields import CaptchaField


class UploadFilesForm(forms.ModelForm):
    max_file_size = 5*1024
    class Meta:
        model = DocumentPostuler
        fields = ['name','number','email','pays','ville','birthCertificate','identityDocument','recentCertificate','signedEngagement',]
        labels = {
            'name': 'Nom',
            'number': 'Numéro ex.(237688888888)',
            'email': 'Email',
            'ville': 'Ville',
            'pays': 'Pays',
            'birthCertificate': 'Certificat de naissance',
            'identityDocument': 'Document d\'identité',
            'recentCertificate': 'Diplôme récent',
            'signedEngagement': 'Fiche d\'enregistrement signé',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control mb-4'}),
            'pays': forms.Select(attrs={'class': 'form-control'}),
            'birthCertificate': forms.ClearableFileInput(attrs={'class': 'form-control '}),
            'identityDocument': forms.ClearableFileInput(attrs={'class': 'form-control '}),
            'recentCertificate': forms.ClearableFileInput(attrs={'class': 'form-control '}),
            'signedEngagement': forms.ClearableFileInput(attrs={'class': 'form-control mb-4'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'email':
                field.required = True
    def clean(self):
        cleaned_data = super().clean()
        for field_name in self.files:
            file = cleaned_data.get(field_name)
            if file:
                if file.size > self.max_file_size:
                    self.add_error(field_name, f"Le fichier est trop gros (taille maximale de {self.max_file_size / 1024:.2f} Mo)" )

class CaptchaTestForm(forms.Form):
    captcha = CaptchaField(error_messages={'invalid': '<Your custom message>'})

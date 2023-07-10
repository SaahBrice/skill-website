from django import forms
from .models import DocumentPostuler
from captcha.fields import CaptchaField


class UploadFilesForm(forms.ModelForm):
    max_file_size = 5*1024
    class Meta:
        model = DocumentPostuler
        fields = '__all__'
    def clean(self):
        cleaned_data = super().clean()
        for field_name in self.files:
            file = cleaned_data.get(field_name)
            if file:
                if file.size > self.max_file_size:
                    self.add_error(field_name, f"Le fichier est trop gros (taille maximale de {self.MAX_FILE_SIZE / 1024 / 1024:.2f} Mo)" )
                    
class CaptchaTestForm(forms.Form):
    captcha = CaptchaField()
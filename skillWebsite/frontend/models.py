from django.db import models
from django_countries.fields import CountryField
# Create your models here.



class DocumentPostuler(models.Model):
    name = models.CharField(blank=True, max_length=50)
    number = models.PositiveIntegerField(blank=True, max_length=12)
    email = models.EmailField(blank=True, max_length=50)
    ville = models.CharField(blank=True, max_length=50)
    pays = CountryField()
    birthCertificate = models.FileField(blank=True, upload_to='media/document', max_length=100)
    identityDocument = models.FileField(blank=True, upload_to='media/document', max_length=100)
    recentCertificate = models.FileField(blank=True, upload_to='media/document', max_length=100)
    signedEngagement = models.FileField(blank=True, upload_to='media/document', max_length=100)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = "DocumentPostuler"
        verbose_name_plural = "DocumentPostulers"

    def __str__(self):
        return self.name


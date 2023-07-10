from django.db import models
from django_countries.fields import CountryField
# Create your models here.

class moduleTypeChoice(models.Model):
    MODULE_TYPE_CHOICES = [
        ('a_la_carte', 'A la carte'),
        ('formation', 'Formation'),
    ]

class Module(models.Model):
    name = models.CharField(blank=False, max_length=50)
    description= models.CharField(blank=True, max_length=50)
    moduleType = models.CharField(blank=True,null=True,choices=moduleTypeChoice.MODULE_TYPE_CHOICES, default='formation', max_length=50)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"

    def __str__(self):
        return self.name





class DocumentPostuler(models.Model):
    name = models.CharField(blank=True, max_length=50)
    number = models.PositiveIntegerField(blank=True, max_length=12)
    email = models.EmailField(blank=True, max_length=50)
    ville = models.CharField(blank=True, max_length=50)
    module = models.ForeignKey(Module, on_delete=models.DO_NOTHING, related_name='documents', null=True)
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


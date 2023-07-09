from django.db import models
from django.contrib.auth.models import AbstractUser


class UserChoices(models.IntegerChoices):
    SECRETARY = 1, 'Secretary'
    LECTURER = 2, 'Lecturer'

class User(AbstractUser):
    usertype = models.PositiveIntegerField(choices=UserChoices.choices, blank=True, default = UserChoices.SECRETARY)

    def __str__(self):
        return self.username


class Secretary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='secretary')
   
    class Meta:
        verbose_name = "secretary"
        verbose_name_plural = "secretaries"
    def __str__(self):
        return self.user.username
    

class Lecturer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='lecturer')

    class Meta:
        verbose_name = "lecturer"
        verbose_name_plural = "lecturers"
    def __str__(self):
        return self.user.username
from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Profile(AbstractUser):
    email = models.CharField(max_length=155, unique = True)
    cpf = models.CharField(max_length=11)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    



class Livro(models.Model):
    titulo = models.CharField(max_length = 30)
    editora = models.CharField(max_length= 30)
    autor = models.CharField(max_length = 30)
    ano = models.IntegerField()

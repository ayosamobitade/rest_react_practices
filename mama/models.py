from django.db import models

# Create your models here.

class momo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length = 20, unique = True)
    messaga = models.TextField(max_length = 200, blank = True)
    create_at = models.DateTimeField(auto_now_add = True)
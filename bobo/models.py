from django.db import models

# Create your models here.

class boboso(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 30, unique = True)
    message = models.TextField(max_length = 200)
    create_at = models.DateTimeField(auto_now_add = True)
    



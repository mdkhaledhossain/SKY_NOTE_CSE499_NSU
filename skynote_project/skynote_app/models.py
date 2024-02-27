from django.db import models

# Create your models here.
    
class Notefile(models.Model):
    title = models.CharField(max_length=100)
    note_text = models.TextField()
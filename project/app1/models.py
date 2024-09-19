from django.db import models

# Create your models here.
# models.py
from django.db import models

class SpokenText(models.Model):
    text = models.TextField()  # Field to store the spoken text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the text was saved

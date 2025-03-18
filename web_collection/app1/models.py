from django.db import models

# Create your models here.
class Collection(models.Model):
    name=models.CharField(max_length=20)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcollections')

    def __str__(self):
        return self.name
# from django.db import models

# from django.db import models

# class Collection(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

#     def __str__(self):
#         return self.name
from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

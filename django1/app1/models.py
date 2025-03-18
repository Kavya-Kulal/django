from django.db import models

class GithubURL(models.Model):
    url1 = models.URLField(unique=True)

    def __str__(self):
        return self.url1

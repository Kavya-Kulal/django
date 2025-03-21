from django.db import models

class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)  # Auto-incrementing, no default needed
    collection_name = models.CharField(max_length=255)  # Default 'c' if no name is provided
    created_at = models.DateTimeField(auto_now_add=True)  # Stores creation time

    def __str__(self):
        return self.collection_name  # Corrected attribute name

    
class Urls(models.Model):
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="bookmarks")
    url_id= models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

   
    def __str__(self):
        return self.url

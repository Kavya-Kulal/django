from django.db import models

class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)  # Auto-incrementing, no default needed
    collection_name = models.CharField(max_length=255)  # Default 'c' if no name is provided
    created_at = models.DateTimeField(auto_now_add=True)  # Stores creation time

    def __str__(self):
        return self.collection_name  # Corrected attribute name

    
class Url(models.Model):
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="bookmarks")
    url= models.URLField(unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

   
    def __str__(self):
        return self.url
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Collection  # Assuming you have a Collection model

@csrf_exempt
def rename_collection(request, collection_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            new_name = data.get("new_name")

            # Fetch collection from DB and update the name
            collection = Collection.objects.get(id=collection_id)
            collection.collection_name = new_name
            collection.save()

            return JsonResponse({"success": True})
        except Collection.DoesNotExist:
            return JsonResponse({"success": False, "error": "Collection not found"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    
    return JsonResponse({"success": False, "error": "Invalid request"})

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from .models import Collection

# Create your views here.
def home(request):

    return render(request, "app1/index.html")


def create_collection(request):
    if request.method == "POST":
        name = request.POST.get("name")
        parent_id = request.POST.get("parent_id", None)

        if name:
            parent = Collection.objects.filter(id=parent_id).first() if parent_id else None
            collection, created = Collection.objects.get_or_create(name=name, parent=parent)

            return JsonResponse({"success": True, "id": collection.id, "name": collection.name, "parent_id": parent_id})
    
    return JsonResponse({"success": False, "error": "Invalid request"})
from django.http import JsonResponse
from .models import Collection  # Ensure Collection model exists

def get_collections(request):
    collections = list(Collection.objects.values("name"))
    return JsonResponse({"collections": collections})

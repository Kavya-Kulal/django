# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse


# def home(request):
#     return render(request, 'app1/index.html')
from django.shortcuts import render
from django.http import JsonResponse
from .models import Collection
import json

def home(request):
    collections = Collection.objects.all()  # Fetch saved collections
    return render(request, "index.html", {"collections": collections})

def insert_collection(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            name = data.get("name")

            if name:
                new_collection = Collection.objects.create(name=name)
                return JsonResponse({"success": True, "name": new_collection.name})
            else:
                return JsonResponse({"success": False, "error": "No name provided!"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request!"})

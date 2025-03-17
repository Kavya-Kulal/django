# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Collection
# import json

# def home(request):
#     collections = Collection.objects.all()  # Fetch existing collections
#     return render(request, "index.html", {"collections": collections})

# def insert_collection(request):
#     if request.method == "POST":
#         data = json.loads(request.body)  # Read JSON from request
#         name = data.get("name")
#         if name:
#             Collection.objects.create(name=name)  # Insert into DB
#             return JsonResponse({"success": True, "name": name})
#     return JsonResponse({"success": False})
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

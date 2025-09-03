import os
from django.shortcuts import render, redirect
from .models import MRIImage
from django.conf import settings
from backend.predict import predict_image  # <-- use your ML predict.py

def upload_image(request):
    if request.method == "POST":
        mri_file = request.FILES.get("mri_image")
        if mri_file:
            # Save image to DB
            image_obj = MRIImage.objects.create(image=mri_file)

            # Run prediction using your ML model
            image_path = os.path.join(settings.MEDIA_ROOT, image_obj.image.name)
            result = predict_image(image_path)

            # Pass result to result page
            return render(request, "tumor/result.html", {"result": result})

    return render(request, "tumor/upload.html")


def result(request):
    # In case user visits directly
    return render(request, "tumor/result.html", {"result": "No prediction yet"})

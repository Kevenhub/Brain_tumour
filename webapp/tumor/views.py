from django.shortcuts import render
from .forms import ImageUploadForm
from mlmodels.prediction import predict_tumor   # we'll create this
import os
from django.conf import settings

def upload_image(request):
    result = None
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data["image"]

            # Save uploaded file to MEDIA folder
            file_path = os.path.join(settings.MEDIA_ROOT, image.name)
            with open(file_path, "wb+") as f:
                for chunk in image.chunks():
                    f.write(chunk)

            # Call your ML model
            result = predict_tumor(file_path)  
    else:
        form = ImageUploadForm()

    return render(request, "tumor/upload.html", {"form": form, "result": result})

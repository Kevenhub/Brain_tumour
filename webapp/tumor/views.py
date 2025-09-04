import os
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from backend.predict import predict_image   # ✅ import your function

def upload_image(request):
    context = {}
    if request.method == "POST" and request.FILES.get("image"):
        uploaded_file = request.FILES["image"]

        # Save uploaded image to MEDIA folder
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, "uploads"))
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url("uploads/" + filename)

        # Full path for backend prediction
        image_path = os.path.join(settings.MEDIA_ROOT, "uploads", filename)

        # Call your ML prediction
        label, confidence, _ = predict_image(image_path)

        context = {
            "file_url": file_url,
            "label": label,
            "confidence": f"{confidence*100:.2f}%",
        }

    return render(request, "tumor/upload.html", context)

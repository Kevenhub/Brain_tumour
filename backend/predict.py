import os
import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Get absolute path of model file inside backend/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "brain_tumor_model.h5")

# Load trained model
model = tf.keras.models.load_model(MODEL_PATH)

def predict_image(image_path):
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"❌ Could not load image from {image_path}")

    # Convert BGR (cv2) -> RGB (matplotlib expects RGB)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # ✅ Resize to match training input size (128x128)
    img_resized = cv2.resize(img_rgb, (128, 128))

    # Normalize
    img_normalized = img_resized.astype("float32") / 255.0  

    # Add batch dimension
    img_input = np.expand_dims(img_normalized, axis=0)  

    # Predict
    prediction = model.predict(img_input)[0][0]  # single sigmoid output

    if prediction >= 0.5:
        label = "Tumor"
        confidence = prediction
    else:
        label = "No Tumor"
        confidence = 1 - prediction

    return label, confidence, img_rgb

if __name__ == "__main__":
    image_path = input("📂 Enter the path of the MRI image: ").strip()

    if not os.path.exists(image_path):
        print("❌ File not found. Please check the path and try again.")
    else:
        label, conf, img_rgb = predict_image(image_path)
        print(f"🧠 Prediction: {label} ({conf*100:.2f}% confidence)")

        # ✅ Show image with prediction
        plt.imshow(img_rgb)
        plt.title(f"Prediction: {label} ({conf*100:.2f}%)")
        plt.axis("off")
        plt.show()

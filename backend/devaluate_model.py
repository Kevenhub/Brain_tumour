import tensorflow as tf
from aload_data import load_data

# Load trained model
model = tf.keras.models.load_model("brain_tumor_model.h5")

# Dataset paths
train_dir = "dataset/train"
test_dir = "dataset/test"

# Load test data
_, test_data = load_data(train_dir, test_dir)

# Evaluate model
loss, acc = model.evaluate(test_data)
print(f"✅ Test Accuracy: {acc*100:.2f}% | Test Loss: {loss:.4f}")

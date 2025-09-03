import os
from tensorflow.keras.optimizers import Adam # type: ignore
from aload_data import load_data
from backend.build_model import build_model

# Dataset paths
train_dir = "dataset/train"
test_dir = "dataset/test"

# Parameters
img_size = 128
batch_size = 32
epochs = 15

# Load data
train_data, test_data = load_data(train_dir, test_dir, img_size, batch_size)

# Build model
model = build_model(img_size)
model.compile(
    loss='binary_crossentropy',
    optimizer=Adam(learning_rate=0.0001),
    metrics=['accuracy']
)

# Train model
history = model.fit(
    train_data,
    epochs=epochs,
    validation_data=test_data
)

# Save trained model
model.save("brain_tumor_model.h5")
print("✅ Model saved as brain_tumor_model.h5")

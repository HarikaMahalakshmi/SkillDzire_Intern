# MNIST Digit Classifier using Keras

This project is a basic implementation of a neural network to classify handwritten digits from the MNIST dataset using TensorFlow and Keras.

---

## Dataset

- **MNIST**: Contains 70,000 grayscale images of handwritten digits (0–9)
  - **Training set**: 60,000 images
  - **Test set**: 10,000 images
  - Each image is **28×28 pixels** in size

---

## Model Architecture

- **Model Type**: Fully Connected Neural Network (Sequential)
- **Input Layer**: Flattened 784-dimensional vector (28x28 image)
- **Output Layer**: 10 neurons with `sigmoid` activation (for digits 0–9)

> ⚠️ Note: `sigmoid` is used here for simplicity, but `softmax` is recommended for multi-class classification.

---

## 🛠️ Dependencies

```bash
pip install tensorflow matplotlib


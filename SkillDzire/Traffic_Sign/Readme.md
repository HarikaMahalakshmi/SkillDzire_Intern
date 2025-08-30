# Project Objective

To build and train a **Convolutional Neural Network (CNN)** using TensorFlow and Keras that can classify images into multiple categories from a Traffic Signs Dataset. The model uses **data augmentation**, **image normalization**, and several convolutional layers to learn robust visual patterns.


# Implementation Overview

### 1. **Dataset Loading**
- Images are loaded using `image_dataset_from_directory()`
- Dataset is split into 80% training and 20% validation.

### 2. **Data Augmentation**
- Random flip (horizontal and vertical)
- Random rotation (±10%)
- Random zoom (up to 20%)

### 3. **Model Architecture**
- CNN with the following layers:
- Data Augmentation
- Rescaling (normalize pixel values)
- 4 × Conv2D + MaxPooling2D blocks
- Flatten layer
- Dense layers (64 and 128 units)
- Dropout layer (0.2)
- Output Dense layer with softmax activation

### 4. **Model Compilation**
- Optimizer: Adam
- Loss: Sparse Categorical Crossentropy
- Metrics: Accuracy

### 5. **Model Training**
- `model.fit()` is used to train on the training dataset
- Validation data is monitored during training

=

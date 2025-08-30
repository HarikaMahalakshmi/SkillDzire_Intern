# 🎧 Audio Feature Extraction Project

This project processes a collection of `.wav` audio files to extract meaningful audio features (MFCC, Chroma, Spectral Contrast), and saves them as a machine learning-ready dataset (`.csv`).

---

## 🎯 Objective

To automatically extract acoustic features from audio files for use in machine learning tasks like:

- Speech emotion recognition
- Speaker identification
- Genre or instrument classification
- Environmental sound detection

---


---

## 📚 Libraries Used

- `librosa` – audio analysis and feature extraction
- `numpy` – numerical operations
- `pandas` – data handling and CSV export
- `os` – directory traversal
- `matplotlib` (optional) – waveform/spectrogram visualization
- `scikit-learn` – feature scaling (optional)

---

## 🔄 How It Works

### 1. **Feature Extraction**

For each audio file, the script computes:

| Feature Type        | Description                                  | Shape |
|---------------------|----------------------------------------------|-------|
| **MFCC (13)**       | Mel-Frequency Cepstral Coefficients           | 13    |
| **Chroma (12)**     | Energy distribution across 12 pitch classes  | 12    |
| **Spectral Contrast (7)** | Peak-valley differences in frequency bands | 7     |

Each feature is **mean-aggregated over time** and combined into a **32-dimensional feature vector**.

---

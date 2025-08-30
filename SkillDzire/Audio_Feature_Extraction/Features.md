# Featues
## 🎧 1. **MFCC (Mel Frequency Cepstral Coefficients)**

### 🧠 What it is:

MFCCs represent the **short-term power spectrum of sound**, based on how humans perceive pitch.

### 🎯 Purpose:

They capture **phonetic information**, making them ideal for **speech and speaker recognition**.

### 🗣️ Example:

Imagine saying "hello." MFCC extracts how the pitch and intensity change over each short time segment. This is like fingerprinting the spoken word.

### 🔍 Visualization:

MFCCs are usually displayed as a 2D spectrogram — time vs. coefficient values (like a heatmap).

---

## 🔄 2. **ZCR (Zero Crossing Rate)**

### 🧠 What it is:

The rate at which the audio signal changes **sign (positive to negative)** in a given frame.

### 🎯 Purpose:

Useful to detect **noisy or percussive sounds**, and **speech detection**.

### 🗣️ Example:

* A **sine wave** has a regular ZCR.
* A **snare drum hit** or **fricative consonant** like “s” has high ZCR due to rapid changes in the waveform.

```python
zcr = librosa.feature.zero_crossing_rate(y)[0]
```

---

## 📏 3. **RMSE (Root Mean Square Energy)**

### 🧠 What it is:

It measures the **loudness (energy)** of the signal in each frame.

### 🎯 Purpose:

To detect **onsets, silences**, and changes in **intensity**.

### 🗣️ Example:

* When the person **starts talking**, RMSE increases.
* During silence, RMSE is near zero.

```python
rmse = librosa.feature.rms(y=y)[0]
```

---

## 🎯 4. **Spectral Centroid**

### 🧠 What it is:

The **“center of mass”** of the audio spectrum — tells us where the **brightness** of the sound is.

### 🎯 Purpose:

Helps distinguish **bright vs. dull sounds**.

### 🗣️ Example:

* A **violin** playing high notes → High spectral centroid (more energy in high frequencies).
* A **bass drum** → Low spectral centroid (energy in low frequencies).

```python
centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
```

---

## ⚡ 5. **Spectral Contrast**

### 🧠 What it is:

Difference between **high and low energy** in different frequency bands.

### 🎯 Purpose:

Helps distinguish **instruments** and **harmonic content**, especially in music.

### 🗣️ Example:

* A sound with both strong bass and high treble will have **high spectral contrast**.
* Flat white noise will have **low contrast**.

```python
contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
```

---

## 🎼 6. **Chroma Features**

### 🧠 What it is:

Represents the **12 pitch classes** (C, C#, D, ..., B) regardless of octave.

### 🎯 Purpose:

Useful for **musical feature extraction**, like key detection or chord recognition.

### 🎹 Example:

* A **C major chord** will activate C, E, and G chroma bins.
* Good for melody/harmony detection in music.

```python
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
```

---

## 🔚 Summary Table

| Feature               | Captures                        | Useful For                     |
| --------------------- | ------------------------------- | ------------------------------ |
| **MFCC**              | Phonetics / timbre              | Speech, speaker recognition    |
| **ZCR**               | Signal fluctuation rate         | Speech onset, noise detection  |
| **RMSE**              | Loudness                        | Voice activity, silence        |
| **Spectral Centroid** | Brightness of sound             | Timbre, instrument detection   |
| **Spectral Contrast** | Peak/valley frequency variation | Music genre, instrument type   |
| **Chroma**            | Pitch class                     | Musical key, harmony detection |



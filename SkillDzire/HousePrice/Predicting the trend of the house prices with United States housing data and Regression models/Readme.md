# 🏠 House Price Prediction using XGBoost and Streamlit

This project uses machine learning to predict housing prices based on various features such as location, area, quality, and other property characteristics. It includes a user-friendly Streamlit web application that allows users to input property features and get a real-time predicted price.

---

## 📌 Features Used

Some of the most important features used for prediction:
- `LotArea`: Lot size in square feet
- `OverallQual`, `OverallCond`: Overall material and finish quality & condition
- `YearBuilt`: Construction year
- `GrLivArea`: Above-ground living area
- `GarageArea`: Size of garage
- Categorical features like:
  - `MSZoning`
  - `Neighborhood`
  - `Street`
  - One-hot encoded fields for quality, condition, and more

---

## 💡 Technologies Used

- 🐍 **Python 3.9+**
- 📦 **Pandas** and **NumPy** for data processing
- 🎯 **Scikit-learn** for preprocessing and evaluation
- 🧠 **XGBoost** for regression modeling
- 💾 **Joblib** for model serialization
- 🌐 **Streamlit** for interactive web UI

---

## ⚙️ Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction

### step2: Install dependencies
pip install requirements.txt

### Running the streamlit app
streamlit run app.py


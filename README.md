# 🌱 Crop & Fertilizer Prediction App (Flask)

A lightweight Flask web application for predicting the best crop and fertilizer based on soil and environmental parameters. This app leverages machine learning models to aid farmers and agricultural enthusiasts with intelligent recommendations.

---

## 🚀 Features

- 🧠 **Crop Prediction** based on N, P, K, temperature, and humidity
- 💊 **Fertilizer Recommendation** based on soil type, crop type, and nutrient levels
- 🧪 Integrated with pre-trained ML models and scalers
- 🌿 Informational pages on organic farming and fertilizers
- 📊 Modular code structure with future support for MongoDB

---

## 🛠 Tech Stack

- ⚙️ **Flask** – Python web framework
- 📈 **Scikit-learn** – For loading and using ML models
- 🧪 **Pickle** – Model serialization
- 📊 **Pandas / NumPy** – Data manipulation
- 🎨 **HTML/CSS** – UI templates (via `render_template`)

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Crop-Fertilizer-Predictor.git
cd Crop-Fertilizer-Predictor
```
### 2. Create a virtual enviroment 
```bash
python -m venv venv
source venv/bin/activate
```
### 3. Install requirements and run the app.
```bash
pip install -r requirements.txt
python app.py
```

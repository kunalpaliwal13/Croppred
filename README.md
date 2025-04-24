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

### Screenshots

![image](https://github.com/user-attachments/assets/edf2a49d-47dc-47a6-8641-3d25c4874c7f)
<br><br>
![image](https://github.com/user-attachments/assets/3fa497bd-b54f-4408-8e69-daff3e7e2871)
<br><br>
![image](https://github.com/user-attachments/assets/15d05eca-e89a-4d03-b233-0aa3df1416ca)
<br><br>
![image](https://github.com/user-attachments/assets/e07b2307-2922-4801-b7e9-919dcd727b79)
<br>

# Prediction: 
## Crop Prediction

We trained **two separate models**:

1. **Crop‑recommender** – suggests the best crop for given soil & weather conditions.  
2. **Fertilizer‑recommender** – suggests the optimal fertilizer for the chosen crop.

### Feature set

<br>

<img src="https://github.com/user-attachments/assets/34ece2e0-5f72-4f7f-ba42-b7981f6acd93" height="200" />

---

### Feature Selection<br> 
<img src="https://github.com/user-attachments/assets/f0e35752-65d8-40e7-9c81-24a2601d34b7" height="350" /><br>
As we can see that ph and rainfall are least affecting our prediction, we dropped them


### Model benchmarking

<br>

<img src="https://github.com/user-attachments/assets/74401410-d4f3-4a34-81ba-718454c222f0" height="350" />

We evaluated several algorithms; **XGBoost** achieved the highest accuracy, so we exported it as a `.pkl` file for deployment.

<br>

<img src="https://github.com/user-attachments/assets/90f192c6-b189-4a17-91d2-5ca132194ef7" height="350" />

---

## Fertilizer Recommendation

### Feature set

<br>

<img src="https://github.com/user-attachments/assets/97807905-4cf4-4323-b61a-527368b581c1" height="200" />

---

### Model benchmarking

<br>

<img src="https://github.com/user-attachments/assets/b302d47b-5031-4843-ac6d-2779d287a561" height="150" />

Among the tested models, **Linear Regression** delivered the best performance, so we adopted it for fertilizer prediction.









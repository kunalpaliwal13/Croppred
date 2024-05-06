from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import pandas as pd
import plotly.express as px
import plotly.io as pio
from sklearn.preprocessing import StandardScaler
# import pymongo
# from googletrans import Translator


app = Flask(__name__)


def load_model(modelfile):
    loaded_model = pickle.load(open(modelfile, 'rb'))
    return loaded_model

@app.route('/contact_us', methods=['GET'])
def contact_us():
    return render_template('contact_us.html')


@app.route('/fertilizer_elements')
def fertilizer_elements():
    return render_template('fertilizer.html')

def create_collection_mongo():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client['kunal']
    collection = db['crop recommendation']
    return collection

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/beginner_tools')
def beginner_tools():
    return render_template('beginner_tools.html')

@app.route('/predict_another', methods=['POST', 'GET'])
def predict_another():
    try:
        loaded_model = load_model('fertilizer_model.pkl')
        

        features = [float(request.form.get(f)) for f in ['soil_type', 'crop_type', 'nitrogen', 'potassium', 'phosphorous']]
        # moisture = 40.5
        # features.append(moisture)
        df = pd.DataFrame([features])
        df.columns = ["Soil Type", "Crop Type", "Nitrogen", "Potassium", "Phosphorus"]
        features = np.array(features).reshape(1, -1)
        scaler = pickle.load(open('fertilizer_scaler.pkl', 'rb'))
        scaled_features = scaler.transform(features)
        prediction = loaded_model.predict(scaled_features)
        prediction = str(prediction)
        
        

        result = prediction[2:-2] + " is the predicted fertilizer"
    except Exception as e:
        result = ""
    return render_template('fertilizerpred.html', another_result=result)


@app.route('/organic_methods', methods=['GET'])
def organic_methods():
    return render_template('organic_methods.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    try:
        # collection = create_collection_mongo()
        loaded_model = load_model('model.pkl')

        scaler = pickle.load(open('scaler.pkl', 'rb'))

        features = [float(request.form.get(f)) for f in ['N', 'P', 'K', 'temp', 'humidity']]
        feature_keys = ['N', 'P', 'K', 'temp', 'humidity']
        feature_values = [float(request.form.get(f)) for f in feature_keys]
        features_dict = dict(zip(feature_keys, feature_values))
        #collection.insert_one(features_dict)

        features = np.array(features).reshape(1, -1)

        scaled_features = scaler.transform(features)

        result = loaded_model.predict(scaled_features)
        class_mapping = {'apple': 0, 'banana': 1, 'blackgram': 2, 'chickpea': 3, 'coconut': 4, 'coffee': 5, 'cotton': 6, 'grapes': 7, 'jute': 8, 'kidneybeans': 9, 'lentil': 10, 'maize': 11, 'mango': 12, 'mothbeans': 13, 'mungbean': 14, 'muskmelon': 15, 'orange': 16, 'papaya': 17, 'pigeonpeas': 18, 'pomegranate': 19, 'rice': 20, 'watermelon': 21}
        predicted_crop = [crop for crop, label in class_mapping.items() if label == result[0]][0]

        result = f"{predicted_crop} is the predicted crop"
    except Exception as e:
        result = e

    return render_template("croppredict.html", result=result)

@app.route('/know-more')
def know_more():
    # df = pd.read_csv("file.csv")
    # correlation_matrix = df.corr()
    # fig = px.imshow(correlation_matrix, labels=dict(color="Correlation"),
    #                 x=correlation_matrix.columns, y=correlation_matrix.columns,
    #                 color_continuous_scale='Mint')
    


    # plot_html = pio.to_html(fig, full_html=False)
    return render_template('know_more.html')
if __name__ == '__main__':
    app.run(debug=True)

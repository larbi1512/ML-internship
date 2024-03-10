import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import MinMaxScaler, LabelEncoder


# Create flask app
app = Flask(__name__)

# Load the model
model = joblib.load('best_model.pkl')
Data=pd.read_csv('first inten project.csv')

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route("/predict", methods=["POST"])
def predict():
    features = request.form.to_dict()
    
    # Preprocess the user-submitted data
    column = ['Num_Adults', 'Num_Week_Nights', 'Meal_Type', 'Car_Parking_Space', 
              'Room_Type', 'Lead_Time', 'Market_Segment_Type', 'Repeated', 'AVG_Price', 'Special_Requests']
    
    # Convert form data to a DataFrame
    features_processed = pd.DataFrame(columns=column)
    features_processed.loc[0] = [features.get(col, 0) for col in column]  # Ensure all columns are present
    
    # Encode categorical data
    labelencoder = LabelEncoder()
    features_processed['Meal_Type'] = labelencoder.fit_transform(features_processed['Meal_Type'])
    features_processed['Room_Type'] = labelencoder.fit_transform(features_processed['Room_Type'])
    features_processed['Market_Segment_Type'] = labelencoder.fit_transform(features_processed['Market_Segment_Type'])
    
    # Convert data types to numeric
    features_processed = features_processed.astype(float)
    
    # Normalize data
    scaler = MinMaxScaler()
    features_scaled = scaler.fit_transform(features_processed)
    
    # Make prediction
    prediction = model.predict(features_scaled)
    
    # Map prediction to corresponding label
    prediction_label = 'not cancelled' if prediction[0] == 1 else 'cancelled'
    
    return render_template('index.html', prediction_text='Predicted Booking status: {}'.format(prediction_label))


if __name__ == '__main__':
    app.run(debug=True)

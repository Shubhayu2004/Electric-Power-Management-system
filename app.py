from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('page10.html')

@app.route('/predict', methods=['POST'])
def predict():
    house_number = int(request.form['house_number'])
    date = pd.to_datetime(request.form['date'], dayfirst=True)


    prediction = model.predict(n_periods=1)  

    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)

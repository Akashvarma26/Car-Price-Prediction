from flask import Flask, request, render_template
import pickle

app = Flask(__name__) 
model = pickle.load(open('model.pkl', 'rb')) 

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        Present_Price = float(request.form['price'])
        Kms_Driven = int(request.form['kms_driven'])
        Fuel_Type = request.form['fuel'].lower()
        Seller_Type = request.form['seller'].lower()
        Transmission = request.form['transmission'].lower()
        no_of_year=int(request.form['year'])
        if Fuel_Type=="petrol":
            Fuel_Type=2
        elif Fuel_Type=="diesel":
            Fuel_Type=1
        elif Fuel_Type=="cng":
            Fuel_Type=0
        if Seller_Type=="dealer":
            Seller_Type=1
        elif Seller_Type=="individual":
            Seller_Type=0
        if Transmission=="manual":
            Transmission=1
        elif Transmission=="automatic":
            Transmission=0
        prediction = model.predict([[Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission,no_of_year]])
        output = round(prediction[0], 2)
        return render_template('index.html', output="The Predicted price of the car is rs {} Lakhs".format(output))

#if __name__ == '__main__':
 #   app.run(debug=True)

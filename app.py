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
        Fuel_Type = request.form['fuel']
        Seller_Type = request.form['seller']
        Transmission = request.form['transmission']
        no_of_year=request.form['year']
        prediction = model.predict([[Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission,no_of_year]])
        output = round(prediction[0], 2)
        return render_template('index.html', output="The Predicted price of the car is rs {} Lakhs".format(output))


if __name__ == '__main__':
    app.run(debug=True)
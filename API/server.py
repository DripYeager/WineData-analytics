from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Load the saved model
        print('Loading model...')
        model = pickle.load(open('wine_variety_predict.pickle', 'rb'))
        
        # Get the input values from the form
        country = float(request.form['country'])
        price = float(request.form['price'])
        province = float(request.form['province'])
        winery = float(request.form['winery'])
        print('Input data:', country, price, province, winery)

        # Make a prediction using the loaded model
        variety = model.predict([[country, price, province, winery]])[0]
        print('Prediction:', variety)

        # Render the prediction on the results page
        return render_template('results.html', variety=variety)

    # Render the form on the home page
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

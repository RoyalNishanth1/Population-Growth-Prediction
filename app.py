import joblib
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load the model
model = joblib.load('population_growth_model.pkl')

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['loggedin'] = True
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    prediction = None
    selected_country = None
    
    if request.method == 'POST':
        country = request.form['country']
        start_year = int(request.form['start_year'])
        end_year = int(request.form['end_year'])
        
        years_to_predict = list(range(start_year, end_year + 1))
        prediction = predict_growth(country, years_to_predict)
        
        selected_country = country
        
        # Plotting the graph
        plot_growth(country, years_to_predict, prediction)
        
        # Redirect to the plot page
        return redirect(url_for('plot'))
    
    return render_template('index.html', prediction=prediction, selected_country=selected_country)

@app.route('/plot')
def plot():
    # Render the plot.html page
    return render_template('plot.html')

def predict_growth(country, years):
    # Placeholder function to simulate prediction
    # Replace with your actual prediction logic
    predictions = []
    for year in years:
        # Example: predict growth rate using a model
        # Replace with actual model prediction
        prediction = np.random.uniform(1.0, 5.0)  # Random prediction for demonstration
        predictions.append(prediction)
    return predictions

def plot_growth(country, years, predictions):
    # Plotting function
    plt.figure(figsize=(10, 6))
    plt.plot(years, predictions, marker='o', linestyle='-', color='b')
    plt.title(f'Population Growth Rate Prediction for {country}')
    plt.xlabel('Year')
    plt.ylabel('Growth Rate')
    plt.grid(True)
    plt.savefig('static/plot.png')  # Save the plot as a PNG file in the static folder
    plt.close()

if __name__ == '__main__':
    app.run(debug=True)

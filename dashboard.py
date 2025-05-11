from flask import Flask, render_template
import requests

app = Flask(__name__)

# Replace 'your_api_key' with your actual FRED API key
API_KEY = '15913e7143c787b4df957818b7e22c04'

def get_unemployment_rate():
    series_id = 'UNRATE'  # Unemployment Rate series ID
    url = f'https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={API_KEY}&file_type=json'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Get the latest observation
        latest_observation = data['observations'][-1]
        return latest_observation['value'], latest_observation['date']  # Return value and date
    else:
        return None, None  # Return None if there's an error

def get_inflation_rate():
    url = 'http://api.worldbank.org/v2/country/US/indicator/FP.CPI.TOTL?format=json'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Get the latest observation
        latest_observation = data[1][-1]
        return latest_observation['value'], latest_observation['date']  # Return value and date
    else:
        return None, None  # Return None if there's an error

@app.route('/dashboard')
def dashboard():
    unemployment_rate, unemployment_date = get_unemployment_rate()
    inflation_rate, inflation_date = get_inflation_rate()
    return render_template('dashboard.html', 
                           unemployment_rate=unemployment_rate, 
                           unemployment_date=unemployment_date,
                           inflation_rate=inflation_rate,
                           inflation_date=inflation_date)

if __name__ == '__main__':
    app.run(debug=True)

from datetime import datetime
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = 'your_api'  # Replace with your actual API key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind': data['wind']['speed'],
                'sunrise': datetime.utcfromtimestamp(data['sys']['sunrise']).strftime('%H:%M'),
                'sunset': datetime.utcfromtimestamp(data['sys']['sunset']).strftime('%H:%M'), 
                'icon': data['weather'][0]['icon']
            }
        else:
            weather = {'error': 'Failed to retrieve weather data'}
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)

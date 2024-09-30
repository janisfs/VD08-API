from flask import Flask, render_template, request
import requests

# Пример использования библиотеки requests для запроса к API
response = requests.get('https://api.openweathermap.org/...', timeout=10)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
    return render_template('index.html', weather=weather, news=news)

def get_weather(city):
    api_key = "d9a0f4c37c536dec3b20825900c97115"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = "6f487be6bb4c495491a7f19adc0475dd"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get('articles', [])

if __name__ == '__main__':
    app.run(debug=True)


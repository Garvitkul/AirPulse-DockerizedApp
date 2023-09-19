import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

def get_air_quality(city):
    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': 'Your API Key'})
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        return data
    else:
        return Exception("Error: {} {}".format(response.status_code, response.text))

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        air_quality = get_air_quality(city)
        return render_template('results.html', result=air_quality, city=city)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')

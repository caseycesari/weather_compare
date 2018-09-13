from pprint import pprint as pp

from flask import Flask, render_template, request

from weather import get_local_time, query_api

app = Flask(__name__)


@app.route('/')
@app.route('/', methods=['POST'])
def index():
    data = []
    error = None
    if request.method == 'POST':
        city1 = request.form.get('city1')
        city2 = request.form.get('city2')
        for c in (city1, city2):
            resp = query_api(c)
            pp(resp)
            if resp:
                data.append(resp)
        if len(data) != 2:
            error = 'Did not get complete response from Weather API'
    return render_template("weather.html",
                           data=data,
                           error=error,
                           time=get_local_time)


@app.route('/api', methods=['GET'])
def api():
    data = []
    error = None
    if request.method == 'GET':
        city1 = request.args.get('city1')
        city2 = request.args.get('city2')
        city3 = request.args.get('city3')
        for c in (city1, city2, city3):
            resp = query_api(c)
            pp(resp)
            if resp:
                data.append(resp)
        if len(data) != 3:
            error = 'Did not get complete response from Weather API'
  
    return f"It is currently {data[0]['main']['temp']:.0f}°F in {data[0]['name']}, {data[1]['main']['temp']:.0f}°F in {data[1]['name']}, and {data[2]['main']['temp']:.0f}°F in {data[2]['name']}."


if __name__ == "__main__":
    app.run()

# import flask
from flask import Flask, Response, request, url_for, redirect

# initiate Flask
app = Flask(__name__)

weather_dict = {'leicester': 'Raining', 'nottingham': 'Sunny', 'peterborough': 'Snow'}


@app.route('/weather/<city>')
def location(city):
    url = url_for('weather', city=city)
    bbc_weather = url_for('ext')
    return """
    <html>
    <head>
    <title>Search a city</title>
    </head>
    <body>
    <h1>The weather in {} is....</h1>
    <p><a href={}>click here</a></p>
    <h2>Or..search the BBC site <a href = {}>here</a></h2>
    </body>
    </html> 
    """.format(city, url, bbc_weather)


@app.route('/weather/report/<city>')
def weather(city):
    define = weather_dict.get(city)
    return """
    <html>
    <head>
    <title>Weather report</title>
    </head>
    <body>
    <h1>The weather in {} is {}</h1>
    </body>
    </html> 
    """.format(city, define)


@app.route('/weather/external')
def ext():
    return redirect('https://www.bbc.co.uk/weather')


# fire up the Flask app
if __name__ == '__main__':
    app.run(debug=True)
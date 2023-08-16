# import flask
from flask import Flask, Response, request, url_for, redirect

# initiate Flask
app = Flask(__name__)

words = {'apple': 'a green fruit', 'banana': 'a yellow fruit', 'strawberry': 'a red fruit'}


@app.route('/dict/search/<word>')
def search_word(word):
    url = url_for('return_definition', word=word)
    return '''
    <html>
    <head>
    <title>Search a word</title>
    </head>
    <body>
    <h1>You search the meaning of the word {}</h1>
    <p>Click <a href={}>here</a> to find your definition</p>
    </body>
    </head>
    '''.format(word, url)


@app.route('/dict/definition/<word>')
def return_definition(word):
    define = words.get(word)
    return '''
     <html>
    <head>
    <title>Definition</title>
    </head>
    <body>
    <h1>{}</h1>
    <p>{}</p>
    </body>
    </head>
    '''.format(word, define)


# fire up the Flask app
if __name__ == '__main__':
    app.run(debug=True)
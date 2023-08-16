# import flask
from flask import Flask, Response, request, url_for, redirect

# initiate Flask
app = Flask(__name__)








# fire up the Flask app
if __name__ == '__main__':
    app.run(debug=True)
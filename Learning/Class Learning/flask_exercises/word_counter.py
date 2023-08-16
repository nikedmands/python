# import flask
from flask import Flask, Response, request, url_for, redirect
from collections import Counter

# initiate Flask
app = Flask(__name__)


@app.route('/word_count/<sentence>')
def count_words(sentence):
    words = sentence.split()
    count = {}
    for x in words:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    counter = "\n".join("{0} {1}".format(k, v) for k, v in count.items())
    return counter


# fire up the Flask app
if __name__ == '__main__':
    app.run(debug=True)
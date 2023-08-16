# import flask
from flask import Flask, Response, request, url_for, redirect

# initiate Flask
app = Flask(__name__)

ToDo = []


# add new job
@app.route('/list/add/<job>')
def add_job(job):
    ToDo.append(job)
    return ToDo


# delete a job
@app.route('/list/remove/<job>')
def remove_job(job):
    ToDo.remove(job)
    return ToDo


# edit a job
@app.route('/list/edit/<job>/<new_job>')
def edit_job(job, new_job):
    x = ToDo.index(job)
    ToDo[x] = new_job
    return ToDo


# fire up the Flask app
if __name__ == '__main__':
    app.run(debug=True)
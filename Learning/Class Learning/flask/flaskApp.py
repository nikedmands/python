# import flask
from flask import Flask, Response, request, url_for, redirect

# initiate Flask
app = Flask(__name__)


# set up a route and bind a function as it's response
# / = index
@app.route('/')
def hello_from_flask():
    return "Hello from Flask!"


@app.route('/get/text')
def get_text():
    return Response("Hello from Flask using an explicit Response object", mimetype="text/plain")


# POST method in this route
@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response("You posted this data to the Flask app: " + data_sent, mimetype='text/plain')


# dynamic routes, route variable word is a string
@app.route('/dynamic/<word>')
def home(word):
    return word


# dynamic routes, use int as variable
@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    line = str(number) + ' squared = ' + str(squared)
    return line


# ADDITION
@app.route('/addNumbers/<int:num1>/<int:num2>')
def add(num1, num2):
    addition = num1 + num2
    line = str(num1) + ' + ' + str(num2) + ' = ' + str(addition)
    return line


# SUBTRACTION
@app.route('/subNumbers/<int:num1>/<int:num2>')
def sub(num1, num2):
    subtraction = num1 - num2
    line = str(num1) + ' - ' + str(num2) + ' = ' + str(subtraction)
    return line


# MULTIPLY
@app.route('/timesNumbers/<int:num1>/<int:num2>')
def times(num1, num2):
    multiply = num1 * num2
    line = str(num1) + ' x ' + str(num2) + ' = ' + str(multiply)
    return line


# DIVIDE
@app.route('/divNumbers/<int:num1>/<int:num2>')
def div(num1, num2):
    divide = num1 / num2
    line = str(num1) + ' / ' + str(num2) + ' = ' + str(divide)
    return line


fruits = []


# change a list with app.route - add
@app.route('/fruits/add/<fruit>')
def add_fruit(fruit):
    fruits.append(fruit)
    return fruits


# change a list with app.route - remove
@app.route('/fruits/remove/<fruit>')
def remove_fruit(fruit):
    fruits.remove(fruit)
    return fruits


# show the fruits list
@app.route('/fruits')
def show_fruits():
    return fruits


# url_for (import url_for at the top)(user logs in, link to their profile page)
@app.route('/login/<username>')
def login(username):
    url = url_for('view_profile', username=username)

    return """
    <html>
    <head>
    <title>Profile Page for {}</title>
    </head>
    <body>
    
    <h1>Welcome {}</h1>
    <p>You have successfully logged in!</p>
    <p>Click below to access your profile</p>
    <a href="{}">Access Profile</a>
    </body>
    
    </html>
    """.format(username, username, url)


# link to user profile page from above
@app.route('/home/userprofile/<username>')
def view_profile(username):
    return """
    <html>
    <head>
    <title>Welcome to your profile {}!</title>
    </head>
    <body>
    
    <h1>{}'s Profile!</h1>
    <p>Welcome to your profile page</p>
    
    </body>
    </html>
""".format(username, username)


# redirect page (import redirect at the top)
@app.route('/home/external')
def external():
    return redirect("https://www.sky.com")


# URLS
@app.route('/home/<name>')
def say_hello(name):
    return """
    
    <html>
    <head>
    
    <title>Sample-Flask Routes</title>
    </head>
    <body>
    
    <h1>Name page</h1>
    <p>Hello {}</p>
    
    </body>
    </html>
    """.format(name)


# sample HTML page
@app.route('/sample/<name>/<int:age>')
def sample(name, age):
    return """
    
    <html>
    <head>
    
    <title>SAMPLE PAGE</title>
    </head>
    <body style="background-color: #153243;">
    
    <h1 style="font-family: sans-serif; text-align: center; color: #EEF0EB">SAMPLE HTML PAGE</h1>
    <h2 style="font-family: sans-serif; color: #B4B8AB; text-align: center">Page displayed when endpoint is accessed</h2>
    <p style="font-family: sans-serif; text-align: center; color: #EEF0EB">Welcome to the page {}<br>You are {} years old!</p>
    
    </body>
    </html>
    """.format(name, age)


# OPERATOR
@app.route('/calculator/<int:num1>/<operator>/<int:num2>')
def calc(num1, operator, num2):
    if operator == 'times':
        return str(num1) + ' x ' + str(num2) + ' = ' + str(num1 * num2)
    elif operator == 'divide':
        return str(num1) + ' / ' + str(num2) + ' = ' + str(num1 / num2)
    elif operator == 'add':
        return str(num1) + ' + ' + str(num2) + ' = ' + str(num1 + num2)
    elif operator == 'minus':
        return str(num1) + ' - ' + str(num2) + ' = ' + str(num1 - num2)
    else:
        return 'ERROR 404'


# fire up the Flask app
if __name__ == '__main__':
    app.run(debug=True)
#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#DELIVERABLE 1
#Your index() view should be routed to at the base URL with /. 
#It should Contain an h1 element that contains the title of this application, 
#"Python Operations with Flask Routing and Views".
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

#DELIVERABLE 2
#A print_string view should take one parameter, a string. 
#It should print the string in the console and display it in the web browser. 
#Its URL should be of the format /print/parameter.
@app.route('/print/<string:route>')
def print_string(route):
    #print in console
    print(route)
    #print in browser
    return route

#DELIVERABLE 3
#A count() view should take one parameter, an integer. 
#It should display all numbers in the range of that parameter on separate lines. 
#Its URL should be of the format /count/parameter.
@app.route('/count/<int:number>')
def count(number):
    #what does f'' mean?
    count = f''
    for n in range(number):
        count += f'{n}\n'
    return count

#DELIVERABLE 4
#A math() view should take three parameters: 
#num1, operation, and num2. 
#It must perform the appropriate operation on the two numbers in the order that they are presented. 
#The included operations should be: +, -, *, div (/ would change the URL path), and %. 
#Its URL should be of the format /math/<num1>/<operation>/<num2>.
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
#The result of 10 % 5 is 0.
#The % operator in Python is the modulus operator, 
#which calculates the remainder of the division between two numbers. 
#In this case, 10 is divided by 5, and since 10 is divisible evenly by 5, 
#there is no remainder, resulting in a value of 0.


if __name__ == '__main__':
    app.run(port=5555, debug=True)

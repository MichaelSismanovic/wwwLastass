from flask import Flask, jsonify, render_template, request, make_response
import random, re, os, pickle

def create_math_problem():
    val1 = random.randint(0, 9)
    val2 = random.randint(0, 9)
    if random.randint(1,3) == 1:
        return f"{val1}*{val2}", val1 * val2
    elif random.randint(1,2) == 1:
        return f"{val1}+{val2}", val1 + val2
    else:
        return f"{val1}-{val2}", val1 - val2

def create_app():
    # create and configure the app
    app = Flask(__name__)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route('/foobar')
    def foobar():
        return '<h1>Hi there, foobar!</h1>'

    @app.route('/contact')
    def contact():
        captcha, solution = create_math_problem()
        t = render_template('contact.html', captcha=captcha, solution=solution)
        res = make_response(t)

        return res

    @app.route('/send-contact', methods=['POST'])
    def post_contact():
        json = request.get_json()

        if json['firstname'] == '' and json['lastname'] == '' and json['text'] == '':
            return 'name and text cannot be empty'

        if re.match(r'^\d{4,14}$', json['phone']) is None:
            return 'this is not a phonenumber'

        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', json['email']) is None:
            return 'this is not an email'

        if re.match(r'^\d{4,14}$', json['phone']) is None:
            return 'this is not a phonenumber'

        if json['captcha'] != json['solution']:
            return 'Learn math!'

        return 'Thanks for participating'

    return app

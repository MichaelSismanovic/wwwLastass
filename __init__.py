from flask import Flask, jsonify, render_template, request, make_response
from flask_wtf.csrf import CSRFProtect
import random, re, os, pickle

def make_captcha():
    val1 = random.randint(0, 2**32)
    val2 = random.randint(0, 2**32)
    if random.randint(1,3) == 1:
        return f"{val1}+{val2}", val1 + val2
    elif random.randint(1,2) == 1:
        return f"{val1}-{val2}", val1 - val2
    else:
        return f"{val1}*{val2}", val1 * val2

counts_file = "/home/david/flaskapp/counts.pkl"
if not os.path.exists(counts_file):
    counts = {}
else:
    with open(counts_file, 'rb') as f:
        counts = pickle.load(f)

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'extremely secret unguessable key'
    csrf = CSRFProtect(app)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route('/foobar')
    def foobar():
        return '<h1>Hi there, foobar!</h1>'

    @app.route('/albums')
    def albums():
        albums = { "albums": [ { "name": "Album 1", "year": 42069, } ]}
        return jsonify(albums)

    @app.route('/flashcards')
    def flashcards():
        return render_template('index.html')

    @app.route('/contact')
    def contact():
        if 'uid' in request.cookies:
            counts[request.cookies['uid']] += 1
        count = counts.get(request.cookies.get('uid', ''), 1)
        captcha, solution = make_captcha()

        t = render_template('contact.html', captcha=captcha, solution=solution, count=count)
        res = make_response(t)

        if 'uid' not in request.cookies:
            uid = f'{random.randint(0,2**32):010d}'
            counts[uid] = 1
            res.set_cookie('uid', uid)

        with open(counts_file, 'wb') as f:
            pickle.dump(counts, f)

        return res

    @app.route('/send-contact', methods=['POST'])
    def post_contact():
        json = request.get_json()

        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', json['email']) is None:
            return f'error: malformed email {json["email"]}'

        if re.match(r'^\d{4,14}$', json['phone']) is None:
            return f'error: malformed phone {json["phone"]}'

        if json['name'] == '' and json['text'] == '':
            return f'error: name and text cannot be empty'

        if json['captcha'] != json['solution']:
            return f'error: wrong captcha'

        return 'success'

    return app


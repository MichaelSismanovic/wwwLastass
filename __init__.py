from flask import Flask, request, render_template, redirect, url_for
import random

def create_app():
    app= Flask(__name__)
    #configure app

    @app.route('/hello')
    def hello():
        return render_template('kontakt.html')
    
    @app.route('/kontakt', methods=['GET', 'POST'])
    def kontakt():
        operators = ['+', '-', '*', '/']
        cal_value_1 = random.randint(0, 9)
        cal_value_2 = random.randint(0, 9)
        cal_op = random.choice(operators)

        result = 0
        
        if random_operator == '+':
            result = value1 + value2
        elif random_operator == '-':
            result = value1 - value2
        elif random_operator == '*':
            result = value1 * value2
        elif random_operator == '/':
            result = value1 / value2

        if request.method == 'POST':
            vorname = request.form.get('vorname')
            nachname = request.form.get('nachname')
            telefonnummer = request.form.get('telefonnummer')
            email = request.form.get('email')
            nachricht = request.form.get('nachricht')
            if(vorname == ""):
                return render_template('kontakt.html', value="fuuuck")
            
            return vorname
        
        return render_template('kontakt.html')


    return app

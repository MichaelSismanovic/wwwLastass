from flask import Flask, request, render_template, redirect, url_for
import random, re

def create_app():
    app= Flask(__name__)
    #configure app

    @app.route('/hello')
    def hello():
        return "hello"
    
    @app.route('/kontakt', methods=['GET', 'POST'])
    def kontakt():

        if request.method == 'POST':
            if(True):
                return "fuuuck"
            data = request.form.to_dict()
            vorname = data.get('vorname')
            nachname = data.get('nachname')
            telefonnummer = data.get('telefonnummer')
            email = data.get('email')
            nachricht = data.get('nachricht')
            res = data.get('rechenaufgabe')

            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            match = re.match(pattern, email)

            if (vorname == "" or nachname == "" or telefonnummer == "" or email == "" or nachricht == ""):
                return render_template('kontakt.html', value="please fill out every field")

            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            match = re.match(pattern, email)

            if(not match):
                return render_template('kontakt.html', value="invalid email")

            pattern = r'^\+43\d{1,4}\d{1,4}\d{1,4}$'
            match = re.match(pattern, telefonnummer)

            if(not match):
                return render_template('kontakt.html', value="invalid phonenumber")

            
            return render_template('kontakt.html', value="Danke für die Nachricht, wir melden uns bald!")

        
        operators = ['+', '-', '*']
        cal_value_1 = random.randint(0, 9)
        cal_value_2 = random.randint(0, 9)
        cal_op = random.choice(operators)
        
        return render_template('kontakt.html', cal_value_1=cal_value_1, cal_value_2=cal_value_2, cal_op=cal_op)


    return app

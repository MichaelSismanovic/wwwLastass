from flask import Flask, request, render_template, redirect, url_for

def create_app():
    app= Flask(__name__)
    #configure app

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    @app.route('/kontakt', methods=['GET', 'POST'])
    def kontakt():
        if request.method == 'POST':
            vorname = request.form.get('vorname')
            nachname = request.form.get('nachname')
            telefonnummer = request.form.get('telefonnummer')
            email = request.form.get('email')
            nachricht = request.form.get('nachricht')
            return "hoooray it works"
        
        return render_template('kontakt.html')


    return app

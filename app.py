from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    print(request.form['name'])
    print(request.form['email'])
    print(request.form['message'])
    return render_template('home.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/voice')
def voice():
    return render_template('voice.html')


@app.route('/theatre')
def theatre():
    return render_template('theatre.html')

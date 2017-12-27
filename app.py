from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config.from_object('config')
app.config.from_envvar
app.config['MAIL_SERVER'] = str(os.environ['FLASK_MAIL_SERVER'])
app.config['MAIL_PORT'] = int(os.environ['FLASK_MAIL_PORT'])
app.config['MAIL_USERNAME'] = str(os.environ['FLASK_MAIL_USERNAME'])
app.config['MAIL_PASSWORD'] = str(os.environ['FLASK_MAIL_PASSWORD'])
app.config['MAIL_USE_TLS'] = str(os.environ['FLASK_MAIL_USE_TLS']) == 'True'
app.config['MAIL_USE_SSL'] = str(os.environ['FLASK_MAIL_USE_SSL']) == 'True'
mail = Mail(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/send_email', methods=['POST'])
def send_email():
    email_title = "Message from " + request.form['name'] + ' (' \
        + request.form['email'] + ')'
    msg = Message(email_title,
                  sender=app.config['MAIL_USERNAME'],
                  recipients=['mr.scott.mcallister@gmail.com'])
    email_body = str(request.form['message'])
    msg.body = email_body
    mail.send(msg)
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

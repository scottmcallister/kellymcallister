# kellymcallister

A portfolio [website](https://kellymcallister.ca) for my wife. It's basically just serving static content, but I decided to use Flask for it just in case I want to build out additional features.

## Installation

To get the project up and running, you'll need Python 3 and virtualenv installed. Clone the repository and set up a virtual environment.

```
$ git clone https://github.com/scottmcallister/kellymcallister.git
$ virtualenv -p python3 env
```

Once you have a virutal environment ready, activate your virtual environment and install the project dependencies.

```
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```

In order to run the app you'll need the following environment variables added to your path:

* `FLASK_MAIL_SERVER` - smtp client address
* `FLASK_MAIL_PORT` - smtp client port
* `FLASK_MAIL_USERNAME` - smtp client username
* `FLASK_MAIL_PASSWORD` - smtp client password
* `RECAPTCHA_KEY` - API key for Google recaptcha
* `RECAPTCHA_SECRET` - API secret for Google recaptcha
* `FLASK_APP` - main script (app.py)

If everyting goes smoothly you should be able to start the app with `flask run`

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Python 3](https://www.python.org/download/releases/3.0/) - Python version
from flask import Flask

from flask_ask import Ask, statement, convert_errors

import logging

app = Flask(__name__)

ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('HelloWorldIntent')
def hello_world():
    speech_text = 'Hello world'
    return statement(speech_text)

#@app.route("/")
#def hello():
#    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


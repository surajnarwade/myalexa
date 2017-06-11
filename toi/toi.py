from flask import Flask
from flask_ask import Ask, statement, convert_errors
import logging
import requests
import json 

app = Flask(__name__)

ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


#Start times of india
@ask.launch
def launch():
    return statement("Welcome to Times of India news, I will tell you Top 10 latest news")




@ask.intent('NewsIntent')
def get_news():
    url = "https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=latest&apiKey=<API-KEY>"
    response = requests.request("GET", url)
    res = json.loads(response.text)
    nth = {
     1: "first",
     2: "second",
     3: "third",
     4: "fourth",
     5: "fifth",
     6: "sixth",
     7: "seventh",
     8:  "eigth",
     9:  "ninth",
     10: "tenth"
     }
    w = [] 
    for i in res['articles']:
        p =  nth[res['articles'].index(i)+1] + " news is  " + i['title'][:-14] + "   " + i['description']
        w.append(p)
    p = '..     '.join(w)
    return statement(p)


@ask.intent("AMAZON.StopIntent")
def stop():
    return statement("Bye, have a nice day")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

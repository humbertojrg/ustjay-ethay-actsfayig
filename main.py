import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

post_url  = "http://hidden-journey-62459.herokuapp.com/piglatinize/"
base_url = "http://hidden-journey-62459.herokuapp.com/"


def get_fact():
    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText().strip()


def get_pig_latin_response(text):
    request = requests.post(post_url,
                            data = {'input_text':text},
                            allow_redirects=False)
    
    return request

def extract_url(response):
    url = response.headers['location']
     
    return url


def get_pig_latin_url(text):
    response = get_pig_latin_response(text)
    url = extract_url(response)
    
    return url
    


@app.route('/')
def home():
    random_fact = get_fact()
    url = get_pig_latin_url(random_fact)
    return url


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)


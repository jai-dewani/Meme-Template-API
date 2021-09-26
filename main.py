import json 
from flask import Flask 
app = Flask(__name__)

data = json.load(open('meme.json'))

# memes = data['list']

@app.route("/")
def index():
    return "Check /all at the moment"

@app.route("/all")
def meme():
    return data
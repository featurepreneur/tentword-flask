import random
from flask import Flask, render_template, request
import json

import tentword

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def get_value():

    word_dict = tentword.get_word()

    #print(list_random)
    return render_template('results.html', word_dict = word_dict)

if __name__=='__main__':
    
    app.debug = True
    app.run()
    app.run(debug=True)
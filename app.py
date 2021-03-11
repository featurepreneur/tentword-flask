import random
from flask import Flask, render_template, request
import json

app = Flask(__name__)

names       = [] # Capacity Number List
name_list   = [] # initializing The 1st List
list_random = [] # initializing The 2nd List

@app.route('/')
def home():

    return render_template('results.html')

@app.route('/', methods = ["POST"])
def get_value():

    names    = request.values.get("names")

    use_random              = False

    if(not names):
        use_random = True
    else:
        name_list       = names.split()
        item_count      = len(name_list)
    
    data = None

    with open('./list.json') as f:
        data = json.load(f)

    if(use_random):
        name_list               = data["items"]
        item_count              = data["item_count"]
    else:
        
        data["items"]           = name_list
        data["item_count"]      = len(name_list)
        json_object             = json.dumps(data)
        
        with open('./list.json', 'w') as outfile: 
            outfile.write(json_object)

    list_random              = random.sample(name_list, item_count)

    #print(list_random)
    return render_template('results.html', randomName = list_random[0], num = item_count)

if __name__=='__main__':
    
    app.debug = True
    app.run()
    app.run(debug=True)
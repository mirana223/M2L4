from flask import Flask
import random

app = Flask(__name__)
facts_list = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "Bananas are berries, but strawberries aren't.",
        "A day on Venus is longer than a year on Venus. It takes about 243 Earth days to rotate once, but only about 225 Earth days to orbit the Sun.",
        "Octopuses have three hearts and blue blood.",
        "Wombat poop is cube-shaped, which helps prevent it from rolling away and marks their territory effectively."
    ]
female_first_namelist = ["Alice", "Charlie", "Diana", "Eve",
                         "karen","nancy","susan","linda","barbara"]
male_first_namelist = ["John", "Michael", "David", "James", "Robert",
                       "William", "Joseph", "Charles", "Thomas", "Christopher"]
last_namelist = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin",
                  "yılmaz", "demir", "şahin", "çelik", "kara", "ak", "güneş", "yıldız", "deniz", "kaya"]
@app.route("/")
def hello_world():
    return '''
    <html>
    <head>
        <title>say hello to trisolaris</title>
                <style>
                body {
                    background-color: lightblue;
                    color: black;
                    font-family: Arial, sans-serif;
                    text-align: center;}
                h1 {
                    color: blue;
                    font-size: 36px;
                    text-align: center;}

            </style> 
    <body>
          
        <h1>Hello, I am 7/24 middle age worker.</h1>
        <h1>there is your treat</h1>
        <a href ="random_facts">Click for random facts</a>
        <p>
        <a href ="trisolaris">Click for say hello to trisolaris</a>
        </p>
        <a href ="_names">Click for random names</a>
                  
    </body>        
    </html>              
                                          '''

@app.route("/trisolaris")
def hello():
    return """<h1>hello trisolaris</h1>"""
@app.route("/random_facts")
def random_facts2():
    return f"""<p>{random.choice(facts_list)}</p>"""
@app.route("/_names")
def fate():
    return f"""
    <html>
    <head>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <h1> female names: {random.choice(female_first_namelist)} {random.choice(last_namelist)}</h1>
        <h1> male names: {random.choice(male_first_namelist)} {random.choice(last_namelist)}</h1>
    </body>
    </html>
    """


app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''<h1>Hello, I am 7/24 middle age worker.</h1>
                <h1>there is your treat</h1>
                <a href ="random_facts">Click for random facts</a>
                <p>
                <a href ="emir">Click for say hello to trisolaris</a>
                </p>
                        '''

@app.route("/emir")
def hello():
    return '<h1>hello trisolaris</h1>'
@app.route("/random_facts")
def random_facts2():
    import random
    facts_list = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "Bananas are berries, but strawberries aren't.",
        "A day on Venus is longer than a year on Venus. It takes about 243 Earth days to rotate once, but only about 225 Earth days to orbit the Sun.",
        "Octopuses have three hearts and blue blood.",
        "Wombat poop is cube-shaped, which helps prevent it from rolling away and marks their territory effectively."
    ]
    return f'<p>{random.choice(facts_list)}</p>'


app.run(debug=True)

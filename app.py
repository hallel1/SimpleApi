import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hallel Python Princess</h1>"


@app.route('/alert', methods=['GET'])
def create_alert():

    return "nothing but alert"


app.run()

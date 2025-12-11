from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
def load():
    with open("data.txt", "a+") as f:
        f.seek(0)
        content = f.read()
        if content == "":
            f.seek(0)
            f.write("0")
            return 0
    try:
        return int(content)
    except ValueError:
        return 0

def save(x):
    with open("data.txt", "a+") as f:
        f.seek(0)
        f.truncate()
        f.write(str(x))

@app.route("/get")
def get():
    return {"counter": load()}
@app.route("/set", methods=["POST"])
def set_():
    x = load()+1
    save(x)
    return {"counter": x}
@app.route("/reset", methods=["POST"])
def reset():
    save(0)

    return {"counter": 0}

@app.route("/")
def home():
    return """
    <html>
    <h1>This is a counter app, this is the home</h1>
    </html>
    """


from flask import Flask
app = Flask(__name__)
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
    except TypeError:
        return 0

def save(x):
    with open("data.txt", "a+") as f:
        f.seek(0)
        f.truncate()
        f.write(str(x))

@app.route("/get")
def get():
    return {"counter": load()}
@app.route("/set")
def set_():
    x = load()+1
    save(x)
    return {"counter": x}
@app.route("/reset")
def reset():
    save(0)
    return {"counter": 0}
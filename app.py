from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello"
@app.route("/<name>")
def ryan(name):
    return "Hello " + name
if __name__ == "__main__":
    app.run(debug=True)



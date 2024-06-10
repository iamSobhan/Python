from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the Home Page!</h1>"


@app.route("/welcome/sonu")
def welcome_sonu():
    return "<h1>Welcome to our Webpage Sonu...</h1>"


@app.route("/welcome/apu")
def welcome_apu():
    return "<h1>Welcome to our Webpage Apu...</h1>"


@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Welcome to our Webpage {name.title()}"


if __name__ == "__main__":
    app.run(debug=True)

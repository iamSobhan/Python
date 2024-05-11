from flask import Flask

#WSGI Application
app = Flask(__name__)

@app.route("/")

def flower():
    return "This is a Sunflower. This is a very beautiful flower."

@app.route("/fruits")

def fruits():
    return "Mango is a very delicious fruit."


if __name__ == "__main__":
    app.run(debug=True)
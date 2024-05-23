from ctypes.wintypes import HHOOK
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index3.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        fname = request.form["fname"]
        lname = request.form["lname"]
        mail = request.form["mail"]
        ph = request.form["ph"]
        return redirect(url_for("user", fname=fname, lname=lname, mail=mail, ph=ph))
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    fname = request.args.get("fname")
    lname = request.args.get("lname")
    mail = request.args.get("mail")
    ph = request.args.get("ph")
    return f"<h1>First Name: {fname}</h1><h1>Last Name: {lname}</h1><h1>Email: {mail}</h1><h1>Phone Number: {ph}</h1>"

	
if __name__ == "__main__":
	app.run(debug=True)

from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "tecoma"
app.permanent_session_lifetime = timedelta(days=7)


@app.route("/")
def home():
    return render_template("index3.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["fname"] = request.form["fname"]
        session["lname"] = request.form["lname"]
        session["mail"] = request.form["mail"]
        session["ph"] = request.form["ph"]
        return redirect(url_for("user"))
    else:
        return render_template("login.html")
    

@app.route("/user")
def user():
    if "fname" in session and "lname" in session and "mail" in session and "ph" in session:
        fname = session["fname"]
        lname = session["lname"]
        mail = session["mail"]
        ph = session["ph"]
        return f"<h1>First Name: {fname}, Last Name: {lname}, Email: {mail}, Phone: {ph}</h1>"
        
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)
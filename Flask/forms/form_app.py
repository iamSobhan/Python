#importing the dependencies
from flask import Flask, render_template, redirect, url_for, flash


from forms import SignupForm, LoginForm


#creating the flask app
app = Flask(__name__)

app.config["SECRET_KEY"] = "flask_form_practice"


#home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title = "Home")


#signup page
@app.route("/signup", methods = ["GET", "POST"])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        flash(f"You have Successfully Signup {form.username.data}...")
        return redirect(url_for("home"))
        
    return render_template("signup.html", title = "Signup", form = form)




#login page
@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    email = form.email.data
    pwd = form.password.data   

    if form.validate_on_submit():
        if email == "sobhan@gmail.com" and pwd == "12345":
            flash(f"You have Successfully Logged in...")
            return redirect(url_for("home"))
        else:
            flash("Incorrect email or password!")

    return render_template("login.html", title = "Login", form = form)


#starting the app
if __name__ == "__main__":
    app.run(debug = True)


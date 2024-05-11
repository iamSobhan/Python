#Building Url Dynamically 
#Variable Rules And URL Building

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def fruits():
    return "Fuits are really good for health."

@app.route("/success/<int:score>")
def success(score):
    return "He is Passed and his score is "+ str(score)

@app.route("/failed/<int:score>")
def failed(score):
    return "He is Failed and his score is "+ str(score)


@app.route("/results/<int:marks>")
def results(marks):
    result = ""
    if marks<35:
        result = "failed"
    else:
        result = "success"
    return redirect(url_for(result, score=marks))



if __name__ == "__main__":
    app.run(debug=True)

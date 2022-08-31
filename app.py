from flask import Flask, render_template, request

from marks import marks_prediction
import marks as m

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/", methods= ["POST"])
def submit():
    #HTML to python
    if request.method == "POST":
        hrs = request.form["hrs"]
        marks_pred = m.marks_prediction(hrs)
        print(marks_pred)
    #python to html
    return render_template("sub.html", n = marks_pred)


if __name__ == "__main__":
    app.run(debug=True)
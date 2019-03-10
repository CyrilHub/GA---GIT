import requests
from flask import Flask, render_template, request

app = Flask(__name__)
#Sets the root page. Pages after at http://localhost:5000/ect
@app.route("/")
def home():
    user = input('Please enter your name:')

    return render_template("index.html", name = user)


if __name__ == "__main__":
    app.run(debug=True)
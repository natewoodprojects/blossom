
import os
from flask import Flask, render_template

app = Flask(__name__)


app.secret_key = os.environ["SECRET_KEY"]


@app.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.env = "development" 
    app.run(debug=True)

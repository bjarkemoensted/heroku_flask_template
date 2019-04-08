
from flask import Flask, render_template, url_for, request, session, redirect

app = Flask(__name__)

app.secret_key = "hunter2"

@app.route('/', methods=['GET', 'POST'])
def index():
    msg = "Hello world!"
    if request.method == "POST":
        msg += "\nGot data:\n"
        msg += request.get_json()

    return msg


if __name__ == '__main__':
    app.run(debug=True)
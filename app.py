
from flask import Flask, render_template, url_for, request, session, redirect

app = Flask(__name__)

with open("secret.txt") as f:
    app.secret_key = max(f.readlines(), key=len).strip()

@app.route('/', methods=['GET'])
def index():
    msg = "Hello world!"
    if request.method == "POST":
        msg += "\nGot data:\n"
        msg += request.get_json()

    return msg


if __name__ == '__main__':
    app.run(debug=True)
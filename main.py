from random import randint
from flask import Flask, make_response, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    secret_number = request.cookies.get("secret_number")
    response = make_response(render_template("index.html"))
    if not secret_number:
        secret_number = randint(1, 30)
        response.set_cookie("secret_number", str(secret_number))

    return response

@app.route("/calculate", methods=["POST"])
def calculate():
    guess = int(request.form.get("guess"))
    secret_number = int(request.cookies.get("secret_number"))

    if guess == secret_number:
        msg = "You got it!"
        response = make_response(render_template("result.html", message=msg))
        response.set_cookie("secret_number", str(randint(1, 30)))
        return response
    elif guess > secret_number:
        msg = "Your guess is too big"
        return render_template("result.html", message=msg)
    elif guess < secret_number:
        msg = "Your guess is too small"
        return render_template("result.html", message=msg)

if __name__ == '__main__':
    app.run()
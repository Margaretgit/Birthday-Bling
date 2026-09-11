from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create", methods=["POST"])
def create_card():

    name = request.form["name"]
    age = request.form["age"]
    relationship = request.form["relationship"]
    style = request.form["style"]
    message = request.form["message"]

    return render_template(
        "card.html",
        name=name,
        age=age,
        relationship=relationship,
        style=style,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)
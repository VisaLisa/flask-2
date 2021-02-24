from flask import Flask, render_template, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route("/api/get-lucky-num", methods=['POST'])
def lucky_num():
    """Define JSON body with name,email,year,color"""
    name = request.json["name"]
    email = request.json["email"]
    year = request.json["year"]
    color = request.json["color"]

    req = {
        "name": name,
        "email": email,
        "year": year,
        "color": color
    }


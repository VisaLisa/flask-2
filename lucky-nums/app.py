from flask import Flask, render_template, jsonify, make_response, render_template, request
from helpers import validate_request, get_num_facts
import random

app = Flask(__name__)


@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route("/api/get-lucky-num", methods=['POST'])
def lucky_num():
    """POST route to process form data and send json response"""

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

    try:
        validation = validate_request(req)

        num = random.randint(1,100)
        data = get_num_facts(num, year)
        return make_response(data, 200)
    except ValidationError as e:
        return make_response(e.errors, 422)
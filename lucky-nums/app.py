from flask import Flask, render_template, request, jsonify
from random import randint 
from forms import UserForm

app = Flask(__name__)
BASE_API_URL = 'http://numbersapi.com'

@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")

@app.route('/api/get-lucky-num', methods=["POST"])
def get_lucky_num():
    """ Creates user from form and returns JSON """

    formdata = request.get_json() #get JSON data
    form = UserForm.from_json(formdata=formdata)

    if form.validate():
        random_number = randint(1,100)
        number = requests.get(f'{BASE_API_URL}/{random_number}')
        year = requests.get(f'{BASE_API_URL}/{form.year.data}')

        return jsonify ({
            "number": {
                "fact": f"{number.text}",
                "num": number
            },
            "year": {
                "fact": f"{year.text}",
                "year": year
            }
        }),200
    return jsonify(form.errors)
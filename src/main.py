from flask import Flask, request, jsonify
from get_predicted_ratings import get_predicted_ratings
from formatters.input_formatter import input_formatter
from formatters.output_formatter import output_formatter

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ratings/predict", methods=["POST"])
def predict_ratings():
    if request.method == "POST":
        #request_data = request.get_json().get('data', "No data found")
        data = input_formatter(request.data)
        data = get_predicted_ratings(data)
        return output_formatter(data)


if __name__ == "__main__":
    app.run(port=1337, host='0.0.0.0', debug=True)
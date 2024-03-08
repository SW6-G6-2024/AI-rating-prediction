from flask import Flask, request
from model import get_predicted_ratings

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ratings/predict", methods=["POST"])
def predict_ratings():
    if request.method == "POST":
        request_data = request.get_json().get('data', "No data found")
        # use the output of the trained AI model to predict the ratings
        return get_predicted_ratings(request_data)


if __name__ == "__main__":
    app.run(port=1337, host='0.0.0.0', debug=True)
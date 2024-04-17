from flask import Flask, request
from get_predicted_ratings import get_predicted_ratings
from formatters.input_formatter import input_formatter
from formatters.output_formatter import output_formatter
from xgboost import XGBClassifier

app = Flask(__name__)

# load the model
xgb_model = XGBClassifier()
xgb_model.load_model('src/saved_models/xgb_model.json')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/ratings/predict", methods=["POST"])
def predict_ratings():
    if request.method == "POST":
        # get the data from the request
        data = input_formatter(request.data)
        rating_list = []
        # loop through the data, get the predicted ratings and append to the list
        for i in data:
            rating_list.append({
                'piste': i['piste'],
                'rating': get_predicted_ratings(i, xgb_model)
            })
        return output_formatter(rating_list)


if __name__ == "__main__":
    app.run(port=1337, host='0.0.0.0', debug=True)

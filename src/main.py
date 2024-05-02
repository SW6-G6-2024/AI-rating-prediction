from flask import Flask, request
import joblib
from get_predicted_ratings import get_predicted_ratings
from formatters.input_formatter import input_formatter
from formatters.output_formatter import output_formatter
from xgboost import XGBClassifier, XGBRegressor
import pandas as pd

app = Flask(__name__)

# load the model
xgb_model = XGBRegressor()
# xgb_model = XGBClassifier()
xgb_model.load_model('src/saved_models/xgb_model_reg.json')


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/ratings/predict", methods=["POST"])
def predict_ratings():
    if request.method == "POST":
        # Get the data from the request
        data = input_formatter(request.data)
        # load scaler
        #scaler = joblib.load('src/saved_scaler/scaler.pkl')
        # Scale the input features
        #scaled_data = scaler.transform(data)
        # Predict ratings for all input data at once
        ratings = get_predicted_ratings(data, xgb_model)
        # Assemble the rating list with corresponding piste id

        # Create a DataFrame with piste ID and corresponding ratings
        rating_df = pd.DataFrame({'piste': data['piste'], 'rating': ratings})
        
        # Convert the DataFrame to a list of dictionaries
        rating_list = rating_df.to_dict(orient='records')
        return output_formatter(rating_list)


if __name__ == "__main__":
    app.run(port=1337, host='0.0.0.0', debug=True)

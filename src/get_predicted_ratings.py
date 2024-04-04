import pandas as pd
from xgboost import XGBClassifier


def get_predicted_ratings(data):
    # load the model
    xgb_model = XGBClassifier()
    xgb_model.load_model('src/saved_models/xgb_model.json')

    # Convert input data to DataFrame
    df = pd.DataFrame([data])

    # Reorder the columns
    # ADD PISTE AS A COLUMN BETWEEN HOUR AND TEMPERATURE WHEN IMPLEMENTED
    df = df[['year', 'month', 'day', 'hour', 'temperature', 'weatherCode',
             'windSpeed', 'windDirection', 'snowfall', 'snowDepth', 'downpour', 'visibility']]

    # Display the DataFrame
    # print(df)

    prediction = xgb_model.predict(df)

    # make predictions
    return prediction.item()

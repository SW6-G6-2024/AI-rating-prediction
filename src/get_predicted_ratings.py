import pandas as pd
from xgboost import XGBClassifier


def get_predicted_ratings(data: dict, model: XGBClassifier):
    """
    Get the predicted ratings for the input data, using XGBoost Classifier.

    Args:
        data (dict): An instance of the input data, as a dictionary.
        e.g. {
            'id': 1,
            'direction': 1,
            'year': 2020,
            'month': 1,
            'day': 1,
            'hour': 1,
            'piste': '1',
            'temperature': 0,
            'weatherCode': 0,
            'windSpeed': 0,
            'windDirection': 0,
            'snowfall': 0,
            'snowDepth': 0,
            'rain': 0,
            'visibility': 0
        }
        model (XGBClassifier): The saved XGBoost Classifier model to use for prediction.

    Returns:
        int: The predicted rating for the input data.
    """

    # Convert input data to DataFrame
    df = pd.DataFrame([data])

    # Reorder the columns
    df = df[['piste', 'direction', 'year', 'month', 'day', 'hour', 'temperature', 'weatherCode',
             'windSpeed', 'windDirection', 'snowfall', 'snowDepth', 'rain', 'visibility']]

    # Display the DataFrame
    # print(df)

    prediction = model.predict(df)

    # make predictions
    return prediction.item()

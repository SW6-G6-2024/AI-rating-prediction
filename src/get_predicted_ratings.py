import pandas as pd


def get_predicted_ratings(data: dict, model):
    """
    Get the predicted ratings for the input data, using XGBoost Classifier.
    
    model (XGBRegressor): The saved XGBoost regressor model to use for prediction.

    Returns:
        int: The predicteds rating for the input data.
    """

    # Ensure the columns are in the correct order
    df = data[['piste', 'direction', 'year', 'month', 'day', 'hour', 'temperature', 'weatherCode',
             'windSpeed', 'windDirection', 'snowfall', 'snowDepth', 'rain', 'visibility']]

    # Make predictions
    predictions = model.predict(df)

    # if predictions are less than 0, set them to 0
    predictions[predictions < 0] = 0

    return predictions

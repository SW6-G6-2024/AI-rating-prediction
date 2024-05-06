import json
import pandas as pd
from validators.validate_input import validate_input_data

required_fields = [
    'pisteList',
    'weather',
    'date'
]
required_piste_info = [
    'id',
    'direction'
]
weather_fields = [
    'temperature',
    'weatherCode',
    'windSpeed',
    'windDirection',
    'snowfall',
    'snowDepth',
    'rain',
    'visibility'
]
date_fields = {
    'year',
    'month',
    'day',
    'hour'
}


def input_formatter(data: str) -> pd.DataFrame:
    """
    Creates a pandas DataFrame from the input data, in order to match the expected input format for the model.

    Args:
        data (json): The input data in json format.

    Returns:
        pd.DataFrame: A DataFrame containing the input data for each piste.
    """

    # load json data
    load = json.loads(data)

    # get required fields
    piste_ids = load.get('pisteList')
    weather = load.get('weather')
    date = load.get('date')

    # get weather fields
    weather_data = {
        'temperature': float(weather.get('temperature')),
        'weatherCode': int(weather.get('weatherCode')),
        'windSpeed': float(weather.get('windSpeed')),
        'windDirection': int(weather.get('windDirection')),
        'snowfall': int(weather.get('snowfall')),
        'snowDepth': float(weather.get('snowDepth')),
        'rain': int(weather.get('rain')),
        'visibility': float(weather.get('visibility'))
    }

    # get date fields
    date_data = {
        'year': int(date.get('year')),
        'month': int(date.get('month')),
        'day': int(date.get('day')),
        'hour': int(date.get('hour'))
    }

    # loop through each id and create dictionary
    formatted_data = []
    for piste_id in piste_ids:
        piste_data = {
            'piste': int(piste_id.get('id')),
            'direction': float(piste_id.get('direction'))
        }
        piste_data.update(weather_data)
        piste_data.update(date_data)
        formatted_data.append(piste_data)

    # validate piste data
    validate_input_data(load, required_fields)
    # validate piste id data
    for piste_id in piste_ids:
        validate_input_data(piste_id, required_piste_info)
    # validate weather data
    validate_input_data(weather, weather_fields)
    # validate date data
    validate_input_data(date, date_fields)

    # Set column names explicitly
    column_names = ['piste', 'direction'] + list(weather_data.keys()) + list(date_data.keys())
    
    return pd.DataFrame(formatted_data, columns=column_names)

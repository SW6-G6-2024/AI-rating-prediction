import json
from validators.validate_input import validate_input_data

def input_formatter(data: str) -> list[dict]:
    """
    Creates a list of dictionaries from the input data, in order to match the expected input format for the model.

    Args:
        data (json): The input data in json format.

    Returns:
        list: A list of dictionaries, each containing the input data for a single piste.
    """
    # Required fields
    required_fields = {
        'pisteList': list,
        'weather': dict, 
        'year': int, 
        'month': int, 
        'day': int, 
        'hour': int
    }
    weather_fields = {
        'temperature': float, 
        'weatherCode': int, 
        'windSpeed': float, 
        'windDirection': int, 
        'snowfall': int, 
        'snowDepth': float, 
        'rain': int, 
        'visibility': float
    }

    # load json data
    load = json.loads(data)
    validate_input_data(load, required_fields)

    # get required fields
    piste_ids = load.get('pisteList')
    weather = load.get('weather')
    year = load.get('year')
    month = load.get('month')
    day = load.get('day')
    hour = load.get('hour')

    # get weather fields
    temperature = weather.get('temperature')
    weatherCode = weather.get('weatherCode')
    windSpeed = weather.get('windSpeed')
    windDirection = weather.get('windDirection')
    snowfall = weather.get('snowfall')
    snowDepth = weather.get('snowDepth')
    rain = weather.get('rain')
    visibility = weather.get('visibility')

    # validate weather data
    validate_input_data(weather, weather_fields)

    # loop through each id and create dictionary
    formatted_data = []
    for piste_id in piste_ids:
        formatted_data.append({
            'piste': piste_id.get('id'),
            'direction': piste_id.get('direction'),
            'temperature': temperature,
            'weatherCode': weatherCode,
            'windSpeed': windSpeed,
            'windDirection': windDirection,
            'snowfall': snowfall,
            'snowDepth': snowDepth,
            'rain': rain,
            'visibility': visibility,
            'year': year,
            'month': month,
            'day': day,
            'hour': hour
        })

    return formatted_data
import json
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


def input_formatter(data: str) -> list[dict]:
    """
    Creates a list of dictionaries from the input data, in order to match the expected input format for the model.

    Args:
        data (json): The input data in json format.

    Returns:
        list: A list of dictionaries, each containing the input data for a single piste.
    """

    # load json data
    load = json.loads(data)

    # get required fields
    piste_ids = load.get('pisteList')
    weather = load.get('weather')
    date = load.get('date')

    # get weather fields
    temperature = weather.get('temperature')
    weatherCode = weather.get('weatherCode')
    windSpeed = weather.get('windSpeed')
    windDirection = weather.get('windDirection')
    snowfall = weather.get('snowfall')
    snowDepth = weather.get('snowDepth')
    rain = weather.get('rain')
    visibility = weather.get('visibility')

    # get date fields
    year = date.get('year')
    month = date.get('month')
    day = date.get('day')
    hour = date.get('hour')

    # loop through each id and create dictionary
    formatted_data = []
    for piste_id in piste_ids:
        formatted_data.append({
            'piste': int(piste_id.get('id')),
            'direction': float(piste_id.get('direction')),
            'temperature': float(temperature),
            'weatherCode': int(weatherCode),
            'windSpeed': float(windSpeed),
            'windDirection': int(windDirection),
            'snowfall': int(snowfall),
            'snowDepth': float(snowDepth),
            'rain': int(rain),
            'visibility': float(visibility),
            'year': int(year),
            'month': int(month),
            'day': int(day),
            'hour': int(hour)
        })

    # validate piste data
    validate_input_data(load, required_fields)
    # validate piste id data
    for piste_id in piste_ids:
        validate_input_data(piste_id, required_piste_info)
    # validate weather data
    validate_input_data(weather, weather_fields)
    # validate date data
    validate_input_data(date, date_fields)

    return formatted_data

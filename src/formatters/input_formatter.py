import json

def input_formatter(data):
    load = json.loads(data)
    # get list of piste ids or throw error if not found
    piste_ids = load.get('pisteList', None)
    weather = load.get('weather', None)
    year = load.get('year', None)
    month = load.get('month', None)
    day = load.get('day', None)
    hour = load.get('hour', None)
    
    # check for errors in input data
    if piste_ids is None and weather is None:
        raise ValueError("No pisteList or weather found in input data")
    if piste_ids == []:
        raise ValueError("pisteList is empty")
    if year is None:
        raise ValueError("No year found in input data")
    if month is None:
        raise ValueError("No month found in input data")
    if day is None:
        raise ValueError("No day found in input data")
    if hour is None:
        raise ValueError("No hour found in input data")

    # loop through each id and create dictionary
    formatted_data = []
    for piste_id in piste_ids:
        formatted_data.append({
            'piste_id': piste_id,
            'weather': weather
        })

    return
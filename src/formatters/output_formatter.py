from flask import jsonify

def output_formatter(data: list[dict]):
    """
    Formats the output data to be returned as a json response.
    
    Args:
        data (dict): The data to be formatted.

    Returns:
        json: The formatted data.
    """
    return jsonify(data)
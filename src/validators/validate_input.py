def validate_input_data(data: dict, required_fields: list[str]):
    """
    Validates the input data.

    Args:
        data (dict): The input data to validate.
        required_fields (list): A list of required fields.

    Raises:
        ValueError: If the input data is invalid.
    """

    for field in required_fields:
        value = data.get(field)
        if value is None:
            raise ValueError(f"Missing required field: {field}")


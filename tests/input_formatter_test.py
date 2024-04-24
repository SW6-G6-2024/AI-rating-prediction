import pytest
from json.decoder import JSONDecodeError
from tests.fixtures.input.input_formatter import fail, fail1, succ

succ_path = '../tests/fixtures/input/input_succ.json'
required_fields = {
    'year': int,
    'month': int,
    'day': int,
    'hour': int,
}

def test_validate_input_data_does_not_throw():
    from src.formatters.input_formatter import validate_input_data
    data = {
        'year': 2021,
        'month': 5,
        'day': 5,
        'hour': 5
    }
    with pytest.raises(Exception, match=""):
        assert(validate_input_data(data, required_fields))


def test_validate_input_data_throws_missing_field():
    from src.formatters.input_formatter import validate_input_data
    data = {
        'year': 2021,
        'month': 5,
        'day': 5
    }
    with pytest.raises(ValueError, match="Missing required field: hour"):
        assert(validate_input_data(data, required_fields))
    

def test_input_formatter_success():
    from src.formatters.input_formatter import input_formatter
    formatted_data = input_formatter(succ())
    # Check that the data is formatted as a list
    assert isinstance(formatted_data, list)
    # Check that the data is formatted as a list of dictionaries with the correct value types
    assert isinstance(formatted_data[0], dict)
    assert isinstance(formatted_data[0]['temperature'], float)
    assert isinstance(formatted_data[0]['weatherCode'], int)
    assert isinstance(formatted_data[0]['windSpeed'], float)
    assert isinstance(formatted_data[0]['windDirection'], int)
    assert isinstance(formatted_data[0]['snowfall'], int)
    assert isinstance(formatted_data[0]['snowDepth'], float)
    assert isinstance(formatted_data[0]['rain'], int)
    assert isinstance(formatted_data[0]['visibility'], float)
    assert isinstance(formatted_data[0]['year'], int)
    assert isinstance(formatted_data[0]['month'], int)
    assert isinstance(formatted_data[0]['day'], int)
    assert isinstance(formatted_data[0]['hour'], int)
    # check for the second instance, to see if it works for multiple instances
    assert isinstance(formatted_data[1], dict)
    assert isinstance(formatted_data[1]['temperature'], float)
    assert isinstance(formatted_data[1]['weatherCode'], int)
    assert isinstance(formatted_data[1]['windSpeed'], float)
    assert isinstance(formatted_data[1]['windDirection'], int)
    assert isinstance(formatted_data[1]['snowfall'], int)
    assert isinstance(formatted_data[1]['snowDepth'], float)
    assert isinstance(formatted_data[1]['rain'], int)
    assert isinstance(formatted_data[1]['visibility'], float)
    assert isinstance(formatted_data[1]['year'], int)
    assert isinstance(formatted_data[1]['month'], int)
    assert isinstance(formatted_data[1]['day'], int)
    assert isinstance(formatted_data[1]['hour'], int)
    

def test_input_formatter_no_file():
    with pytest.raises(JSONDecodeError) as err:
        from src.formatters.input_formatter import input_formatter
        input_formatter("foo")
        assert str(err.value) == "Expecting value: line 1 column 1 (char 0)"


def test_input_formatter_missing_field():
    with pytest.raises(ValueError) as err:
        from src.formatters.input_formatter import input_formatter
        input_formatter(fail1())
        assert str(err.value) == "ValueError: Missing required field: hour"
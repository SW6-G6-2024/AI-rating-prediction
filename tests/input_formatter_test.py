import pytest
from json.decoder import JSONDecodeError
import pandas as pd

from tests.fixtures.input.input_fixtures import succ, fail1

required_fields = {
    'year': int,
    'month': int,
    'day': int,
    'hour': int,
}

def test_validate_input_data_does_not_throw():
    from formatters.input_formatter import validate_input_data
    data = {
        'year': 2021,
        'month': 5,
        'day': 5,
        'hour': 5
    }
    with pytest.raises(Exception, match=""):
        assert(validate_input_data(data, required_fields))


def test_validate_input_data_throws_missing_field():
    from formatters.input_formatter import validate_input_data
    data = {
        'year': 2021,
        'month': 5,
        'day': 5
    }
    with pytest.raises(ValueError, match="Missing required field: hour"):
        assert(validate_input_data(data, required_fields))
    

def test_input_formatter_success():
    from formatters.input_formatter import input_formatter
    formatted_data = input_formatter(succ())
    # Check that the data is formatted as a DataFrame
    assert isinstance(formatted_data, pd.DataFrame)
    # Check the column names to ensure all features are present
    expected_columns = ['piste', 'direction', 'temperature', 'weatherCode', 'windSpeed', 'windDirection',
                        'snowfall', 'snowDepth', 'rain', 'visibility', 'year', 'month', 'day', 'hour']
    assert list(formatted_data.columns) == expected_columns
    # Check the data types of the DataFrame columns
    assert formatted_data['temperature'].dtype == float
    assert formatted_data['weatherCode'].dtype == 'int64'
    assert formatted_data['windSpeed'].dtype == float
    assert formatted_data['windDirection'].dtype == 'int64'
    assert formatted_data['snowfall'].dtype == 'int64'
    assert formatted_data['snowDepth'].dtype == float
    assert formatted_data['rain'].dtype == 'int64'
    assert formatted_data['visibility'].dtype == float
    assert formatted_data['year'].dtype == 'int64'
    assert formatted_data['month'].dtype == 'int64'
    assert formatted_data['day'].dtype == 'int64'
    assert formatted_data['hour'].dtype == 'int64'
    

def test_input_formatter_no_file():
    with pytest.raises(JSONDecodeError) as err:
        from formatters.input_formatter import input_formatter
        input_formatter("foo")
        assert str(err.value) == "Expecting value: line 1 column 1 (char 0)"


def test_input_formatter_missing_field():
    with pytest.raises(ValueError) as err:
        from formatters.input_formatter import input_formatter
        input_formatter(fail1())
        assert str(err.value) == "ValueError: Missing required field: hour"
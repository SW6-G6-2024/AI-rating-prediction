import pytest
from src.training.data_processing import load_data
from src.training.data_processing import flatten

fake_path = 'tests/fixtures/test_data2.json'
data_path = 'tests/fixtures/test_data.json'


def test_load_data(monkeypatch):
    # Define the dummy data to be returned by the mock function
    dummy_data = [{}] * 1000

    # Define the mock function
    def mock_load_data(path):
        return dummy_data

    # Patch the load_data function with the mock function
    monkeypatch.setattr("src.training.data_processing.load_data", mock_load_data)

    # Call the function that uses load_data
    data = load_data(data_path)

    # Check the behavior of the function
    assert len(data) == 1000  # Check that data is loaded
    assert isinstance(data, list)  # Check that data is a list
    assert isinstance(data[0], dict)  # Check that data contains dictionaries


def test_load_data_no_file():
    from src.training.data_processing import load_data
    with pytest.raises(FileNotFoundError) as err:
        load_data(fake_path)
    # Check that the file is not found
    assert str(
        err.value) == "[Errno 2] No such file or directory: " + "'" + fake_path + "'"


def test_flatten():
    data = [
        [{"points": 1, "text": "This is a test"}, {
            "points": 1, "text": "This is a test"}],
        [{"points": 2, "text": "This is a test"}, {
            "points": 2, "text": "This is a test"}],
        [{"points": 3, "text": "This is a test"}, {
            "points": 3, "text": "This is a test"}],
        [{"points": 4, "text": "This is a test"}, {
            "points": 4, "text": "This is a test"}],
        [{"points": 5, "text": "This is a test"}, {
            "points": 5, "text": "This is a test"}]
    ]
    new_data = flatten(data)
    assert len(new_data) == 10  # Check that data is flattened
    assert isinstance(new_data, list)  # Check that data is a list
    # Check that data contains dictionaries
    assert isinstance(new_data[0], dict)
    # Check that data is shuffled
    assert new_data != [sublist for l in data for sublist in l]


def test_flatten_wrong_format():
    
    pytest.raises(TypeError, flatten, [1, 4])  # Check that TypeError is raised


def test_balance_data():
    from src.training.data_processing import balance_data
    data = [
        {"points": 1, "text": "This is a test"},
        {"points": 2, "text": "This is a test"}, {"points": 2, "text": "This is a test"},
        {"points": 3, "text": "This is a test"}, {"points": 3, "text": "This is a test"}, {"points": 3, "text": "This is a test"},
        {"points": 4, "text": "This is a test"},
        {"points": 5, "text": "This is a test"},
    ]

    new_data = balance_data(data)
    # max_length found by checking the length of each list of ratings
    max_length = max([len(list(filter(lambda x: x['points'] == i, data)))
                      for i in range(1, 6)])
    max_points = 5
    # Check that data is balanced
    assert len(new_data) == max_length * max_points  # Check that data is balanced
    assert isinstance(new_data, list)  # Check that data is a list
    # Check that data contains dictionaries
    assert isinstance(new_data[0], dict)


def test_balance_data_wrong_format():
    from src.training.data_processing import balance_data
    # Check that TypeError is raised
    pytest.raises(TypeError, balance_data, [1, 4])

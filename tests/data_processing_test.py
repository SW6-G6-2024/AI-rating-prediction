import pytest

fake_path = 'tests/fixtures/test_data2.json'
data_path = 'tests/fixtures/test_data.json'

def test_load_data():
		from src.training.data_processing import load_data
		data = load_data(data_path)
		assert len(data) == 1000 # Check that data is loaded
		assert isinstance(data, list) # Check that data is a list
		assert isinstance(data[0], dict) # Check that data contains dictionaries
  
def test_load_data_no_file():
		from src.training.data_processing import load_data
		with pytest.raises(FileNotFoundError) as err:
				load_data(fake_path)
		# Check that the file is not found
		assert str(err.value) == "[Errno 2] No such file or directory: " + "'" + fake_path + "'"
    

def test_flatten():
		from src.training.data_processing import flatten
		data = [
				[{"points": 1, "text": "This is a test"}, {"points": 1, "text": "This is a test"}],
				[{"points": 2, "text": "This is a test"}, {"points": 2, "text": "This is a test"}],
				[{"points": 3, "text": "This is a test"}, {"points": 3, "text": "This is a test"}],
				[{"points": 4, "text": "This is a test"}, {"points": 4, "text": "This is a test"}],
				[{"points": 5, "text": "This is a test"}, {"points": 5, "text": "This is a test"}]
		]
		new_data = flatten(data)
		assert len(new_data) == 10 # Check that data is flattened
		assert isinstance(new_data, list) # Check that data is a list
		assert isinstance(new_data[0], dict) # Check that data contains dictionaries
		assert new_data != [sublist for l in data for sublist in l] # Check that data is shuffled
  
def test_flatten_wrong_format():
		from src.training.data_processing import flatten
		pytest.raises(TypeError, flatten, [1, 4]) # Check that TypeError is raised
  
def test_balance_data():
		from src.training.data_processing import balance_data
		data = [
				{"points": 1, "text": "This is a test"},
				{"points": 2, "text": "This is a test"}, {"points": 2, "text": "This is a test"},
				{"points": 3, "text": "This is a test"}, {"points": 3, "text": "This is a test"}, {"points": 3, "text": "This is a test"},
				{"points": 4, "text": "This is a test"},
				{"points": 5, "text": "This is a test"}
		]
		new_data = balance_data(data)
		assert len(new_data) == len(data) * max([len(lst) for lst in data]) # Check that data is processed
		assert isinstance(new_data, list) # Check that data is a list
		assert isinstance(new_data[0], dict) # Check that data contains dictionaries
  
def test_balance_data_wrong_format():
		from src.training.data_processing import balance_data
		pytest.raises(TypeError, balance_data, [1, 4]) # Check that TypeError is raised

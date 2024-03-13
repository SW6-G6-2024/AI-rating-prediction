import pytest

def test_separate_labels_success():
		from src.training.data_splitter import separate_labels
		data = [
				{"points": 1, "text": "This is a test"},
				{"points": 2, "text": "This is a test"},
				{"points": 3, "text": "This is a test"},
				{"points": 4, "text": "This is a test"},
				{"points": 5, "text": "This is a test"}
		]
		new_data, labels = separate_labels(data)
		assert new_data == [test for test in data if "points" not in test]
		assert labels == [1, 2, 3, 4, 5]
	
def test_separate_labels_failure():
		from src.training.data_splitter import separate_labels
		data = [
				{"points": 1, "text": "This is a test"},
				{"points": 2, "text": "This is a test"},
				{"points": 3, "text": "This is a test"},
				{"points": 4, "text": "This is a test"},
				{"points": 5.0, "text": "This is a test"}
		]
		with pytest.raises(ValueError) as err:
				new_data, labels = separate_labels(data)
				assert str(err.value) == 'Label must be an integer'
		
		data = [
				{"points": 1, "text": "This is a test"},
				{"text": "This is a test"},
				{"points": 3, "text": "This is a test"},
				{"points": 4, "text": "This is a test"},
				{"points": 5, "text": "This is a test"}
		]
		with pytest.raises(ValueError) as err:
				new_data, labels = separate_labels(data)
				assert str(err.value) == "No points in entry"
		
		data = [
				{"points": 1, "text": "This is a test"},
				{"points": 2, "text": "This is a test"},
				{"points": 3, "text": "This is a test"},
				{"points": 4, "text": "This is a test"},
				{"points": "5", "text": "This is a test"}
		]
		with pytest.raises(ValueError) as err:
				new_data, labels = separate_labels(data)
				assert str(err.value) == 'Label must be an integer'
		
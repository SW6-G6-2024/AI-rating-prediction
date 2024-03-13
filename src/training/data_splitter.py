def split_data(data: list[dict], labels, split_ratio: float = 0.8):
		""" Splits the data into training and test data.
		Args:
			data (list[dict]): training/evaluation data
			labels (list): labels for the training/evaluation data
			split_ratio (float): ratio to split the data
		Returns:
			tuple: training data, test data, training labels, test labels
		"""
	
		new_data = data.copy()
		if len(new_data) != len(labels):
				raise ValueError('Data and labels must be of same length')	
	
		split_index = int(len(new_data) * split_ratio)
		return new_data[:split_index], new_data[split_index:], labels[:split_index], labels[split_index:]

def separate_labels(data: list[dict]) -> tuple[list[dict], list[int]]:
		""" Separates the labels from the data.
		Args:
			data (list[dict]): training/evaluation data
		Returns:
			tuple: data, labels
		"""
		new_data = data.copy()
	
		for entry in new_data:
				if "points" not in entry:
						raise ValueError('No points in entry')
		
		labels = [entry["points"] for entry in new_data]
  
		# Remove the labels from the data
		for entry in new_data:
				if "points" in entry:
					del entry["points"]
     
		for label in labels:
				if not isinstance(label, int):
						raise ValueError('Label must be an integer')
	
		return new_data, labels
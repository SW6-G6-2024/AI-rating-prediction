import json
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt


def load_data(path: str) -> list[dict]:
		"""Reads data from file at a given path.
		Args:
			path (str): path to the file
		Returns:
			list[dict]: training data from 'data.json' file
		"""
		with open(path, 'r') as f:
				data = json.load(f)
		return data


def flatten(data: list[list[dict]]) -> list[dict]:
		""" flattens a multi dimensional list to a one dimensional list.
		Args:
			data (list): list of lists
		Returns:
			list[dict]: flattened list of points
		"""
		# Flatten the data
		return [sublist for l in data for sublist in l]


def process_data(data: list[dict]) -> list[dict]:
		""" Balances the amount of each rating by copying the data 
		for each rating to make the ratings more balanced.
		Args:
			data (list[dict]): training data
			
		Returns:
			list[dict]: list of points
		"""

		# 5 lists of data for each rating
		lists = [list(filter(lambda x: x['points'] == i, data)) for i in range(1, 6)] 
		# Length of each list of ratings
		lengths = [len(i) for i in lists] 
		max_length = max(lengths)
		# Factors to multiply each list by to make them roughly equal length
		factors = [round(max_length / i) for i in lengths] 
		
		for i in range(1, 6):
				# Multiply each list by the factor to make them roughly equal length
				lists[i-1] += lists[i - 1] * (factors[i - 1] - 1) 
		
		# Cut the lists to the same length
		lists = [i[:max_length+30] for i in lists]

		# Flatten the lists
		data = flatten(lists)

		return data


def make_plot(data) -> tuple[plt.Figure, list[plt.Axes]]:
		""" Plots point distribution with Seaborn	
		Returns:
			tuple[plt.Figure, list[plt.Axes]]: Illustration of the point distribution
		"""
		# Plotting with Seaborn
		fig, axes = plt.subplots(1, 2, sharex=True, figsize=(10,5))
		fig.suptitle('Rating Distribution')
		axes[0].set_title('Before Balancing')
		axes[1].set_title('After Balancing')
		
		for i, data in enumerate(data):
				df = pd.DataFrame(data)
				sb.histplot(df['points'], kde=False, ax=axes[i], bins=5)
				axes[i].set_xlabel('Rating')
				axes[i].set_ylabel('Count')
    
		plt.show()
		return fig, axes

# non-balanced data
data = load_data('data.json')
# balanced data
balanced_data = process_data(data)

make_plot([data, balanced_data])


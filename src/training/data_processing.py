import json
import random
from sys import argv
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from data_splitter import separate_labels, split_data


def load_data(path: str) -> list[dict]:
		"""Reads data from file at a given path.
		Args:
			path (str): path to the file
		Returns:
			list[dict]: data from loaded file
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

		newData = [sublist for l in data for sublist in l]
		random.shuffle(newData)
		return newData


def balance_data(data: list[dict]) -> list[dict]:
		""" Balances the amount of each rating by copying the data 
		for each rating to make the ratings more balanced.
		Args:
			data (list[dict]): training datas
			
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
		lists = [i[:max_length] for i in lists]

		# Flatten the lists
		data = flatten(lists)

		return data

def make_plot(data: list[list[dict]]) -> tuple[plt.Figure, list[plt.Axes]]: # pragma: no cover
		"""Plots the distribution of the ratings before and after balancing.

		Args:
				data (list[list[dict]]): list of points

		Returns:
				tuple[plt.Figure, list[plt.Axes]]: figure and axes
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

def process_data(path: str, plot: bool = False) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
		"""Processes the data from the file at the given path.
		Args:
			path (str): path to the file
		Returns:
			tuple[list[dict], list[dict], list[dict], list[dict]]: training data, labels, training data, labels
		"""
		data = load_data(path)
		balanced_data = balance_data(data)
		data, labels = separate_labels(balanced_data)

		if plot:
				make_plot([data, balanced_data])
		
		# Make data into a feature vector
		balanced_data = [
  			[
            entry['piste']['_id'],
				  	entry['piste']['direction'],
						entry['date']['year'],
						entry['date']['month'],
						entry['date']['day'],
						entry['date']['hours'],
						# entry['minutes'], # ignored minutes, as it is not relevant without hours
						*entry['weather'].values()
				] for entry in balanced_data
		]
	
		x_train, x_test, y_train, y_test = split_data(balanced_data, labels)
		return np.array(x_train), np.array(x_test), np.array(y_train), np.array(y_test)

# non-balanced data
data = load_data('data.json')
# balanced data
balanced_data = balance_data(data)

if(len(argv) >= 2 and argv[1] == "plot"):
	make_plot([data, balanced_data])

data, labels = separate_labels(balanced_data)

data = [
  [
        entry['piste']['_id'],
	  		entry['piste']['direction'],
				entry['date']['year'],
				entry['date']['month'],
				entry['date']['day'],
				entry['date']['hours'],
				#entry['minutes'],
				*entry['weather'].values()
		] for entry in balanced_data
]

x_train, x_test, y_train, y_test = split_data(data, labels)
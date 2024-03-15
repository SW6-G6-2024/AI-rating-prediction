import numpy as np
import torch
from ffn import RatingModel
from data_processing import process_data
from torch import nn

def train_model(Model: nn.Module):
	# load the data from the json file
	x_train, x_test, y_train, y_test = process_data('data.json')
	
	# TODO: init and train the model
	model = Model(x_train.shape[1], 1)
	print(x_train)
	
	# using the mean squared error loss function
	criterion = torch.nn.MSELoss()
	# using the Adam optimizer
	optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
	# define number of epochs
	epochs = 100
	batch_size = 10
	batches_pr_epoch = len(x_train) // batch_size

	for epoch in range(epochs):
		total_loss = 0.0
		total_accuracy = 0.0
		total_samples = 0
		# iterate over the training data
		for i in range(batches_pr_epoch):
				start = i * batch_size
				# clear the gradients
				x_batch = torch.tensor(x_train[start:start+batch_size], dtype=torch.float32)
				y_batch = torch.tensor(y_train[start:start+batch_size], dtype=torch.float32).reshape(-1, 1)
				# make a prediction
				y_pred = model(x_batch)
				
				# compute the loss
				cost = criterion(y_pred, y_batch)
				total_loss += cost.item()

				optimizer.zero_grad()
				cost.backward()
				optimizer.step()
    
				batch_accuracy = torch.sum(y_pred.round() == y_batch)
				total_accuracy += batch_accuracy
				total_samples += len(y_batch)
			
		avg_loss = total_loss / total_samples
		avg_accuracy = total_accuracy / total_samples
			
		if epoch % 10 == 0:
			print(f'epoch: {epoch} cost: {avg_loss} accuracy: {avg_accuracy}')
	
	# evaluate the model
	model.eval()
	with torch.no_grad():
		y_pred = model(torch.tensor(x_test, dtype=torch.float32))
		cost = criterion(y_pred, torch.tensor(y_test, dtype=torch.float32).reshape(-1, 1))
		accuracy = torch.sum(y_pred.round() == torch.tensor(y_test, dtype=torch.float32)) / len(y_test)
		print(f'Cost: {cost.item()} Accuracy: {accuracy}')

train_model(RatingModel)
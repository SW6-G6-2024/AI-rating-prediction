import json
import numpy as np
import torch
from ffn import RatingModel

def training_model():
  # load the data from the json file
  with open('data.json', 'r') as f:
    data = json.load(f)

  features = []
  labels = [] 
  
  for entry in data['data']:
    weather_features = entry['weather']
    feature_vector = [
        entry['pisteId'],
        entry['month'],
        entry['day'],
        entry['hour'],
        # using * to unpack the values from the key-value pairs
        *weather_features.values()
    ]
    features.append(feature_vector)
    labels.append(entry['rating'])

  # convert the lists to numpy arrays
  features = np.array(features)
  labels = np.array(labels)
  # convert the numpy arrays to torch tensors
  features = torch.tensor(features)
  labels = torch.tensor(labels)
  
  # TODO: init and train the model

training_model()
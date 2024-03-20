from torch import nn

class RatingModel(nn.Module):
  def __init__(self, input_size, output_size):
        super(RatingModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)  # Input features: 13, Output features: 64
        self.relu = nn.ReLU()          # ReLU activation function
        self.dropout = nn.Dropout(0.2) # Dropout with 20% probability
        self.fc2 = nn.Linear(64, 32)  # Input features: 64, Output features: 32
        self.fc3 = nn.Linear(32, output_size)    # Input features: 32, Output features: 5 (number of classes)

  def forward(self, x):
      x = self.fc1(x)
      x = self.relu(x)
      x = self.dropout(x)
      x = self.fc2(x)
      x = self.relu(x)
      x = self.dropout(x)
      x = self.fc3(x)
      return x

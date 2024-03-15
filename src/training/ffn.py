from torch import nn

class RatingModel(nn.Module):
  def __init__(self, input_size, output_size=1):
    super(RatingModel, self).__init__()
    # define the layers
    self.l1 = nn.Linear(input_size, 10)
    self.dropout = nn.Dropout(0.2)
    self.relu = nn.ReLU()
    self.l2 = nn.Linear(10, 5)
    self.l3 = nn.Linear(5, output_size)

  def forward(self, x):
    output = self.l1(x)
    output = self.dropout(output)
    output = self.relu(output)
    output = self.l2(output)
    output = self.dropout(output)
    output = self.relu(output)
    output = self.l3(output)
    return output

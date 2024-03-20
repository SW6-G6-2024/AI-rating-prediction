
import numpy as np
import torch
from ffn import RatingModel
from data_processing import process_data
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
import matplotlib.pyplot as plt

# Load and preprocess the data
x_train, x_test, y_train, y_test = process_data('data.json')
y_train = y_train - 1  # Adjust target labels to start from 0
y_train = torch.LongTensor(y_train)

# Initialize the model
model = RatingModel(x_train.shape[1], 5)

# Define the loss function
criterion = nn.CrossEntropyLoss()

# Create DataLoader objects for training and testing
train_data = TensorDataset(torch.Tensor(x_train), y_train)
test_data = TensorDataset(torch.Tensor(x_test), torch.LongTensor(y_test))  # Ensure target labels are LongTensor
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
test_loader = DataLoader(test_data, batch_size=32, shuffle=False)

# Training function
def train_model(model, criterion, train_loader, optimizer, epochs=10):
    train_losses = []  # List to store training losses for visualization
    test_accuracies = []  # List to store test accuracies for visualization
    for epoch in range(epochs):
        model.train()  # Set model to training mode
        running_loss = 0.0
        for inputs, targets in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        train_loss = running_loss / len(train_loader)
        train_losses.append(train_loss)
        print(f"Epoch {epoch+1}, Loss: {train_loss}")
        
        # Evaluate on test data
        test_accuracy = evaluate_model(model, test_loader)
        test_accuracies.append(test_accuracy)
        print(f"Test Accuracy: {test_accuracy}%")
    
    # Plot training losses and test accuracies
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(range(1, epochs+1), train_losses, label='Training Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training Loss Over Epochs')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(range(1, epochs+1), test_accuracies, label='Test Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy (%)')
    plt.title('Test Accuracy Over Epochs')
    plt.legend()
    
    plt.show()

# Evaluation function
def evaluate_model(model, data_loader):
    model.eval()  # Set model to evaluation mode
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, targets in data_loader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
            total += targets.size(0)
            correct += (predicted == targets).sum().item()
    accuracy = (correct / total) * 100
    return accuracy

# Initialize optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Train the model
# train_model(model, criterion, train_loader, optimizer)

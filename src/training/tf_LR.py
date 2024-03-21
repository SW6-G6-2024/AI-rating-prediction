from sklearn.metrics import accuracy_score
from data_processing import process_data
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import os

# load and process data
x_train, x_test, y_train, y_test = process_data('data.json')
y_train = y_train - 1  # Adjust target labels to start from 0
y_test = y_test - 1  # Adjust feature values to start from 0

# Initialize the model (LR)
model = LogisticRegression(max_iter=1000)
# Train the model
model.fit(x_train, y_train)
# make predictions on the test data
test_predictions = model.predict(x_test)
# evaluate the model on the test data
test_accuracy = accuracy_score(y_test, test_predictions)
print(f"Testing Accuracy: {test_accuracy * 100}")

# predict on training data
train_predictions = model.predict(x_train)
# evaluate the model on the training data
train_accuracy = accuracy_score(y_train, train_predictions)
print(f"Training Accuracy: {train_accuracy * 100}")

cm = confusion_matrix(y_test, test_predictions)
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Reds', cbar=False)
plt.xticks(np.arange(len(cm))+0.5, np.arange(1, len(cm)+1))
plt.yticks(np.arange(len(cm))+0.5, np.arange(1, len(cm)+1))
plt.title('LR validation confusion matrix')
plt.xlabel(f'Predicted \n\n Test Accuracy: {test_accuracy*100:.5f}%, Training Accuracy: {train_accuracy*100:.5f}%\n')
plt.ylabel('Actual')

# Create the 'images' folder if it doesn't exist
images_folder = 'images'
if not os.path.exists(images_folder):
    os.makedirs(images_folder)
    print("Created 'images' folder...")

# Save the plot to the images folder
try:
    plt.savefig(os.path.join(images_folder, 'LR_confusion_matrix.png'))
except:
    print("Could not save the LR confusion matrix plot.")
else:
    print("LR confusion matrix plot saved.")
from sklearn.metrics import accuracy_score, confusion_matrix
from data_processing import process_data
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# load and process data
x_train, x_test, y_train, y_test = process_data('data.json')
y_train = y_train - 1  # Adjust target labels to start from 0
y_test = y_test - 1  # Adjust feature values to start from 0

# Scale the features (recommended for SVM)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Initialize the SVM model without specifying C
model = SVC(kernel='linear')

# Train the model
print("Training in progress...")
model.fit(x_train_scaled, y_train)
print("Training completed.")

# make predictions on the test data
test_predictions = model.predict(x_test_scaled)
# evaluate the model on the test data
test_accuracy = accuracy_score(y_test, test_predictions)
print(f"Testing Accuracy: {test_accuracy * 100}")

# predict on training data
train_predictions = model.predict(x_train_scaled)
# evaluate the model on the training data
train_accuracy = accuracy_score(y_train, train_predictions)
print(f"Training Accuracy: {train_accuracy * 100}")

# plot confusion matrix
cm = confusion_matrix(y_test, test_predictions)
plt.figure(figsize=(10, 9))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', cbar=True)
plt.xticks(np.arange(len(cm))+0.5, np.arange(1, len(cm)+1))
plt.yticks(np.arange(len(cm))+0.5, np.arange(1, len(cm)+1))
plt.title('SVM validation confusion matrix')
plt.xlabel(f'Predicted\n\n Test Accuracy: {test_accuracy*100:.5f}%\nTraining Accuracy: {train_accuracy*100:.5f}%\n')
plt.ylabel('Actual')

# Create the 'images' folder if it doesn't exist
images_folder = 'images'
if not os.path.exists(images_folder):
    os.makedirs(images_folder)
    print("Created 'images' folder...")

# Save the plot to the images folder
try:
    plt.savefig(os.path.join(images_folder, 'SVM_confusion_matrix.pdf'), format='pdf')
except:
    print("Could not save the SVM confusion matrix.")
else:
    print("SVM confusion matrix plot saved.")
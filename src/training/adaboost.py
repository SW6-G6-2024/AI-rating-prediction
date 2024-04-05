from sklearn.ensemble import AdaBoostClassifier
from data_processing import process_data
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# load data
x_train, x_test, y_train, y_test = process_data('data.json')
y_train = y_train - 1  # Adjust target labels to start from 0
y_test = y_test - 1  # Adjust feature values to start from 0

# Scale the features
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

ada = AdaBoostClassifier(n_estimators=200, learning_rate=1, algorithm='SAMME')

print("Training AdaBoost model...")
ada_model = ada.fit(x_train_scaled, y_train)
print("AdaBoost model trained.")

ada_train_pred = ada_model.predict(x_train_scaled)
ada_test_pred = ada_model.predict(x_test_scaled)

# Accuracy on training set
train_accuracy = accuracy_score(y_train, ada_train_pred)
print("Training Accuracy:", train_accuracy * 100)

# Accuracy on test set
test_accuracy = accuracy_score(y_test, ada_test_pred)
print("Test Accuracy:", test_accuracy * 100)

# plot confusion matrix
cm = confusion_matrix(y_test, ada_test_pred)
plt.figure(figsize=(10, 9))
sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges', cbar=True)
plt.xticks(np.arange(len(cm))+0.5, np.arange(1, len(cm)+1))
plt.yticks(np.arange(len(cm))+0.5, np.arange(1, len(cm)+1))
plt.title('AdaBoost validation confusion matrix')
plt.xlabel(f'Predicted\n\n Test Accuracy: {test_accuracy*100:.5f}%\nTraining Accuracy: {train_accuracy*100:.5f}%\n')
plt.ylabel('Actual')

# Create the 'images' folder if it doesn't exist
images_folder = 'images'
if not os.path.exists(images_folder):
    os.makedirs(images_folder)
    print("Created 'images' folder...")

# Save the plot to the images folder
try:
    plt.savefig(os.path.join(images_folder, 'ada_confusion_matrix.pdf'), format='pdf')
except:
    print("Could not save the AdaBoost confusion matrix plot.")
else:
    print("AdaBoost confusion matrix plot saved.")
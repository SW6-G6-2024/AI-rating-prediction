from sklearn.metrics import accuracy_score
from data_processing import process_data
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# load and process data
x_train, x_test, y_train, y_test = process_data('data.json')
y_train = y_train - 1  # Adjust target labels to start from 0

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

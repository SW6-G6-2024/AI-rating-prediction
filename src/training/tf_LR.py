from sklearn.metrics import accuracy_score
from data_processing import process_data
from sklearn.linear_model import LogisticRegression

# load and process data
x_train, x_test, y_train, y_test = process_data('data.json')
y_train = y_train - 1  # Adjust target labels to start from 0

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



from sklearn.ensemble import AdaBoostClassifier
from data_processing import process_data
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# load data
x_train, x_test, y_train, y_test = process_data('data.json')

# Scale the features
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

ada = AdaBoostClassifier(n_estimators=2000, learning_rate=1, algorithm='SAMME')

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
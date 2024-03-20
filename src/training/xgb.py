from xgboost import XGBClassifier
from data_processing import process_data
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# load data
x_train, x_test, y_train, y_test = process_data('data.json')
y_train = y_train - 1  # Adjust target labels to start from 0
y_test = y_test - 1  # Adjust feature values to start from 0

# Scale the features
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Train the XGBoost model
# n_estimators: Number of boosting rounds
# learning_rate: Step size shrinkage used to prevent overfitting
# subsample: Fraction of samples used for training
# reg_lambda: L2 regularization term on weights
# reg_alpha: L1 regularization term on weights
xgb = XGBClassifier(n_estimators=2000, learning_rate=0.3, subsample=0.2, req_lambda=1, req_alpha=1)

print("Training XGBoost model...")
# early_stopping_rounds: Stop training if no improvement in n rounds
# eval_set: Validation set to evaluate the model
xgb_model = xgb.fit(x_train_scaled, y_train, early_stopping_rounds=50, eval_set=[(x_test_scaled, y_test)])
print("XGBoost model trained.")

xgb_train_pred = xgb_model.predict(x_train_scaled)
xgb_test_pred = xgb_model.predict(x_test_scaled)

# Accuracy on training set
train_accuracy = accuracy_score(y_train, xgb_train_pred)
print("Training Accuracy:", train_accuracy * 100)

# Accuracy on test set
test_accuracy = accuracy_score(y_test, xgb_test_pred)
print("Test Accuracy:", test_accuracy * 100)
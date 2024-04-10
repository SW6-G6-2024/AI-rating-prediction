from xgboost import XGBClassifier
from data_processing import process_data
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
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

# Train the XGBoost model
# n_estimators: Number of boosting rounds
# learning_rate: Step size shrinkage used to prevent overfitting
# subsample: Fraction of samples used for training
# reg_lambda: L2 regularization term on weights
# reg_alpha: L1 regularization term on weights
xgb = XGBClassifier(n_estimators=2000, learning_rate=0.3, subsample=0.2)

print("Training XGBoost model...")
# early_stopping_rounds: Stop training if no improvement in n rounds
# eval_set: Validation set to evaluate the model
xgb_model = xgb.fit(x_train_scaled, y_train, early_stopping_rounds=50, eval_set=[
                    (x_test_scaled, y_test)])
print("XGBoost model trained.")

# Save the trained model
model_path = 'src/saved_models/xgb_model.json'
xgb_model.save_model(model_path)

# Predictions
xgb_train_pred = xgb_model.predict(x_train_scaled)
xgb_test_pred = xgb_model.predict(x_test_scaled)

# Accuracy on training set
train_accuracy = accuracy_score(y_train, xgb_train_pred)
print("Training Accuracy:", train_accuracy * 100)

# Accuracy on test set
test_accuracy = accuracy_score(y_test, xgb_test_pred)
print("Test Accuracy:", test_accuracy * 100)

cm = confusion_matrix(y_test, xgb_test_pred)
plt.figure(figsize=(10, 9))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=True)
plt.xticks(np.arange(len(cm))+0.5, np.arange(1, len(cm)+1))
plt.yticks(np.arange(len(cm))+0.5, np.arange(1, len(cm)+1))
plt.title('XGB validation confusion matrix')
plt.xlabel(
    f'Predicted \n\nTest Accuracy: {test_accuracy*100:.5f}%\nTraining Accuracy: {train_accuracy*100:.5f}%\n')
plt.ylabel('Actual')

# Create the 'images' folder if it doesn't exist
images_folder = 'images'
if not os.path.exists(images_folder):
    os.makedirs(images_folder)
    print("Created 'images' folder...")

# Save the plot to the images folder
try:
    plt.savefig(os.path.join(images_folder,
                'XGB_confusion_matrix.pdf'), format='pdf')
except:
    print("Could not save the XGB confusion matrix.")
else:
    print("XGB confusion matrix plot saved.")


feature_importances = xgb_model.feature_importances_
features = ['year', 'month', 'day', 'hours', 'temp', 'wcode',
            'wspeed', 'wdirection', 'snowfall', 'snowdepth', 'rain', 'visibility']

plt.figure(figsize=(10, 6))
plt.barh(features, feature_importances)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title('XGBoost Feature Importance')
plt.savefig(os.path.join(images_folder, 'XGB_feature_importance.pdf'), format='pdf')

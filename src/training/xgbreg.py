from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from data_processing import process_data
import matplotlib.pyplot as plt
from xgboost import plot_importance
import os

x_train, x_test, y_train, y_test = process_data('data.json')
y_train = y_train - 1  # Adjust target labels to start from 0
y_test = y_test - 1  # Adjust feature values to start from 0

# Train the XGBoost model
xgb = XGBRegressor(n_estimators=2000, learning_rate=0.3, subsample=0.2)

print("Training XGBoost model...")
xgb_model = xgb.fit(x_train, y_train, early_stopping_rounds=50, eval_set=[
                    (x_test, y_test)], verbose=False)
print("XGBoost model trained.")

# Save the trained model
model_path = 'src/saved_models/xgb_model_reg.json'
xgb_model.save_model(model_path)

# Predictions
xgb_train_pred = xgb_model.predict(x_train)
xgb_test_pred = xgb_model.predict(x_test)

# Calculate Root Mean Squared Error
rmse = mean_squared_error(y_test, xgb_test_pred)
print("Root Mean Squared Error:", rmse)

# calculate Mean Absolute Error
mae = mean_absolute_error(y_test, xgb_test_pred)
print("Mean Absolute Error:", mae)


features = ['id', 'direction','year', 'month', 'day', 'hours', 'temp', 'wcode',
            'wspeed', 'wdirection', 'snowfall', 'snowdepth', 'rain', 'visibility']

plt.figure(figsize=(10, 6))
plot_importance(xgb_model)
plt.title('XGBoost Feature Importance')

images_folder = 'images'
if not os.path.exists(images_folder):
    os.makedirs(images_folder)
    print("Created 'images' folder...")

# Save the plot to the images folder
try:
    plt.savefig(os.path.join(images_folder,
                'XGB_reg_feature.pdf'), format='pdf')
except:
    print("Could not save the XGB feature importance.")
else:
    print("XGB feature importance plot saved.")
from sklearn.metrics import confusion_matrix
from data_processing import process_data
from sklearn.preprocessing import StandardScaler
from catboost import CatBoostClassifier, Pool
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

x_train, x_test, y_train, y_test = process_data('data.json')
y_train = y_train - 1  # Adjust target labels to start from 0
y_test = y_test - 1  # Adjust feature values to start from 0

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

pool = Pool(data=x_train_scaled, label=y_train)
model = CatBoostClassifier(iterations=8000, learning_rate=0.8, depth=4, loss_function='MultiClass')

print("Training CatBoost model...")

model.fit(pool, eval_set=(x_test_scaled, y_test), early_stopping_rounds=50)

print("CatBoost model trained.")
# test accuracy
test_accuracy = model.score(x_test_scaled, y_test)
print("Test Accuracy:", test_accuracy)
# training accuracy
train_accuracy = model.score(x_train_scaled, y_train)
print("Training Accuracy:", train_accuracy)


model.save_model('src/saved_models/catboost.json')
print("Model saved.")

cat_pred = model.predict(x_test_scaled)

cm = confusion_matrix(y_test, cat_pred)
plt.figure(figsize=(10, 9))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=True)
plt.xticks(np.arange(len(cm))+0.5, np.arange(1, len(cm)+1))
plt.yticks(np.arange(len(cm))+0.5, np.arange(1, len(cm)+1))
plt.title('Cat validation confusion matrix')
plt.xlabel(
    f'Predicted \n\nTest Accuracy: {test_accuracy*100:.5f}%\nTraining Accuracy: {train_accuracy*100:.5f}%\n')
plt.ylabel('Actual')

images_folder = 'images'
if not os.path.exists(images_folder):
    os.makedirs(images_folder)
    print("Created 'images' folder...")

# Save the plot to the images folder
try:
    plt.savefig(os.path.join(images_folder,
                'CAT_confusion_matrix.pdf'), format='pdf')
except:
    print("Could not save the CAT confusion matrix.")
else:
    print("CAT confusion matrix plot saved.")


model.plot(kind='FeatureImportance', figsize=(10, 6))

images_folder = 'images'
if not os.path.exists(images_folder):
    os.makedirs(images_folder)
    print("Created 'images' folder...")

# Save the plot to the images folder
try:
    plt.savefig(os.path.join(images_folder,
                'CAT_Feature_importance.pdf'), format='pdf')
except:
    print("Could not save the CAT feature importance.")
else:
    print("CAT feature importance plot saved.")
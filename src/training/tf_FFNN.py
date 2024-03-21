from data_processing import process_data
from sklearn.preprocessing import StandardScaler
from keras import Sequential
from keras.layers import Dense, Dropout, Input
from matplotlib import pyplot as plt
from keras.callbacks import EarlyStopping
from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np
import os

# load data
x_train, x_test, y_train, y_test = process_data('data.json')
y_train = y_train - 1  # Adjust target labels to start from 1
y_test = y_test - 1  # Adjust feature values to start from 1

# Scale the features (recommended for FFNN)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# init FFNN model
model = Sequential()
model.add(Input(shape=(x_train_scaled.shape[1],))) # resolves warning
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(16, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(8, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(5, activation='softmax'))

# Define early stopping callback
early_stopping = EarlyStopping(
    monitor='val_loss', patience=5, restore_best_weights=True)

# compile and train model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

history = model.fit(
    x_train_scaled,
    y_train, epochs=100,
    batch_size=32,
    validation_data=(x_test_scaled, y_test),
    callbacks=[early_stopping]
)

# Evaluate the model
train_loss, train_accuracy = model.evaluate(x_train_scaled, y_train, verbose=0)
print("Training Accuracy:", train_accuracy)
print("Training Loss:", train_loss)

# Evaluate the model on test data
test_loss, test_accuracy = model.evaluate(x_test_scaled, y_test, verbose=0)
print("Test Accuracy:", test_accuracy)
print("Test Loss:", test_loss)


# Plot training & validation loss values
plt.figure(figsize=(12, 7))
# Plot loss
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Train')
plt.plot(history.history['val_loss'], label='Test')
plt.title('FFNN Loss')
plt.xlabel(f'Epoch\n\nTrain Loss: {train_loss*100:.5f}%\nTest Loss: {test_loss*100:.5f}%')
plt.ylabel('Loss')
plt.legend()

# Plot accuracy
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Train')
plt.plot(history.history['val_accuracy'], label='Test')
plt.title('FFNN Accuracy')
plt.xlabel(f'Epoch\n\nTrain Accuracy: {train_accuracy*100:.5f}%\nTest Accuracy: {test_accuracy*100:.5f}%')
plt.ylabel('Accuracy')
plt.legend()

plt.tight_layout()
# Create the 'images' folder if it doesn't exist
images_folder = 'images'
if not os.path.exists(images_folder):
    os.makedirs(images_folder)
    print("Created 'images' folder...")

# Save the plot to the images folder
try:
    plt.savefig(os.path.join(images_folder, 'FFNN_graph.pdf'), format='pdf')
except:
    print("Could not save the FFNN graph.")
else:
    print("FFNN graph plot saved.")

# Plot Confusion matrix
# Predict the values from the validation dataset
y_pred = model.predict(x_test_scaled)
# Convert predictions classes to one hot vectors
y_pred = np.argmax(y_pred, axis=1)
# compute the confusion matrix
cm = confusion_matrix(y_test, y_pred)
# plot the confusion matrix
plt.figure(figsize=(10, 9))
sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', cbar=True)
plt.xticks(np.arange(len(cm))+0.5, np.arange(1, len(cm)+1))
plt.yticks(np.arange(len(cm))+0.5, np.arange(1, len(cm)+1))
plt.title('FFNN validation confusion matrix')
plt.xlabel(f'Predicted\n\n Test Accuracy: {test_accuracy*100:.5f}%\nTrain Accuracy: {train_accuracy*100:.5f}%')
plt.ylabel('Actual')

# Save the plot to the images folder
try:
    plt.savefig(os.path.join(images_folder, 'FFNN_confusion_matrix.pdf'), format='pdf')
except:
    print("Could not save the FFNN confusion matrix plot.")
else:
    print("FFNN confusion matrix plot saved.")
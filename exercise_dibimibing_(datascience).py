# -*- coding: utf-8 -*-
"""Exercise DIBIMIBING (DataScience)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SAELhe81-jPyMJy6Jkl8Ks8W-cFj9dHV
"""

# Import the pandas library for data manipulation
import pandas as pd

# Import the datasets module from scikit-learn to load built-in datasets
from sklearn import datasets

# Load the wine dataset from scikit-learn
wine = datasets.load_wine()

# Store the feature data (independent variables) in the variable x
x = wine.data  # `x` is a NumPy array containing the features for each sample

# Store the target labels (dependent variables) in the variable y
y = wine.target  # `y` is a NumPy array containing the class label for each sample

# Create a DataFrame from the feature data (x) with column names from wine.feature_names
df_x = pd.DataFrame(x, columns=wine.feature_names)

# Create a Series from the target data (y) and name it 'target'
df_y = pd.Series(y, name='target')

# Combine the feature DataFrame (df_x) and the target Series (df_y) into a single DataFrame
df = pd.concat([df_x, df_y], axis=1)

# Display the first 5 rows of the DataFrame to inspect the data
print(df.head(10))

df.info()

df['target'].unique()

df.describe()

# Import the train_test_split function from scikit-learn for splitting the dataset
from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    df_x,       # Feature data (independent variables)
    df_y,       # Target data (dependent variable)
    test_size=0.2,  # Proportion of the dataset to include in the test set (20%)
    random_state=42  # Ensures reproducibility by setting a random seed
)

# Import the DecisionTreeClassifier from scikit-learn
from sklearn.tree import DecisionTreeClassifier

# Create an instance of the DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=42)  # random_state ensures reproducibility

# Train the decision tree model using the training dataset
model.fit(x_train, y_train)  # x_train: features, y_t

# Import the accuracy_score function from scikit-learn for evaluating model accuracy
from sklearn.metrics import accuracy_score

# Use the trained model to make predictions on the test set
y_pred = model.predict(x_test)  # Predict the target labels for the test set features

# Calculate the accuracy of the model by comparing predicted and actual target labels
accuracy = accuracy_score(y_test, y_pred)  # Returns the proportion of correct predictions

# Print the classification report (accuracy of the model)
print("Classification Report")
print(f"Accuracy: {accuracy * 100:.2f}%")  # Display accuracy as a percentage with 2 decimal places

# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Import the tree module from scikit-learn for visualizing decision trees
from sklearn import tree

# Create a figure for the plot with specified dimensions
plt.figure(figsize=(15, 10))  # Width: 15, Height: 10

# Plot the decision tree
tree.plot_tree(
    model,  # The trained decision tree model
    feature_names=wine.feature_names,  # Correct spelling: Feature names from the dataset
    class_names=wine.target_names,  # Class names corresponding to the target labels
    filled=True  # Fill nodes with colors representing different classes
)

# Add a title to the plot
plt.title("Decision Tree - Wine Dataset")

# Display the plot
plt.show()
import pandas as pd
path="Salary_dataset.csv"
df=pd.read_csv(path)
del df['Unnamed: 0']

# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Assuming your data is already loaded in 'df' with 'YearsExperience' and 'Salary' columns

# Define features and target variable
X = df[['YearsExperience']]  # Features
y = df['Salary']             # Target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Save the model
joblib.dump(model, 'linear_regression_model.joblib')
print("Model saved as 'linear_regression_model.joblib'")

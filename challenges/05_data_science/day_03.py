import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# load data set
data = pd.read_csv("experience_salary.csv")

X = data[["YearsExperience"]]
y = data[["Salary"]]

model = LinearRegression()
model.fit(X, y)

data["PredictedSalary"] = model.predict(X)

# print("Model Coefficients (slope)", round(model.coef_[0], 2))
# print("Model Intercept (y-intercept)", round(model.intercept_, 2))

print("Model Coefficient (slope)", round(float(model.coef_[0]), 2))
print("Model Intercept (base salary)", round(float(model.intercept_), 2))

plt.scatter(X, y, color="blue", label="Actual Salary")
plt.plot(X, data["PredictedSalary"], color="red", label="Predicted Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")
plt.legend()
plt.show()
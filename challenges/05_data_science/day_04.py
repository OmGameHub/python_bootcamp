import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

# load data set
data = pd.read_csv("experience_salary.csv")

X = data[["YearsExperience"]]
y = data[["Salary"]]

model = LinearRegression()
model.fit(X, y)

st.title("Salary Prediction")
st.write("Enter your years of experience to predict your salary:")
years_of_experience = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.1)

if years_of_experience:
    print(years_of_experience)

    predicted_salary = model.predict([[years_of_experience]])[0]
    st.success(f"Estimated Salary: {predicted_salary}")

st.subheader("Regression Line")

data["PredictedSalary"] = model.predict(X)

fig, ax = plt.subplots()
ax.scatter(X, y, color="blue", label="Actual Salary")
ax.plot(X, data["PredictedSalary"], color="red", label="Predicted Salary")
ax.set_xlabel("Years of Experience")
ax.set_ylabel("Salary")
ax.set_title("Experience vs Salary")
ax.legend()
st.pyplot(fig)

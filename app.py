import streamlit as st
import pandas as pd
from sympy import symbols, Eq, solve

st.title("Sample Streamlit App")

# Read the dataset
@st.cache  # Use caching to improve performance
def load_data():
    data = pd.read_csv('data/dataset.csv')
    return data

data = load_data()

st.header("Sample Dataset")
st.write(data)

st.header("Algebraic Equation Solver")
st.write("Solve an equation of the form 'ax + b = 0'")

# User input for the equation
a = st.number_input("Enter the value of 'a':")
b = st.number_input("Enter the value of 'b':")

equation = Eq(a * symbols('x') + b, 0)

if st.button("Solve Equation"):
    try:
        solution = solve(equation, symbols('x'))
        st.write(f"Solutions for x: {solution}")
    except Exception as e:
        st.error("Invalid Equation")

import streamlit as st
from sympy import symbols, Eq, solve

st.title("Algebraic Equation Solver")

st.write("Enter an algebraic equation (e.g., '2x + 2 = 4', '2x = 2', '2x + 2x = 4'):")

# User input for the equation
equation_input = st.text_input("Equation:")

# Define a symbolic variable
x = symbols('x')

try:
    # Parse and solve the equation
    equation = Eq(eval(equation_input.replace('x', '*x')), 0)
    solution = solve(equation, x)

    st.write(f"Solutions for x: {solution}")
except Exception as e:
    st.error("Invalid Equation")

import streamlit as st
import numpy as np

st.title("Linear Equation Solver")

st.write("Enter a linear system of equations as space-separated values (e.g., '3 -9; 2 4' * 'x y' = '-42 2', '1 -2 -1; 2 2 -1; -1 -1 2' * 'x y z' = '6 1 1'):")

# User input for the equation
equation_input = st.text_input("Linear System of Equations:")

try:
    # Split the input into matrices and vectors
    matrices, variables_and_constants = equation_input.split('*')

    coefficients = [list(map(float, matrix.strip().split())) for matrix in matrices.split(';')]
    constants = list(map(float, variables_and_constants.split('='))

    # Parse matrices and vectors
    A = np.array(coefficients)
    b = np.array(constants)

    # Solve the linear system of equations
    x = np.linalg.solve(A, b)

    st.write(f"Solutions for variables: {x}")
except Exception as e:
    st.error("Invalid Linear System of Equations")

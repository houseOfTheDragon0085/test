import streamlit as st
import numpy as np

st.title("Linear Equation Solver")

st.write("Enter a linear system of equations as matrices (e.g., '[3, -9; 2, 4] * [x; y] = [-42; 2]', '[1, -2, -1; 2, 2, -1; -1, -1, 2] * [x; y; z] = [6; 1; 1]'):")

# User input for the equation
equation_input = st.text_input("Linear System of Equations:")

try:
    # Split the input into matrices and vectors
    equations = equation_input.split('=')
    coefficients, constants = equations[0].strip(), equations[1].strip()

    # Parse matrices and vectors
    A = np.array(eval(coefficients.replace('[', '').replace(']', '')))

    b = np.array(eval(constants.replace('[', '').replace(']', ''))

    # Solve the linear system of equations
    x = np.linalg.solve(A, b)

    st.write(f"Solutions for variables: {x}")
except Exception as e:
    st.error("Invalid Linear System of Equations")

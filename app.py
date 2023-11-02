import streamlit as st
import sympy as sym

st.title("Algebraic Equation Solver with SymPy")

st.write("Enter an algebraic equation with symbolic variables (e.g., '2*x**2 + y + z = 1', 'x + 2*y + z = c1', '-2*x + y = -z'):")

# User input for the equation
equation_input = st.text_input("Equation:")

# Define symbolic variables
x, y, z, c1 = sym.symbols('x y z c1')

try:
    # Parse and solve the equation
    equations = [sym.Eq(*sym.sympify(eq.split('='))) for eq in equation_input.split(',')]
    solutions = sym.solve(equations, (x, y, z))

    st.write("Solutions for x, y, z:")
    for solution in solutions:
        st.write(solution)
except Exception as e:
    st.error("Invalid Equation")

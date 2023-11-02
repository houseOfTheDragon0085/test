import streamlit as st
import sympy as sym

st.title("Symbolic Equation Solver with SymPy")

st.write("Enter algebraic equations with symbolic variables in separate fields:")

# User input for the equations
equation_x = st.text_input("Equation for x:")
equation_y = st.text_input("Equation for y:")
equation_z = st.text_input("Equation for z:")

# Define symbolic variables
x, y, z, c1 = sym.symbols('x y z c1')

try:
    # Parse and solve the equations
    eq_x = sym.Eq(*sym.sympify(equation_x.split('=')))
    eq_y = sym.Eq(*sym.sympify(equation_y.split('=')))
    eq_z = sym.Eq(*sym.sympify(equation_z.split('=')))

    solution_x = sym.solve(eq_x, x)
    solution_y = sym.solve(eq_y, y)
    solution_z = sym.solve(eq_z, z)

    st.write("Solutions:")
    st.write(f"x = {solution_x}")
    st.write(f"y = {solution_y}")
    st.write(f"z = {solution_z}")
except Exception as e:
    st.error("Invalid Equations")

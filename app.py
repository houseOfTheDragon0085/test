import streamlit as st
import sympy as sym

st.title("Algebraic Expression Solver")

st.write("Enter an algebraic expression (e.g., 'x + y + x - y', '2x + 2y'):")

# User input for the expression
expression_input = st.text_input("Expression:")

# Define symbolic variables
x = sym.Symbol('x')
y = sym.Symbol('y')

try:
    # Parse the expression
    parsed_expr = sym.sympify(expression_input)

    # Simplify the expression
    simplified_expr = sym.simplify(parsed_expr)

    st.write(f"Simplified expression: {simplified_expr}")
except Exception as e:
    st.error("Invalid Expression")

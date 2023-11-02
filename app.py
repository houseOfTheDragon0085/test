import streamlit as st
import sympy as sym

st.title("Simplify")

st.write("Enter an algebraic expression (e.g., 'x + y + x - y', '(x + y) ** 2'):")

# User input for the expression
expression_input = st.text_input("Expression:")

# Define symbolic variables
x = sym.Symbol('x')
y = sym.Symbol('y')

try:
    # Parse and simplify the expression
    expression = sym.simplify(expression_input)

    st.write(f"Simplified Expression: {expression}")
except Exception as e:
    st.error("Invalid Expression")

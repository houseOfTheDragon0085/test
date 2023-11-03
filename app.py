import streamlit as st
import sympy as sym

st.title("Algebraic Expression Solver")

st.write("Enter an algebraic expression (e.g., 'x + y + x - y', '2x + 2y'):")

# User input for the expression
expression_input = st.text_input("Expression:")

# Define symbolic variables
x, y = sym.symbols('x y')

try:
    # Parse the expression
    parsed_expr = sym.sympify(expression_input)

    # Simplify the expression
    simplified_expr = sym.simplify(parsed_expr)

    st.write(f"Original expression: {parsed_expr}")
    st.write(f"Simplified expression: {simplified_expr}")

    # Solve the expression and get step-by-step solutions
    solutions = sym.solveset(simplified_expr, (x, y), domain=sym.S.Reals)
    
    st.write("Solving steps:")
    for solution in solutions:
        st.write(solution)

except Exception as e:
    st.error("Invalid Expression")

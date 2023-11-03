import streamlit as st
import sympy as sym

st.title("Algebraic Expression Solver")

st.write("Enter an algebraic expression (e.g., 'x + y + x - y', '2x + 2x + 2y - y'):")

# User input for the expression
expression_input = st.text_input("Expression:")

# Define symbolic variables
x, y, z, a, b = sym.symbols('x y z a b')

try:
    # Parse the expression
    parsed_expr = sym.sympify(expression_input)

    # Display the original expression
    st.write(f"Original expression: {parsed_expr}")

    # Initialize a list to store solving steps
    solving_steps = [parsed_expr]

    # Get the variables in the expression
    variables = list(parsed_expr.free_symbols)

    # Simplify the expression step by step for each variable
    for var in variables:
        simplified_expr = sym.simplify(parsed_expr, rational=True)
        solving_steps.append(simplified_expr)
        parsed_expr = simplified_expr

    # Display step-by-step solving
    st.write("Solving steps:")
    for i, step in enumerate(solving_steps):
        st.write(f"Step {i + 1}: {step}")

    st.write(f"Final simplified expression: {simplified_expr}")

except Exception as e:
    st.error("Invalid Expression")

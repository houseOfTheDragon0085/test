import streamlit as st
import sympy as sym
import re

st.title("Algebraic Expression Solver")

st.write("Enter a sentence or question with an algebraic expression following a colon (e.g., 'Please calculate: 2x + 3 = 8', 'Solve: 2x + 2x'):")

# User input for the sentence/question
user_input = st.text_input("Question:")

# Define symbolic variables
x, y = sym.symbols('x y')

try:
    # Use regular expressions to extract algebraic expressions following a colon
    matches = re.findall(r':\s*(\d*\.*\d*\s*[a-zA-Z]\s*[\+\-\*/\(\)\^=\s]*)+', user_input)

    if matches:
        # Combine the extracted matches to form an expression
        expression = " ".join(matches)

        # Remove the colon and leading white spaces
        expression = expression.lstrip(':').strip()

        # Replace '*' with Python-friendly multiplication symbol '**'
        expression = expression.replace('*', '**')

        # Parse the expression
        parsed_expr = sym.sympify(expression)
        simplified_expr = sym.simplify(parsed_expr)

        # Solve the expression
        solution = sym.solve(parsed_expr, (x, y))

        st.write(f"Original expression: {parsed_expr}")
        st.write(f"Simplified expression: {simplified_expr}")

        st.write("Solving steps:")
        for step in sym.solve(parsed_expr, (x, y), manual=True):
            st.write(step)

        st.write(f"Solution for x and y: {solution}")
    else:
        st.error("No algebraic expression found in the input.")
except Exception as e:
    st.error("Invalid Input")

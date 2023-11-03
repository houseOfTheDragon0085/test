import streamlit as st
import sympy as sym
import re

st.title("Algebraic Expression Solver")

st.write("Enter a sentence or question with an algebraic expression (e.g., 'Hi, can you solve 2x + 3 = 8', 'Calculate 2x + 2x'):")

# User input for the sentence/question
user_input = st.text_input("Question:")

# Define symbolic variables
x = sym.Symbol('x')

try:
    # Use regular expressions to extract algebraic expressions from user input
    matches = re.findall(r'(\d*\.*\d*\s*[a-zA-Z]\s*[\+\-\*/\(\)\^=\s]*)+', user_input)

    if matches:
        # Combine the extracted matches to form an expression
        expression = " ".join(matches)

        # Parse and solve the expression
        parsed_expr = sym.sympify(expression)
        simplified_expr = sym.simplify(parsed_expr)
        solution = sym.solve(simplified_expr, x)

        st.write(f"Original expression: {parsed_expr}")
        st.write(f"Simplified expression: {simplified_expr}")
        st.write(f"Solving steps:")
        for step in sym.steps(solution):
            st.write(step)
        st.write(f"Solution for x: {solution}")
    else:
        st.error("No algebraic expression found in the input.")
except Exception as e:
    st.error("Invalid Input")

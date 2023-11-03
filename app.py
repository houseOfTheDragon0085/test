import streamlit as st
import sympy as sym
import re

st.title("Algebraic Expression Solver")

st.write("Enter a sentence or question with an algebraic expression following a colon (e.g., 'Please calculate: 2x + 3 = 8', 'Solve: 2x + 2x'):")

# User input for the sentence/question
user_input = st.text_input("Question:")

# Define symbolic variables
x = sym.Symbol('x')

try:
    # Use regular expressions to extract algebraic expressions after a colon
    matches = re.findall(r':\s*(\d*\.*\d*\s*[a-zA-Z]\s*[\+\-\*/\(\)\^=\s]*)+', user_input)

    if matches:
        # Combine the extracted matches to form an expression
        expression = " ".join(matches)

        # Remove the colon and leading white spaces
        expression = expression.lstrip(':').strip()

        # Parse the expression
        parsed_expr = sym.sympify(expression)
        simplified_expr = sym.simplify(parsed_expr)

        st.write(f"Original expression: {parsed_expr}")
        st.write(f"Simplified expression: {simplified_expr}")

        # Solve the expression step by step
        solution_steps = []
        for step in sym.solve(parsed_expr, x, evaluate=False):
            solution_steps.append(step)

        st.write(f"Solving steps:")
        for i, step in enumerate(solution_steps):
            st.write(f"Step {i + 1}: {step}")

        # Find the final solution
        solution = sym.solve(parsed_expr, x)

        st.write(f"Solution for x: {solution}")
    else:
        st.error("No algebraic expression found in the input.")
except Exception as e:
    st.error("Invalid Input")

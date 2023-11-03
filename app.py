import streamlit as st
import sympy as sym
import pandas as pd

# Initialize a session_state variable to store chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title("Algebraic Expression Solver")

st.write("Enter an algebraic expression (e.g., 'x + y + x - y', '2x + 2x + 2y - y'):")

# User input for the expression
expression_input = st.text_input("User Input:", "Type an expression...")

# Define symbolic variables
x, y = sym.symbols('x y')

if expression_input:
    try:
        # Parse the expression
        parsed_expr = sym.sympify(expression_input)

        # Display the original expression
        st.write(f"User: {expression_input}")

        # Initialize a list to store solving steps
        solving_steps = [parsed_expr]

        # Simplify the expression step by step
        simplified_expr = parsed_expr
        while True:
            simplified = sym.simplify(simplified_expr)
            if simplified == simplified_expr:
                break  # No further simplification possible
            simplified_expr = simplified
            solving_steps.append(simplified_expr)

        # Display step-by-step solving
        st.write("Solving steps:")
        for i, step in enumerate(solving_steps):
            st.write(f"Step {i + 1}: {step}")

        st.write(f"Solver: {simplified_expr}")

        # Store the expression and the simplified result in chat history
        st.session_state.chat_history.append((expression_input, simplified_expr))

    except Exception as e:
        st.error("Invalid Expression")

# Display chat history as a table
st.write("Chat History:")

if st.session_state.chat_history:
    chat_df = pd.DataFrame(st.session_state.chat_history, columns=["User", "Solver"])
    st.dataframe(chat_df, use_container_width=True)

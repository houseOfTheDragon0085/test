import streamlit as st
import sympy as sym
from chatbot import chatbot  # Import your chatbot function

# Define symbolic variables
x = sym.Symbol('x')
y = sym.Symbol('y')

# Function to extract and solve algebraic expressions
def solve_algebraic_expression(expression):
    try:
        parsed_expr = sym.sympify(expression, evaluate=False)
        simplified_expr = sym.simplify(parsed_expr)
        return simplified_expr
    except Exception as e:
        return None

st.title("Algebraic Expression Solver with Chatbot")

st.write("Enter a chat message with an algebraic expression (e.g., 'Can you help me solve 2x + 2 = 4?'):")

# User input for the chat message
chat_input = st.text_input("Chatbot Message:")

if not chat_input:
    st.info("Please enter a chat message.")
else:
    # Check if the chat input contains a number
    if any(char.isdigit() for char in chat_input):
        # Extract and solve the algebraic expression
        simplified_expr = solve_algebraic_expression(chat_input)

        if simplified_expr:
            st.write(f"Algebraic Expression: {simplified_expr}")
            st.write(f"Solution: {simplified_expr}")
        else:
            st.error("Invalid Algebraic Expression")

    else:
        # If the chat input doesn't contain numbers, run the chatbot and fetch the reply
        st.info("Fetching chatbot reply...")
        chatbot_reply = chatbot(chat_input)
        st.write("Chatbot Reply:")
        st.write(chatbot_reply)

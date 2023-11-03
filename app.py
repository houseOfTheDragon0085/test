import streamlit as st
import sympy as sym
import spacy
import en_core_web_sm


# Load the spaCy NLP model
nlp = en_core_web_sm.load()

st.title("Algebraic Expression Solver")

st.write("Enter a sentence or question with an algebraic expression (e.g., 'Hi, can you solve 2x + 3 = 8', 'Calculate 2x + 2x'):")

# User input for the sentence/question
user_input = st.text_input("Question:")

# Define symbolic variables
x = sym.Symbol('x')

try:
    # Use spaCy to extract algebraic expressions from user input
    doc = nlp(user_input)

    # Initialize an empty list to collect extracted expressions
    expressions = []

    for token in doc:
        if token.pos_ == "SYM":
            # Collect symbols to form expressions
            expressions.append(str(token))

    if expressions:
        # Combine the collected symbols to form an expression
        expression = " ".join(expressions)

        # Parse and solve the expression
        parsed_expr = sym.sympify(expression)
        simplified_expr = sym.simplify(parsed_expr)

        st.write(f"Simplified expression: {simplified_expr}")
    else:
        st.error("No algebraic expression found in the input.")
except Exception as e:
    st.error("Invalid Input")

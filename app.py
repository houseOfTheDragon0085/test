import streamlit as st
from sympy import Eq, symbols, solve

st.title("Algebraic Equation Solver")

st.write("Enter an algebraic equation of the form 'ax = b', 'ax + b = c', or 'ax + bx = c':")

# User input for the equation
equation_input = st.text_input("Equation:", value="2x + 2 = 4")

# Parse the equation
parts = equation_input.split('=')
if len(parts) != 2:
    st.error("Invalid equation format. Please use 'ax = b', 'ax + b = c', or 'ax + bx = c'.")
else:
    left_part = parts[0].strip()
    right_part = parts[1].strip()

    # Define symbols
    x = symbols('x')
    
    try:
        if '+' in left_part:
            left_terms = left_part.split('+')
            if len(left_terms) == 2:
                a, b = [term.strip() for term in left_terms]
                equation = Eq(float(a) * x + float(b), float(right_part))
            else:
                st.error("Invalid equation format. Please use 'ax = b', 'ax + b = c', or 'ax + bx = c'.")
        elif left_part.count('x') == 1:
            a = left_part.replace('x', '').strip()
            equation = Eq(float(a) * x, float(right_part))
        else:
            st.error("Invalid equation format. Please use 'ax = b', 'ax + b = c', or 'ax + bx = c'.")
        
        if not st.session_state.get('eq') or st.session_state.eq != equation:
            st.session_state.eq = equation

        solution = solve(equation, x)
        st.write(f"Solutions for x: {solution}")
    except Exception as e:
        st.error("Invalid Equation")

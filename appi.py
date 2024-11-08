import streamlit as st
import streamlit.web.cli as stcli

# Set page title
st.title("My First Streamlit App")

# Text input
name = st.text_input("Enter your name:")

# Number input
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)

# Dropdown selection
favorite_color = st.selectbox("Choose your favorite color:", ["Red", "Green", "Blue", "Yellow"])

# Button
if st.button("Submit"):
    # Display results
    st.write(f"Hello, {name}!")
    st.write(f"Age: {age}")
    st.write(f"Favorite Color: {favorite_color}")

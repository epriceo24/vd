import streamlit as st

st.title("Will You Be My Valentine?")

# Function to handle user's response
def handle_response(response):
    # If the user types 'no', display an error message
    if response.lower() == 'yes':
        st.success("YIPPEEE Happy Valentine's Day! 💖")
    # If the user types anything else, display a positive response
    else:
        st.error("Error: Invalid response. Please type 'yes' to be my Valentine.")

# Ask the user if they want to be your Valentine
user_response = st.text_input("Will you be my Valentine? (Type 'yes' to accept)")

# If the user has responded, handle their response
if user_response:
    handle_response(user_response)
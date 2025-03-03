import streamlit as st
import random

# Custom CSS for styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #40E0D0
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .guess-box {
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #333;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and instructions
st.title("🎲 Number Guessing Game")
st.write("💡 Try to guess the randomly generated number between **1 and 100**!")
st.write("🔥 You have **7 attempts** to guess correctly!")

# Initialize session state variables
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0  # Attempt counter

# Get user input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Button to check guess
if st.button("Submit Guess"):
    if st.session_state.attempts < 6:  # Allow 7 attempts (0 to 6)
        st.session_state.attempts += 1
        if guess < st.session_state.secret_number:
            st.warning(f"📉 Too low! Attempts left: {7 - st.session_state.attempts}")
        elif guess > st.session_state.secret_number:
            st.warning(f"📈 Too high! Attempts left: {7 - st.session_state.attempts}")
        else:
            st.success("🎉 Congratulations! You guessed the correct number!")
            st.balloons()
            # Reset game
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
    else:
        st.error("❌ Game Over! You've used all 7 attempts. The game will restart.")
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0


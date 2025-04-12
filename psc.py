import streamlit as st
import re

st.title("🔒 Password Strength Checker")
st.markdown("---")
st.markdown("### Check how strong your password is!")
st.write("Enter a password and see if it's weak, medium, or strong.")

# Password input from user
password = st.text_input("Enter your password", type="password")

def check_password_strength(password):
    # Initial score and feedback
    score = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    elif len(password) >= 8 and len(password) < 12:
        score += 1
        feedback.append("Good length (8+ characters).")
    else:
        score += 2
        feedback.append("Great length (12+ characters)!")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("Contains uppercase letters.")
    else:
        feedback.append("Add uppercase letters (A-Z).")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("Contains lowercase letters.")
    else:
        feedback.append("Add lowercase letters (a-z).")

    # Check for numbers
    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("Contains numbers.")
    else:
        feedback.append("Add numbers (0-9).")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("Contains special characters.")
    else:
        feedback.append("Add special characters (e.g., !@#$%^&*).")

    # Determine strength based on score
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, score, feedback, color

# Check button
if st.button("Check Strength"):
    if password:
        strength, score, feedback, color = check_password_strength(password)
        st.markdown(f"**Password Strength:** <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)
        st.write(f"**Score:** {score}/6")
        st.write("**Feedback:**")
        for line in feedback:
            st.write(f"- {line}")
    else:
        st.error("Please enter a password first!")
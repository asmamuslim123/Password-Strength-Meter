import streamlit as st
import re
import random
import string

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[@$!%*?&]", password) is None
    
    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
    strength = "Weak"
    color = "#FF4B4B"
    suggestions = []
    
    if length_error:
        suggestions.append("Increase the length to at least 8 characters.")
    if digit_error:
        suggestions.append("Add at least one numeric digit (0-9).")
    if uppercase_error:
        suggestions.append("Include at least one uppercase letter (A-Z).")
    if lowercase_error:
        suggestions.append("Include at least one lowercase letter (a-z).")
    if special_char_error:
        suggestions.append("Use at least one special character (@$!%*?&).")
    
    if sum(errors) == 0:
        strength = "Strong"
        color = "#4CAF50"
    elif sum(errors) <= 2:
        strength = "Medium"
        color = "#FF9800"
    
    return strength, color, suggestions

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "@$!%*?&"
    strong_password = ''.join(random.choice(characters) for _ in range(length))
    return strong_password

# Streamlit App Design
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #2B2B3A;
            color: white;
            font-family: Arial, sans-serif;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
            border: 2px solid #4CAF50;
            padding: 12px;
            font-size: 18px;
            background-color:rgb(217, 217, 241);
            color: white;
        }
        .strength-indicator {
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-top: 10px;
        }
        .suggestions {
            font-size: 16px;
            color: #FFC107;
            margin-top: 10px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 12px;
            font-size: 16px;
            font-weight: bold;
            border: none;
        }
        .stButton>button:hover {
            background-color: #45A049;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its strength.")

password = st.text_input("Enter Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")
passwords_match = password and confirm_password and password == confirm_password

if password and confirm_password:
    if passwords_match:
        strength, color, suggestions = check_password_strength(password)
        st.markdown(f"""<p class='strength-indicator' style='color: {color};'>🔒 Password Strength: {strength}</p>""", unsafe_allow_html=True)
        
        if strength == "Strong":
            st.success("✅ Your password is strong!")
        else:
            st.warning("⚠️ Your password is weak. Consider improving it.")
            
        if suggestions:
            st.write("🔎 Suggestions to improve your password:")
            for suggestion in suggestions:
                st.markdown(f"- {suggestion}")
    else:
        st.markdown("<p style='color: #FF4B4B; font-weight: bold;'>❌ Passwords do not match! Please enter the same password.</p>", unsafe_allow_html=True)

if passwords_match:
    if st.button("Generate Strong Password"):
        strong_password = generate_strong_password()
        st.text(f"🔑 Strong Password: {strong_password}")

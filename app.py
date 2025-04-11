import streamlit as st
import re

st.set_page_config(page_title="Password strength checker")

st.title("🔐Password Strength Checker")
st.markdown("""
## Welcome to the ultimate password strength checker! 👋  
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.  
We will give you helpful tips to create a **Strong Password** 🔒
""")

password = st.text_input("Enter your password", type="password")

if st.button("Check Password"):
    feedback = []
    score = 0

    if password:
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ Password should be at least 8 characters long.")

        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("❌ Password should contain both upper and lower case characters.")

        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("❌ Password should contain at least one digit.")

        if re.search(r'[!@#$%^&*]', password):
            score += 1
        else:
            feedback.append("❌ Password should contain at least one special character (!@#$%^&*).")

        # Final feedback based on score
        if score == 4:
            st.success("☑️ Your password is strong! 🎉")
        elif score == 3:
            st.warning("🟡 Your password is medium strength. It could be stronger.")
        else:
            st.error("🔴 Your password is weak. Please make it stronger.")

        if feedback:
            st.markdown("## Improvement Suggestions")
            for tip in feedback:
                st.write(tip)
    else:
        st.info("Please enter a password before checking.")

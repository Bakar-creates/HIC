import streamlit as st
import json
from github import Github
from pathlib import Path
import bcrypt
import streamlit_authenticator as stauth

# Streamlit App Configuration
st.set_page_config(page_title="Blood Bank Finder", page_icon="🩸", layout="centered")

# GitHub Repo Configuration
GITHUB_TOKEN = "your_github_personal_access_token"  # Replace with your PAT
GITHUB_REPO = "your_username/your_repo_name"  # Replace with your repository
GITHUB_FILE = "users.json"  # File to store user data

# Connect to GitHub
g = Github(GITHUB_TOKEN)
repo = g.get_repo(GITHUB_REPO)

# Fetch or Create User Data File in the GitHub Repo
try:
    content = repo.get_contents(GITHUB_FILE)
    users_data = json.loads(content.decoded_content.decode())
except Exception as e:
    users_data = {"users": []}  # Initialize empty user list if file doesn't exist

# Function to Save Users to GitHub
def save_users_to_github(data):
    try:
        content = repo.get_contents(GITHUB_FILE)
        repo.update_file(GITHUB_FILE, "Update user data", json.dumps(data), content.sha)
    except Exception as e:
        repo.create_file(GITHUB_FILE, "Create user data", json.dumps(data))

# Login/Signup System
def main():
    st.title("🩸 Blood Bank Finder")
    st.sidebar.title("Login/Signup")

    menu = st.sidebar.selectbox("Menu", ["Login", "Sign Up"])

    if menu == "Login":
        st.sidebar.subheader("Login")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        login_button = st.sidebar.button("Login")

        if login_button:
            for user in users_data["users"]:
                if user["username"] == username and bcrypt.checkpw(password.encode(), user["password"].encode()):
                    st.success(f"Welcome back, {username}!")
                    show_blood_bank_app()
                    return
            st.error("Invalid username or password.")

    elif menu == "Sign Up":
        st.sidebar.subheader("Sign Up")
        new_username = st.sidebar.text_input("Create a Username")
        new_password = st.sidebar.text_input("Create a Password", type="password")
        confirm_password = st.sidebar.text_input("Confirm Password", type="password")
        signup_button = st.sidebar.button("Sign Up")

        if signup_button:
            if new_password == confirm_password:
                hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()
                users_data["users"].append({"username": new_username, "password": hashed_password})
                save_users_to_github(users_data)
                st.success("Account created successfully! Please log in.")
            else:
                st.error("Passwords do not match.")

def show_blood_bank_app():
    st.markdown("""
    Welcome to the **Blood Bank Finder** app! Use the filters to find the nearest blood banks in Karachi.
    """)

# Run the app
if __name__ == "__main__":
    main()

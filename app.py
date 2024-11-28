import streamlit as st
import pandas as pd
from time import sleep
import hashlib
import os
import re

# Helper function for password hashing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Validate email format
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Validate password strength
def is_strong_password(password):
    return len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password)

# Dummy blood bank data
blood_banks = [
    {"Name": "City Blood Bank", "Location": "Shahrah-e-Faisal, Karachi", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-300-1234567", "Available Blood Groups": "A+, A-, O+, O-, B+", "Website": "https://citybloodbank.com"},
    {"Name": "Safe Blood Bank", "Location": "North Nazimabad, Karachi", "Timings": "24/7", "Contact": "+92-300-7654321", "Available Blood Groups": "B+, B-, AB+, O+, O-", "Website": "https://safebloodbank.com"},
    {"Name": "National Blood Center", "Location": "Clifton, Karachi", "Timings": "10:00 AM - 8:00 PM", "Contact": "+92-21-3456789", "Available Blood Groups": "A+, AB-, O-, O+", "Website": "https://nationalbloodcenter.com"},
    {"Name": "Karachi Blood Bank", "Location": "Korangi, Karachi", "Timings": "8:00 AM - 6:00 PM", "Contact": "+92-300-4567890", "Available Blood Groups": "A+, B-, O+, O-", "Website": "https://karachibloodbank.com"},
    {"Name": "Lifesaver Blood Bank", "Location": "Gulshan-e-Iqbal, Karachi", "Timings": "9:00 AM - 10:00 PM", "Contact": "+92-300-6789012", "Available Blood Groups": "O+, AB-, A-, O-", "Website": "https://lifesaverbloodbank.com"},
]

# Convert data to DataFrame for manipulation
df = pd.DataFrame(blood_banks)

# Debugging: Check DataFrame structure
st.write("DataFrame structure:")
st.write(df)

# Check if the "Location" column exists
if "Location" in df.columns:
    # Extract unique areas for dropdown
    df["Location"] = df["Location"].fillna("Unknown")  # Handle missing values in 'Location'
    areas = sorted(df['Location'].apply(lambda x: x.split(',')[0]).unique())
else:
    st.error("The 'Location' column is missing in the dataset.")
    areas = ["Unknown"]  # Fallback value if 'Location' is missing

# Load user data
user_data_file = "user_data.csv"
if not os.path.exists(user_data_file):
    pd.DataFrame(columns=["Email", "Password", "Contact", "Blood Group"]).to_csv(user_data_file, index=False)
users_df = pd.read_csv(user_data_file)

# Cache blood bank data for performance
@st.cache
def get_blood_banks():
    return df

# Streamlit App Configuration
st.set_page_config(page_title="Blood Bank Finder", page_icon="🩸", layout="centered")

# Title and Introduction
st.markdown("<h1 class='title'>🩸 Blood Bank Finder 🩸</h1>", unsafe_allow_html=True)

# Sidebar for Login/Signup
def show_login_signup():
    global users_df
    auth_option = st.sidebar.radio("Choose an option:", ["Login", "Sign Up"])

    if auth_option == "Sign Up":
        st.subheader("Create an Account")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        contact = st.text_input("Contact Number")
        blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])

        if st.button("Sign Up"):
            if not email or not password or not contact or not blood_group:
                st.error("Please fill in all fields.")
            elif not is_valid_email(email):
                st.error("Invalid email format. Please use a valid email.")
            elif not is_strong_password(password):
                st.error("Password must be at least 8 characters long and include letters and numbers.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            elif email in users_df["Email"].values:
                st.error("Email already exists. Please login instead.")
            else:
                new_user = pd.DataFrame({
                    "Email": [email],
                    "Password": [hash_password(password)],
                    "Contact": [contact],
                    "Blood Group": [blood_group]
                })
                users_df = pd.concat([users_df, new_user], ignore_index=True)
                users_df.to_csv(user_data_file, index=False)
                st.success("Account created successfully! Please log in.")

    elif auth_option == "Login":
        st.subheader("Login to Your Account")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            hashed_password = hash_password(password)
            user = users_df[(users_df["Email"] == email) & (users_df["Password"] == hashed_password)]

            if not user.empty:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.session_state.user_contact = user.iloc[0]["Contact"]
                st.session_state.user_blood_group = user.iloc[0]["Blood Group"]
                st.success(f"Welcome, {email}!")
            else:
                st.error("Incorrect email or password. Please try again.")

# Blood Bank Finder
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    show_login_signup()
else:
    st.markdown("Welcome to the **Blood Bank Finder** app!")

    if st.button("Logout"):
        st.session_state.clear()
        st.experimental_rerun()

    st.subheader("📍 Search by Area")
    selected_area = st.selectbox("Select an Area:", ["All"] + areas, index=0)

    st.subheader("🔍 Search for a Specific Blood Group")
    blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    selected_blood_group = st.selectbox("Choose a Blood Group:", ["All"] + blood_groups, index=0)

    if st.button("Clear Filters"):
        st.experimental_rerun()

    with st.spinner('Filtering the blood banks...'):
        sleep(1)
        data = get_blood_banks()

        if selected_blood_group != "All":
            data = data[data["Available Blood Groups"].str.contains(selected_blood_group, case=False)]
        if selected_area != "All":
            data = data[data["Location"].str.contains(selected_area, case=False)]

    if not data.empty:
        st.markdown("### Blood Bank Details:")
        for _, blood_bank in data.iterrows():
            st.markdown(f"""
            <div>
                <h3>{blood_bank['Name']}</h3>
                <p><strong>Location:</strong> {blood_bank['Location']}</p>
                <p><strong>Timings:</strong> {blood_bank['Timings']}</p>
                <p><strong>Available Blood Groups:</strong> {blood_bank['Available Blood Groups']}</p>
                <p><strong>Contact:</strong> {blood_bank['Contact']}</p>
                <p><strong>Website:</strong> <a href="{blood_bank['Website']}" target="_blank">Visit Website</a></p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No results found based on the selected filters.")

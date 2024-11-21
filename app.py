import streamlit as st
import pandas as pd
from time import sleep
import hashlib
import os

# Helper function for password hashing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Dummy blood bank data with more entries and details
blood_banks = [
    {"Name": "City Blood Bank", "Location": "Shahrah-e-Faisal, Karachi", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-300-1234567", "Available Blood Groups": "A+, A-, O+, O-, B+", "Website": "https://citybloodbank.com"},
    {"Name": "Safe Blood Bank", "Location": "North Nazimabad, Karachi", "Timings": "24/7", "Contact": "+92-300-7654321", "Available Blood Groups": "B+, B-, AB+, O+, O-", "Website": "https://safebloodbank.com"},
    {"Name": "National Blood Center", "Location": "Clifton, Karachi", "Timings": "10:00 AM - 8:00 PM", "Contact": "+92-21-3456789", "Available Blood Groups": "A+, AB-, O-, O+", "Website": "https://nationalbloodcenter.com"},
    {"Name": "Karachi Blood Bank", "Location": "Korangi, Karachi", "Timings": "8:00 AM - 6:00 PM", "Contact": "+92-300-4567890", "Available Blood Groups": "A+, B-, O+, O-", "Website": "https://karachibloodbank.com"},
    {"Name": "Lifesaver Blood Bank", "Location": "Gulshan-e-Iqbal, Karachi", "Timings": "9:00 AM - 10:00 PM", "Contact": "+92-300-6789012", "Available Blood Groups": "O+, AB-, A-, O-", "Website": "https://lifesaverbloodbank.com"},
    {"Name": "Hope Blood Bank", "Location": "F.B Area, Karachi", "Timings": "24/7", "Contact": "+92-300-2345678", "Available Blood Groups": "B+, AB+, O+, O-", "Website": "https://hopebloodbank.com"},
    {"Name": "Red Crescent Blood Bank", "Location": "Karachi Cantt, Karachi", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-300-9988776", "Available Blood Groups": "A-, AB-, O+, O-", "Website": "https://redcrescentbloodbank.com"},
    {"Name": "Miracle Blood Bank", "Location": "Saddar, Karachi", "Timings": "10:00 AM - 6:00 PM", "Contact": "+92-300-1122334", "Available Blood Groups": "A+, B+, O-, O+", "Website": "https://miraclebloodbank.com"}
]

# Convert the data to a DataFrame for easier manipulation
df = pd.DataFrame(blood_banks)

# Extract unique areas from the "Location" column (only Karachi areas)
areas = sorted(df['Location'].apply(lambda x: x.split(',')[0]).unique())

# Load user data (or create a new one if file doesn't exist)
user_data_file = "user_data.csv"
if not os.path.exists(user_data_file):
    pd.DataFrame(columns=["Email", "Password", "Contact", "Blood Group"]).to_csv(user_data_file, index=False)

# Load user data into a DataFrame
users_df = pd.read_csv(user_data_file)

# Streamlit App Configuration
st.set_page_config(page_title="Blood Bank Finder", page_icon="🩸", layout="centered")

# Title and Introduction
st.markdown("<h1 class='title'>🩸 Blood Bank Finder 🩸</h1>", unsafe_allow_html=True)

# Function to handle login/signup interface
def show_login_signup():
    global users_df  # Add this line to reference the global users_df variable

    auth_option = st.sidebar.radio("Choose an option:", ["Login", "Sign Up"])

    # Signup Page
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
            elif password != confirm_password:
                st.error("Passwords do not match.")
            elif email in users_df["Email"].values:
                st.error("Email already exists. Please login instead.")
            elif not email.endswith("@bbf.com"):
                st.error("Email must end with '@bbf.com'.")
            else:
                # Add new user to the DataFrame and save
                new_user = pd.DataFrame({
                    "Email": [email],
                    "Password": [hash_password(password)],
                    "Contact": [contact],
                    "Blood Group": [blood_group]
                })
                users_df = pd.concat([users_df, new_user], ignore_index=True)
                users_df.to_csv(user_data_file, index=False)
                st.success("Account created successfully! Please log in.")

    # Login Page
    elif auth_option == "Login":
        st.subheader("Login to Your Account")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            # Authenticate user
            hashed_password = hash_password(password)
            user = users_df[(users_df["Email"] == email) & (users_df["Password"] == hashed_password)]

            if not user.empty:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.session_state.user_contact = user.iloc[0]["Contact"]
                st.session_state.user_blood_group = user.iloc[0]["Blood Group"]
                st.success(f"Welcome, {email}!")
            else:
                st.error("Invalid email or password. Please try again or sign up.")


# Blood Bank Finder (only for logged-in users)
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    show_login_signup()  # Show login/signup if not logged in
else:
    # Blood Bank Finder will only be displayed after login
    st.markdown("""Welcome to the **Blood Bank Finder** app! Find the nearest blood banks in Karachi, their timings, and available blood groups.""")

    # Add a prominent logout button at the top for easy logout
    if st.button("Logout"):
        st.session_state.clear()  # Clear the session state
        st.experimental_rerun()  # Rerun the app to show login/signup interface

    # Add search placeholder texts
    st.subheader("📍 Search by Area")
    selected_area = st.selectbox("Select an Area:", ["All"] + areas, help="Select an area to filter blood banks.", index=0)

    st.subheader("🔍 Search for a Specific Blood Group")
    blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    selected_blood_group = st.selectbox("Choose a Blood Group:", ["All"] + blood_groups, help="Select a blood group to filter the available blood banks.", index=0)

    # Adding a loading spinner for a better user experience
    with st.spinner('Filtering the blood banks...'):
        sleep(1)  # Simulate a loading process

    # Filter the data based on selected criteria
    if selected_blood_group != "All":
        filtered_by_group = df[df["Available Blood Groups"].str.contains(selected_blood_group, case=False)]
    else:
        filtered_by_group = df

    if selected_area != "All":
        filtered_data = filtered_by_group[filtered_by_group["Location"].str.contains(selected_area, case=False)]
    else:
        filtered_data = filtered_by_group

    # Display results with card-style layout
    if selected_area != "All" or selected_blood_group != "All":  # Show results only when filters are applied
        if not filtered_data.empty:
            st.markdown("### Blood Bank Details:")

            for idx, blood_bank in filtered_data.iterrows():
                st.markdown(f"""
                <div class="card">
                    <div>
                        <h3>{blood_bank['Name']}</h3>
                        <p><strong>Location:</strong> {blood_bank['Location']}</p>
                        <p><strong>Timings:</strong> {blood_bank['Timings']}</p>
                        <p><strong>Available Blood Groups:</strong> {blood_bank['Available Blood Groups']}</p>
                        <p><strong>Contact:</strong> {blood_bank['Contact']}</p>
                        <p><strong>Website:</strong> <a href="{blood_bank['Website']}" target="_blank">Visit Website</a></p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.write("No results found based on the selected filters. Please try different options.")
    else:
        st.write("Please select a filter to view the blood bank details.")

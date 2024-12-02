import streamlit as st
import pandas as pd
from time import sleep
import re


# Sample data for validation
valid_emails = ["user1@bbfk.com", "user2@bbfk.com"]

def login():
    email = st.text_input("Enter your email:")
    password = st.text_input("Enter your password:", type="password")
    
    if email and "@bbfk.com" not in email:
        st.error("Please enter a valid email address with @bbfk.com domain.")
    
    if st.button("Login"):
        if email in valid_emails and password == "correctpassword":  # Replace with actual validation logic
            st.success("Login successful!")
        else:
            st.error("Invalid email or password.")
            st.experimental_rerun()

login()

# Sample Data for Blood Banks (same as your original list)
karachi_blood_banks = [
    {"Name": "City Blood Bank", "City": "Karachi", "Location": "Shahrah-e-Faisal", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-300-1234567", "Available Blood Groups": "A+, A-, O+, O-, B+", "Website": "https://citybloodbank.com"},
    {"Name": "Dow Blood Bank", "City": "Karachi", "Location": "Gulshan-e-Iqbal", "Timings": "24/7", "Contact": "+92-321-9876543", "Available Blood Groups": "A+, AB-, O+", "Website": "https://dowbloodbank.com"},
    # Add other blood banks here...
]

# Convert data to DataFrame
df = pd.DataFrame(karachi_blood_banks)

# Cache blood bank data
@st.cache_data
def get_blood_banks():
    return df

# Function to validate email with @bbfk.com
def validate_email(email):
    if re.match(r"^[a-zA-Z0-9_.+-]+@bbfk\.com$", email):
        return True
    return False

# App configuration
st.set_page_config(page_title="Blood Bank Finder Karachi", page_icon="🩸", layout="centered")

# Custom CSS for styling
st.markdown("""
   <style>
    .stApp {
        background: linear-gradient(to bottom right, #e0f7fa, #fff8e1);
        color: #333;
    }

    .header {
        text-align: center;
        background: linear-gradient(to right, #007bff, #00bcd4);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        font-family: 'Poppins', sans-serif;
    }

    .header h1 {
        font-size: calc(1.5em + 2vw);  /* Responsive font size */
        word-wrap: break-word;
    }

    .header p {
        font-size: 1.2em;
        font-weight: 300;
    }

    .login-signup-card {
        background: linear-gradient(to bottom, #ffffff, #e0f7fa);
        padding: 30px;
        margin: 20px 0;
        border-radius: 15px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }

    .login-signup-card:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    }

    .input-field {
        padding: 10px;
        margin: 10px 0;
        border-radius: 10px;
        border: 1px solid #007bff;
        background-color: #f0f9ff;
        width: 100%;
    }

    .input-field:focus {
        border-color: #0a74da;
        outline: none;
    }

    .login-btn, .signup-btn {
        padding: 10px 20px;
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
        width: 100%;
    }

    .login-btn:hover, .signup-btn:hover {
        background-color: #0056b3;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class="header">
        <h1>Blood Bank Finder Karachi</h1>
        <p>Find blood banks near you with ease in Karachi.</p>
    </div>
""", unsafe_allow_html=True)

# Signup/Login Form
st.subheader("👤 Login or Signup")

# User selection: Login or Signup
auth_choice = st.selectbox("Choose an option", ["Login", "Signup"], index=0)

if auth_choice == "Login":
    # Login form
    email = st.text_input("Enter your email address", key="login_email")
    password = st.text_input("Enter your password", type="password", key="login_password")

    if st.button("Login", key="login_btn"):
        if not validate_email(email):
            st.error("Please enter a valid email address ending with '@bbfk.com'.")
        elif password == "":
            st.error("Password cannot be empty.")
        else:
            st.success("Logged in successfully!")
            # Proceed to next steps after login (for example, showing blood bank list)
            st.experimental_rerun()

elif auth_choice == "Signup":
    # Signup form
    email = st.text_input("Enter your email address", key="signup_email")
    password = st.text_input("Enter your password", type="password", key="signup_password")
    confirm_password = st.text_input("Confirm your password", type="password", key="confirm_signup_password")

    if st.button("Signup", key="signup_btn"):
        if not validate_email(email):
            st.error("Please enter a valid email address ending with '@bbfk.com'.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        elif password == "":
            st.error("Password cannot be empty.")
        else:
            st.success("Signup successful! Please login to continue.")
            # Proceed to login after successful signup (or automatic login in real-world apps)
            st.experimental_rerun()

# Display Blood Bank Finder after login/signup
if email and password and validate_email(email):
    st.markdown("""
    <div class="filter-section">
        <h3>📍 Search by Area</h3>
        """, unsafe_allow_html=True)

    # Area Selection
    filtered_areas = sorted(df["Location"].unique())
    selected_area = st.selectbox("Select an Area:", ["All"] + filtered_areas, index=0)

    # Blood Group Selection
    st.subheader("🔍 Search by Blood Group")
    blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    selected_blood_group = st.selectbox("Choose a Blood Group:", ["All"] + blood_groups, index=0)

    st.markdown('</div>', unsafe_allow_html=True)

    # Filter and Display Results
    with st.spinner('Filtering blood banks...'):
        sleep(1)
        data = get_blood_banks()

        if selected_area != "All":
            data = data[data["Location"] == selected_area]
        if selected_blood_group != "All":
            data = data[data["Available Blood Groups"].str.contains(selected_blood_group, case=False, na=False)]

        if not data.empty:
            st.markdown("### Blood Bank Details:")
            for _, blood_bank in data.iterrows():
                st.markdown(f"""
                <div class="card">
                    <h3>{blood_bank['Name']}</h3>
                    <p><strong>Location:</strong> {blood_bank['Location']}</p>
                    <p><strong>Timings:</strong> {blood_bank['Timings']}</p>
                    <p><strong>Available Blood Groups:</strong> {blood_bank['Available Blood Groups']}</p>
                    <p><strong>Contact:</strong> {blood_bank['Contact']}</p>
                    <a class="visit-button" href="{blood_bank['Website']}" target="_blank">Visit Website</a>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No results found for the selected filters.")

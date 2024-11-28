import streamlit as st
import pandas as pd
from time import sleep

# Expanded blood bank data with more blood banks and Karachi areas
blood_banks = [
    {"Name": "City Blood Bank", "Location": "Shahrah-e-Faisal, Karachi", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-300-1234567", "Available Blood Groups": "A+, A-, O+, O-, B+", "Website": "https://citybloodbank.com"},
    {"Name": "Dow Blood Bank", "Location": "Gulshan, Karachi", "Timings": "24/7", "Contact": "+92-321-9876543", "Available Blood Groups": "A+, AB-, O+", "Website": "https://dowbloodbank.com"},
    {"Name": "Punjab Blood Bank", "Location": "Model Town, Lahore", "Timings": "8:00 AM - 8:00 PM", "Contact": "+92-322-5556789", "Available Blood Groups": "O+, O-", "Website": "https://punjabbloodbank.com"},
    {"Name": "Karachi Blood Bank", "Location": "Korangi, Karachi", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-300-6781234", "Available Blood Groups": "A+, O+, B+", "Website": "https://karachibloodbank.com"},
    {"Name": "Northern Blood Bank", "Location": "North Nazimabad, Karachi", "Timings": "24/7", "Contact": "+92-323-1234567", "Available Blood Groups": "AB-, A-, O+", "Website": "https://northernbloodbank.com"},
    {"Name": "Sindh Blood Bank", "Location": "Clifton, Karachi", "Timings": "8:00 AM - 8:00 PM", "Contact": "+92-324-9876543", "Available Blood Groups": "A-, O-, B+", "Website": "https://sindhbloodbank.com"},
    {"Name": "Jinnah Blood Bank", "Location": "Jamshed Road, Karachi", "Timings": "9:00 AM - 6:00 PM", "Contact": "+92-331-2345678", "Available Blood Groups": "B-, AB+, O+", "Website": "https://jinnahbloodbank.com"}
]

# Convert data to DataFrame for manipulation
df = pd.DataFrame(blood_banks)

# Verify the 'Location' column exists and handle missing or invalid data
if "Location" in df.columns:
    df["Location"] = df["Location"].fillna("Unknown")  # Fill missing values with "Unknown"
    areas = sorted(df["Location"].apply(lambda x: x.split(",")[0]).unique())
else:
    st.warning("The 'Location' column is missing in the dataset.")
    areas = []

# Cache blood bank data for performance
@st.cache
def get_blood_banks():
    return df

# Streamlit App Configuration
st.set_page_config(page_title="Blood Bank Finder", page_icon="🩸", layout="centered")

# Title and Introduction
st.markdown("<h1 class='title'>🩸 Blood Bank Finder 🩸</h1>", unsafe_allow_html=True)

# Style for the blood bank cards with background image
st.markdown("""
    <style>
        /* Background Image */
        body {
            background-image: url('https://raw.githubusercontent.com/Bakar-creates/HIC/main/assets/background-image.jpg');  /* Your raw GitHub URL */
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        /* Style for the blood bank cards */
        .blood-bank-card {
            background-color: cyan;  /* Cyan background for the cards */
            padding: 20px;
            margin: 10px 0;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        /* Improved styling for readability */
        .blood-bank-card h3 {
            color: #2c3e50;
            font-size: 22px;
            margin-bottom: 10px;
        }
        .blood-bank-card p {
            color: #34495e;
            font-size: 18px;
            line-height: 1.6;
            margin-bottom: 8px;
        }
        .blood-bank-card a {
            color: #3498db;
            text-decoration: none;
            font-weight: bold;
        }
        .blood-bank-card a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# Blood Bank Finder
st.markdown("Welcome to the **Blood Bank Finder** app!")

# Search by Area
st.subheader("📍 Search by Area")
selected_area = st.selectbox("Select an Area:", ["All"] + areas, index=0)

# Search for a Specific Blood Group
st.subheader("🔍 Search for a Specific Blood Group")
blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
selected_blood_group = st.selectbox("Choose a Blood Group:", ["All"] + blood_groups, index=0)

with st.spinner('Filtering the blood banks...'):
    sleep(1)
    data = get_blood_banks()

    if selected_blood_group != "All":
        data = data[data["Available Blood Groups"].str.contains(selected_blood_group, case=False)]
    if selected_area != "All":
        data = data[data["Location"].str.contains(selected_area, case=False)]

# Display blood bank details only if the filters match
if selected_area != "All" or selected_blood_group != "All":
    if not data.empty:
        st.markdown("### Blood Bank Details:")
        for _, blood_bank in data.iterrows():
            st.markdown(f"""
            <div class="blood-bank-card">
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
else:
    st.warning("Please select a filter to search for blood banks.")

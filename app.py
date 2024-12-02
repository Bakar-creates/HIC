import streamlit as st
import pandas as pd
from time import sleep

# Expanded blood bank data for Karachi
karachi_blood_banks = [
    {"Name": "City Blood Bank", "City": "Karachi", "Location": "Shahrah-e-Faisal", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-300-1234567", "Available Blood Groups": "A+, A-, O+, O-, B+", "Website": "https://citybloodbank.com"},
    {"Name": "Dow Blood Bank", "City": "Karachi", "Location": "Gulshan-e-Iqbal", "Timings": "24/7", "Contact": "+92-321-9876543", "Available Blood Groups": "A+, AB-, O+", "Website": "https://dowbloodbank.com"},
    # More blood banks...
]

# Convert data to DataFrame
df = pd.DataFrame(karachi_blood_banks)

# Cache blood bank data
@st.cache_data
def get_blood_banks():
    return df

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

        .filter-section {
            background-color: #f5f5f5;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .filter-section select {
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #007bff;
            background-color: #ffffff;
        }

        .filter-section select:focus {
            border-color: #00bcd4;
            outline: none;
            box-shadow: 0 4px 10px rgba(0, 188, 212, 0.3);
        }

        .card {
            background: linear-gradient(to bottom, #ffffff, #e0f7fa);
            padding: 20px;
            margin: 10px 0;
            border-radius: 15px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }

        .visit-button {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #003366;  /* Dark Blue */
            color: white;
            text-decoration: none;
            border-radius: 8px;
            transition: background-color 0.3s ease;
        }

        .visit-button:hover {
            background-color: #002244;  /* Darker Blue on hover */
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class="header">
        <h1>🩸 Blood Bank Finder Karachi 🩸</h1>
        <p>Find blood banks near you with ease in Karachi.</p>
    </div>
""", unsafe_allow_html=True)

# Filter Section
st.markdown('<div class="filter-section">', unsafe_allow_html=True)

# Area Selection
st.subheader("📍 Search by Area")
filtered_areas = sorted(df["Location"].unique())
selected_area = st.selectbox("Select an Area:", ["All"] + filtered_areas, index=0)

# Blood Group Selection
st.subheader("🔍 Search by Blood Group")
blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]  # Example blood groups
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

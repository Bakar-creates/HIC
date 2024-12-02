import streamlit as st
import pandas as pd
from time import sleep

# Expanded blood bank data across Pakistan
blood_banks = [
    {"Name": "City Blood Bank", "City": "Karachi", "Location": "Shahrah-e-Faisal", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-300-1234567", "Available Blood Groups": "A+, A-, O+, O-, B+", "Website": "https://citybloodbank.com"},
    {"Name": "Dow Blood Bank", "City": "Karachi", "Location": "Gulshan", "Timings": "24/7", "Contact": "+92-321-9876543", "Available Blood Groups": "A+, AB-, O+", "Website": "https://dowbloodbank.com"},
    {"Name": "Punjab Blood Bank", "City": "Lahore", "Location": "Model Town", "Timings": "8:00 AM - 8:00 PM", "Contact": "+92-322-5556789", "Available Blood Groups": "O+, O-", "Website": "https://punjabbloodbank.com"},
    {"Name": "Abbottabad Blood Bank", "City": "Abbottabad", "Location": "Mansehra Road", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-335-9876543", "Available Blood Groups": "A-, B+", "Website": "https://abbottabadbloodbank.com"},
    # Add additional entries as needed
]

# Convert data to DataFrame
df = pd.DataFrame(blood_banks)

# Cache blood bank data
@st.cache_data
def get_blood_banks():
    return df

# App configuration
st.set_page_config(page_title="Blood Bank Finder Pakistan", page_icon="🩸", layout="centered")

# Add custom CSS for styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Roboto:wght@300;400&display=swap');
        :root {
            --primary-color: #007bff;
            --background-light: #ffffff;
            --background-dark: #333333;
            --text-light: #333333;
            --text-dark: #ffffff;
            --card-light: #e0f7fa;
            --card-dark: #444444;
            --shadow-light: rgba(0, 0, 0, 0.1);
            --shadow-dark: rgba(255, 255, 255, 0.1);
        }
        html[data-theme="light"] {
            --background-color: var(--background-light);
            --text-color: var(--text-light);
            --card-color: var(--card-light);
            --shadow-color: var(--shadow-light);
        }
        html[data-theme="dark"] {
            --background-color: var(--background-dark);
            --text-color: var(--text-dark);
            --card-color: var(--card-dark);
            --shadow-color: var(--shadow-dark);
        }
        body {
            background-color: var(--background-color);
            color: var(--text-color);
            font-family: 'Roboto', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 2.5em;
            font-weight: 600;
            margin-bottom: 20px;
            color: var(--primary-color);
            font-family: 'Poppins', sans-serif;
        }
        .card {
            background-color: var(--card-color);
            padding: 20px;
            margin: 10px 0;
            border-radius: 12px;
            box-shadow: 0 6px 12px var(--shadow-color);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 16px var(--shadow-color);
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown('<div class="title">🩸 Blood Bank Finder Pakistan 🩸</div>', unsafe_allow_html=True)

# Extract unique cities
cities = sorted(df["City"].unique())

# City filter
st.subheader("📍 Search by City")
selected_city = st.selectbox("Select a City:", ["All"] + cities, index=0)

# Area filter
st.subheader("📍 Search by Area")
if selected_city != "All":
    filtered_df = df[df["City"] == selected_city]
    filtered_areas = sorted(filtered_df["Location"].unique())
else:
    filtered_df = df
    filtered_areas = sorted(df["Location"].unique())

selected_area = st.selectbox("Select an Area:", ["All"] + filtered_areas, index=0)

# Blood group filter
st.subheader("🔍 Search by Blood Group")
blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
selected_blood_group = st.selectbox("Choose a Blood Group:", ["All"] + blood_groups, index=0)

# Filter and display results
with st.spinner('Filtering blood banks...'):
    sleep(1)
    data = get_blood_banks()

    # Apply filters
    if selected_city != "All":
        data = data[data["City"] == selected_city]
    if selected_area != "All":
        data = data[data["Location"] == selected_area]
    if selected_blood_group != "All":
        data = data[data["Available Blood Groups"].str.contains(selected_blood_group, case=False, na=False)]

    # Display results
    if not data.empty:
        st.markdown("### Blood Bank Details:")
        for _, blood_bank in data.iterrows():
            st.markdown(f"""
            <div class="card">
                <h3>{blood_bank['Name']}</h3>
                <p><strong>City:</strong> {blood_bank['City']}</p>
                <p><strong>Location:</strong> {blood_bank['Location']}</p>
                <p><strong>Timings:</strong> {blood_bank['Timings']}</p>
                <p><strong>Available Blood Groups:</strong> {blood_bank['Available Blood Groups']}</p>
                <p><strong>Contact:</strong> {blood_bank['Contact']}</p>
                <p><strong>Website:</strong> <a href="{blood_bank['Website']}" target="_blank">Visit Website</a></p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No results found for the selected filters.")

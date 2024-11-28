import streamlit as st
import pandas as pd
from time import sleep

# Blood bank data
blood_banks = [
    {"Name": "City Blood Bank", "Location": "Shahrah-e-Faisal, Karachi", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-300-1234567", "Available Blood Groups": "A+, A-, O+, O-, B+", "Website": "https://citybloodbank.com"},
    {"Name": "Dow Blood Bank", "Location": "Gulshan, Karachi", "Timings": "24/7", "Contact": "+92-321-9876543", "Available Blood Groups": "A+, AB-, O+", "Website": "https://dowbloodbank.com"},
    {"Name": "Punjab Blood Bank", "Location": "Model Town, Lahore", "Timings": "8:00 AM - 8:00 PM", "Contact": "+92-322-5556789", "Available Blood Groups": "O+, O-", "Website": "https://punjabbloodbank.com"},
    {"Name": "Karachi Blood Bank", "Location": "Korangi, Karachi", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-300-6781234", "Available Blood Groups": "A+, O+, B+", "Website": "https://karachibloodbank.com"},
    {"Name": "Northern Blood Bank", "Location": "North Nazimabad, Karachi", "Timings": "24/7", "Contact": "+92-323-1234567", "Available Blood Groups": "AB-, A-, O+", "Website": "https://northernbloodbank.com"},
    {"Name": "Sindh Blood Bank", "Location": "Clifton, Karachi", "Timings": "8:00 AM - 8:00 PM", "Contact": "+92-324-9876543", "Available Blood Groups": "A-, O-, B+", "Website": "https://sindhbloodbank.com"},
    {"Name": "Jinnah Blood Bank", "Location": "Jamshed Road, Karachi", "Timings": "9:00 AM - 6:00 PM", "Contact": "+92-331-2345678", "Available Blood Groups": "B-, AB+, O+", "Website": "https://jinnahbloodbank.com"}
]

# Convert data to DataFrame
df = pd.DataFrame(blood_banks)

# Extract unique areas for the dropdown
areas = sorted(df["Location"].apply(lambda x: x.split(",")[0] if "," in x else x).unique())

# Cache blood bank data
@st.cache
def get_blood_banks():
    return df

# App configuration
st.set_page_config(page_title="Blood Bank Finder", page_icon="🩸", layout="centered")

# App title and introduction
st.markdown("<h1>🩸 Blood Bank Finder 🩸</h1>", unsafe_allow_html=True)

# Dropdowns for search filters
st.subheader("📍 Search by Area")
selected_area = st.selectbox("Select an Area:", ["All"] + areas, index=0)

st.subheader("🔍 Search for a Specific Blood Group")
blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
selected_blood_group = st.selectbox("Choose a Blood Group:", ["All"] + blood_groups, index=0)

# Filter and display results
with st.spinner('Filtering blood banks...'):
    sleep(1)
    data = get_blood_banks()

    # Apply filters if not set to "All"
    if selected_blood_group != "All":
        data = data[data["Available Blood Groups"].str.contains(selected_blood_group, case=False, na=False)]
    if selected_area != "All":
        data = data[data["Location"].str.contains(selected_area, case=False, na=False)]

    # Display results or warnings
    if not data.empty:
        st.markdown("### Blood Bank Details:")
        for _, blood_bank in data.iterrows():
            st.markdown(f"""
            <div style="background-color: cyan; padding: 15px; margin: 10px 0; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                <h3>{blood_bank['Name']}</h3>
                <p><strong>Location:</strong> {blood_bank['Location']}</p>
                <p><strong>Timings:</strong> {blood_bank['Timings']}</p>
                <p><strong>Available Blood Groups:</strong> {blood_bank['Available Blood Groups']}</p>
                <p><strong>Contact:</strong> {blood_bank['Contact']}</p>
                <p><strong>Website:</strong> <a href="{blood_bank['Website']}" target="_blank">Visit Website</a></p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No results found for the selected filters.")

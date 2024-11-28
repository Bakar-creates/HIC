import streamlit as st
import pandas as pd
from time import sleep

# Blood bank data across Pakistan
blood_banks = [
    {"Name": "City Blood Bank", "City": "Karachi", "Location": "Shahrah-e-Faisal", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-300-1234567", "Available Blood Groups": "A+, A-, O+, O-, B+", "Website": "https://citybloodbank.com"},
    {"Name": "Dow Blood Bank", "City": "Karachi", "Location": "Gulshan", "Timings": "24/7", "Contact": "+92-321-9876543", "Available Blood Groups": "A+, AB-, O+", "Website": "https://dowbloodbank.com"},
    {"Name": "Punjab Blood Bank", "City": "Lahore", "Location": "Model Town", "Timings": "8:00 AM - 8:00 PM", "Contact": "+92-322-5556789", "Available Blood Groups": "O+, O-", "Website": "https://punjabbloodbank.com"},
    {"Name": "Karachi Blood Bank", "City": "Karachi", "Location": "Korangi", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-300-6781234", "Available Blood Groups": "A+, O+, B+", "Website": "https://karachibloodbank.com"},
    {"Name": "Northern Blood Bank", "City": "Karachi", "Location": "North Nazimabad", "Timings": "24/7", "Contact": "+92-323-1234567", "Available Blood Groups": "AB-, A-, O+", "Website": "https://northernbloodbank.com"},
    {"Name": "Sindh Blood Bank", "City": "Karachi", "Location": "Clifton", "Timings": "8:00 AM - 8:00 PM", "Contact": "+92-324-9876543", "Available Blood Groups": "A-, O-, B+", "Website": "https://sindhbloodbank.com"},
    {"Name": "Jinnah Blood Bank", "City": "Karachi", "Location": "Jamshed Road", "Timings": "9:00 AM - 6:00 PM", "Contact": "+92-331-2345678", "Available Blood Groups": "B-, AB+, O+", "Website": "https://jinnahbloodbank.com"},
    {"Name": "Faisal Blood Bank", "City": "Lahore", "Location": "Johar Town", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-322-9991234", "Available Blood Groups": "A+, AB+, O+", "Website": "https://faisalbloodbank.com"},
    {"Name": "Rawalpindi Blood Bank", "City": "Rawalpindi", "Location": "Saddar", "Timings": "24/7", "Contact": "+92-333-7654321", "Available Blood Groups": "A+, A-, O+", "Website": "https://rawalpindibloodbank.com"},
    {"Name": "Peshawar Blood Bank", "City": "Peshawar", "Location": "Hayatabad", "Timings": "8:00 AM - 8:00 PM", "Contact": "+92-334-1112233", "Available Blood Groups": "O+, B-, AB+", "Website": "https://peshawarbloodbank.com"},
    {"Name": "Quetta Blood Bank", "City": "Quetta", "Location": "Civil Lines", "Timings": "9:00 AM - 5:00 PM", "Contact": "+92-335-5551234", "Available Blood Groups": "A-, B+, O-", "Website": "https://quettabloodbank.com"},
    {"Name": "Islamabad Blood Bank", "City": "Islamabad", "Location": "Blue Area", "Timings": "9:00 AM - 6:00 PM", "Contact": "+92-336-7651234", "Available Blood Groups": "AB+, A-, O+", "Website": "https://islamabadbloodbank.com"}
]

# Convert data to DataFrame
df = pd.DataFrame(blood_banks)

# Extract unique cities and areas for dropdown filters
cities = sorted(df["City"].unique())
areas = sorted(df["Location"].unique())

# Cache blood bank data
@st.cache
def get_blood_banks():
    return df

# App configuration
st.set_page_config(page_title="Blood Bank Finder", page_icon="🩸", layout="centered")

# App title
st.markdown("<h1>🩸 Blood Bank Finder - Pakistan 🩸</h1>", unsafe_allow_html=True)

# Filters
st.subheader("📍 Search by City")
selected_city = st.selectbox("Select a City:", ["All"] + cities, index=0)

st.subheader("📍 Search by Area")
if selected_city != "All":
    filtered_areas = sorted(df[df["City"] == selected_city]["Location"].unique())
else:
    filtered_areas = areas
selected_area = st.selectbox("Select an Area:", ["All"] + filtered_areas, index=0)

st.subheader("🔍 Search by Blood Group")
blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
selected_blood_group = st.selectbox("Choose a Blood Group:", ["All"] + blood_groups, index=0)

# Filter and display results
with st.spinner('Filtering blood banks...'):
    sleep(1)
    data = get_blood_banks()

    # Apply City filter
    if selected_city != "All":
        data = data[data["City"] == selected_city]
    
    # Apply Area filter
    if selected_area != "All":
        data = data[data["Location"] == selected_area]
    
    # Apply Blood Group filter
    if selected_blood_group != "All":
        data = data[data["Available Blood Groups"].str.contains(selected_blood_group, case=False, na=False)]

    # Display results or warnings
    if not data.empty:
        st.markdown("### Blood Bank Details:")
        for _, blood_bank in data.iterrows():
            st.markdown(f"""
            <div style="background-color: cyan; padding: 15px; margin: 10px 0; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
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

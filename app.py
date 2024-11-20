import streamlit as st
import pandas as pd

# Dummy blood bank data with additional entries and more areas
blood_banks = [
    {
        "Name": "City Blood Bank",
        "Location": "Shahrah-e-Faisal, Karachi",
        "Timings": "9:00 AM - 9:00 PM",
        "Contact": "+92-300-1234567",
        "Available Blood Groups": "A+, A-, O+, O-",
    },
    {
        "Name": "Safe Blood Bank",
        "Location": "North Nazimabad, Karachi",
        "Timings": "24/7",
        "Contact": "+92-300-7654321",
        "Available Blood Groups": "B+, B-, AB+, O+",
    },
    {
        "Name": "National Blood Center",
        "Location": "Clifton, Karachi",
        "Timings": "10:00 AM - 8:00 PM",
        "Contact": "+92-21-3456789",
        "Available Blood Groups": "A+, AB-, O-",
    },
    {
        "Name": "Karachi Blood Bank",
        "Location": "Korangi, Karachi",
        "Timings": "8:00 AM - 6:00 PM",
        "Contact": "+92-300-4567890",
        "Available Blood Groups": "A+, B-, O+",
    },
    {
        "Name": "Lifesaver Blood Bank",
        "Location": "Gulshan-e-Iqbal, Karachi",
        "Timings": "9:00 AM - 10:00 PM",
        "Contact": "+92-300-6789012",
        "Available Blood Groups": "O+, AB-, A-",
    },
    {
        "Name": "Hope Blood Bank",
        "Location": "F.B Area, Karachi",
        "Timings": "24/7",
        "Contact": "+92-300-2345678",
        "Available Blood Groups": "B+, AB+, O+",
    },
    {
        "Name": "Red Cross Blood Bank",
        "Location": "Saddar, Karachi",
        "Timings": "9:00 AM - 5:00 PM",
        "Contact": "+92-21-9876543",
        "Available Blood Groups": "O-, A-, B+",
    },
    {
        "Name": "Everest Blood Bank",
        "Location": "Lahore, Karachi",
        "Timings": "9:00 AM - 6:00 PM",
        "Contact": "+92-300-9876543",
        "Available Blood Groups": "A+, O+, AB-",
    },
    {
        "Name": "LifeLink Blood Bank",
        "Location": "Jamshed Town, Karachi",
        "Timings": "8:00 AM - 8:00 PM",
        "Contact": "+92-21-6654321",
        "Available Blood Groups": "A-, B-, AB+, O-",
    },
    {
        "Name": "Zindagi Blood Bank",
        "Location": "Malir, Karachi",
        "Timings": "9:00 AM - 7:00 PM",
        "Contact": "+92-300-1122334",
        "Available Blood Groups": "O+, B-, A+",
    },
    {
        "Name": "MedLife Blood Bank",
        "Location": "Bahria Town, Karachi",
        "Timings": "24/7",
        "Contact": "+92-300-9988776",
        "Available Blood Groups": "B+, AB-, O+",
    },
]

# Convert the data to a DataFrame for easier manipulation
df = pd.DataFrame(blood_banks)

# Extract unique areas from the "Location" column
areas = sorted(df['Location'].apply(lambda x: x.split(',')[0]).unique())

# Streamlit App
st.set_page_config(page_title="Blood Bank Finder", page_icon="🩸", layout="centered")

# Header and introduction
st.title("🩸 Blood Bank Finder")
st.write("Find blood banks in Karachi with their details, available blood groups, and areas.")
st.markdown("### Blood donation saves lives! 💉❤️")

# Filter by blood group
st.subheader("Search for a Specific Blood Group")
blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
selected_blood_group = st.selectbox("Select a blood group:", ["All"] + blood_groups)

if selected_blood_group != "All":
    filtered_by_group = df[df["Available Blood Gro

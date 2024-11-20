import streamlit as st
import pandas as pd
from time import sleep

# Dummy blood bank data with more entries and details
blood_banks = [
    {
        "Name": "City Blood Bank",
        "Location": "Shahrah-e-Faisal, Karachi",
        "Timings": "9:00 AM - 9:00 PM",
        "Contact": "+92-300-1234567",
        "Available Blood Groups": "A+, A-, O+, O-, B+",
        "Website": "https://citybloodbank.com"
    },
    {
        "Name": "Safe Blood Bank",
        "Location": "North Nazimabad, Karachi",
        "Timings": "24/7",
        "Contact": "+92-300-7654321",
        "Available Blood Groups": "B+, B-, AB+, O+, O-",
        "Website": "https://safebloodbank.com"
    },
    {
        "Name": "National Blood Center",
        "Location": "Clifton, Karachi",
        "Timings": "10:00 AM - 8:00 PM",
        "Contact": "+92-21-3456789",
        "Available Blood Groups": "A+, AB-, O-, O+",
        "Website": "https://nationalbloodcenter.com"
    },
    {
        "Name": "Karachi Blood Bank",
        "Location": "Korangi, Karachi",
        "Timings": "8:00 AM - 6:00 PM",
        "Contact": "+92-300-4567890",
        "Available Blood Groups": "A+, B-, O+, O-",
        "Website": "https://karachibloodbank.com"
    },
    {
        "Name": "Lifesaver Blood Bank",
        "Location": "Gulshan-e-Iqbal, Karachi",
        "Timings": "9:00 AM - 10:00 PM",
        "Contact": "+92-300-6789012",
        "Available Blood Groups": "O+, AB-, A-, O-",
        "Website": "https://lifesaverbloodbank.com"
    },
    {
        "Name": "Hope Blood Bank",
        "Location": "F.B Area, Karachi",
        "Timings": "24/7",
        "Contact": "+92-300-2345678",
        "Available Blood Groups": "B+, AB+, O+, O-",
        "Website": "https://hopebloodbank.com"
    },
    {
        "Name": "Red Crescent Blood Bank",
        "Location": "Karachi Cantt, Karachi",
        "Timings": "9:00 AM - 9:00 PM",
        "Contact": "+92-300-9988776",
        "Available Blood Groups": "A-, AB-, O+, O-",
        "Website": "https://redcrescentbloodbank.com"
    },
    {
        "Name": "Miracle Blood Bank",
        "Location": "Saddar, Karachi",
        "Timings": "10:00 AM - 6:00 PM",
        "Contact": "+92-300-1122334",
        "Available Blood Groups": "A+, B+, O-, O+",
        "Website": "https://miraclebloodbank.com"
    }
]

# Convert the data to a DataFrame for easier manipulation
df = pd.DataFrame(blood_banks)

# Extract unique areas from the "Location" column (only Karachi areas)
areas = sorted(df['Location'].apply(lambda x: x.split(',')[0]).unique())

# Streamlit App Configuration
st.set_page_config(page_title="Blood Bank Finder", page_icon="🩸", layout="centered")

# Title and Introduction
st.markdown("<h1 class='title'>🩸 Blood Bank Finder</h1>", unsafe_allow_html=True)
st.markdown("""
Welcome to the **Blood Bank Finder** app! Find the nearest blood banks in Karachi, their timings, and available blood groups.
""")

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

# CSS Styling for Animation and Transitions
st.markdown(
    """
    <style>
        .title {
            color: #FF6347;
            text-align: center;
            transition: color 0.3s ease;
        }

        .title:hover {
            color: #FF4500;  /* Change color on hover */
        }

        body {
            background-color: #f0f0f5;
            color: #333;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        .card {
            border: 2px solid #FF6347;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            background-color: #f8f8f8;
            color: #333;
            transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
        }

        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            background-color: #FF6347;
            color: white;
        }

        .card h3 {
            color: #FF6347;
            transition: color 0.3s ease;
        }

        .card a {
            color: #FF6347;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .card a:hover {
            color: #FFFFFF;
            text-decoration: underline;
        }

        .card p {
            transition: color 0.3s ease;
        }
    </style>
    """, unsafe_allow_html=True)

# Display results with card-style layout and animations
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

# Footer with Contact Information
st.markdown("""
---
📞 Contact the blood bank directly for more information.
""")

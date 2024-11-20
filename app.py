import streamlit as st
import pandas as pd

# Dummy blood bank data with more entries and details
blood_banks = [
    {
        "Name": "City Blood Bank",
        "Location": "Shahrah-e-Faisal, Karachi",
        "Timings": "9:00 AM - 9:00 PM",
        "Contact": "+92-300-1234567",
        "Available Blood Groups": "A+, A-, O+, O-",
        "Image": "https://via.placeholder.com/100"  # Placeholder image for now
    },
    {
        "Name": "Safe Blood Bank",
        "Location": "North Nazimabad, Karachi",
        "Timings": "24/7",
        "Contact": "+92-300-7654321",
        "Available Blood Groups": "B+, B-, AB+, O+",
        "Image": "https://via.placeholder.com/100"
    },
    {
        "Name": "National Blood Center",
        "Location": "Clifton, Karachi",
        "Timings": "10:00 AM - 8:00 PM",
        "Contact": "+92-21-3456789",
        "Available Blood Groups": "A+, AB-, O-",
        "Image": "https://via.placeholder.com/100"
    },
    {
        "Name": "Karachi Blood Bank",
        "Location": "Korangi, Karachi",
        "Timings": "8:00 AM - 6:00 PM",
        "Contact": "+92-300-4567890",
        "Available Blood Groups": "A+, B-, O+",
        "Image": "https://via.placeholder.com/100"
    },
    {
        "Name": "Lifesaver Blood Bank",
        "Location": "Gulshan-e-Iqbal, Karachi",
        "Timings": "9:00 AM - 10:00 PM",
        "Contact": "+92-300-6789012",
        "Available Blood Groups": "O+, AB-, A-",
        "Image": "https://via.placeholder.com/100"
    },
    {
        "Name": "Hope Blood Bank",
        "Location": "F.B Area, Karachi",
        "Timings": "24/7",
        "Contact": "+92-300-2345678",
        "Available Blood Groups": "B+, AB+, O+",
        "Image": "https://via.placeholder.com/100"
    },
]

# Convert the data to a DataFrame for easier manipulation
df = pd.DataFrame(blood_banks)

# Extract unique areas from the "Location" column
areas = sorted(df['Location'].apply(lambda x: x.split(',')[0]).unique())

# Streamlit App Configuration
st.set_page_config(page_title="Blood Bank Finder", page_icon="🩸", layout="centered")

# Background Image Styling (optional)
st.markdown(
    """
    <style>
        body {
            background-image: url('https://example.com/your-background-image.jpg'); /* Replace with your image URL */
            background-size: cover;
            background-position: center center;
        }
        .title {
            color: white;
            font-size: 36px;
            font-weight: bold;
        }
        .subheader {
            font-size: 24px;
            color: #D32F2F;
        }
        .stTextInput input {
            background-color: #ffffff;
            border-radius: 10px;
        }
        .stSelectbox {
            background-color: #ffffff;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Introduction
st.markdown("<h1 class='title'>🩸 Blood Bank Finder</h1>", unsafe_allow_html=True)
st.markdown("""
Welcome to the **Blood Bank Finder** app! Find the nearest blood banks in Karachi, their timings, and available blood groups.
""")

# User-friendly instructions
st.sidebar.markdown("### How to Use:")
st.sidebar.write("""
1. **Select a Blood Group** to filter blood banks with that specific blood type.
2. **Choose an Area** to narrow your search to specific locations.
3. **View Blood Bank Details**: Including timings, contact, and available blood groups.
""")

# Blood Group Search
st.subheader("🔍 Search for a Specific Blood Group")
blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
selected_blood_group = st.selectbox("Choose a Blood Group:", ["All"] + blood_groups, help="Select a blood group to filter the available blood banks.")

# Area Search
st.subheader("📍 Search by Area")
selected_area = st.selectbox("Select an Area:", ["All"] + areas, help="Select an area to filter blood banks.")

# Filter the data based on selected criteria
if selected_blood_group != "All":
    filtered_by_group = df[df["Available Blood Groups"].str.contains(selected_blood_group, case=False)]
else:
    filtered_by_group = df

if selected_area != "All":
    filtered_data = filtered_by_group[filtered_by_group["Location"].str.contains(selected_area, case=False)]
else:
    filtered_data = filtered_by_group

# Display results with attractive card-style layout
if not filtered_data.empty:
    st.markdown("### Blood Bank Details:")

    for idx, blood_bank in filtered_data.iterrows():
        st.markdown(f"""
        <div style="border: 2px solid #FF4C4C; border-radius: 10px; padding: 20px; margin-bottom: 20px; background-color: #f8f8f8;">
            <div style="display: flex; align-items: center;">
                <img src="{blood_bank['Image']}" alt="Blood Bank Image" style="width: 100px; height: 100px; border-radius: 10px; margin-right: 20px;">
                <div>
                    <h3>{blood_bank['Name']}</h3>
                    <p><strong>Location:</strong> {blood_bank['Location']}</p>
                    <p><strong>Timings:</strong> {blood_bank['Timings']}</p>
                    <p><strong>Available Blood Groups:</strong> {blood_bank['Available Blood Groups']}</p>
                    <p><strong>Contact:</strong> {blood_bank['Contact']}</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.write("No results found based on the selected filters. Please try different options.")

# Footer
st.markdown("""
---
📞 Contact the blood bank directly for more information.
""")

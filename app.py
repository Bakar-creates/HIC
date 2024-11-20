import streamlit as st
import pandas as pd

# Dummy blood bank data
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
]

# Convert the data to a DataFrame for easier manipulation
df = pd.DataFrame(blood_banks)

# Extract unique areas from the "Location" column
areas = sorted(df['Location'].apply(lambda x: x.split(',')[0]).unique())

# Streamlit App
st.set_page_config(page_title="Blood Bank Finder", page_icon="🩸", layout="centered")

st.title("🩸 Blood Bank Finder")
st.write("Find blood banks in Karachi with their details, available blood groups, and areas.")

# Search functionality for blood banks
st.subheader("Search for a Blood Bank")

# Filter by name or location
search_term = st.text_input("Search by blood bank name or location:")
if search_term:
    filtered_data = df[
        df["Name"].str.contains(search_term, case=False) |
        df["Location"].str.contains(search_term, case=False)
    ]
    if not filtered_data.empty:
        st.write("Search Results:")
        st.write(filtered_data[["Name", "Location", "Timings", "Contact"]])  # Show relevant columns
    else:
        st.write("No results found.")

# Filter by blood group
st.subheader("Search for a Specific Blood Group")
blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
selected_blood_group = st.selectbox("Select a blood group:", ["All"] + blood_groups)

if selected_blood_group != "All":
    filtered_by_group = df[df["Available Blood Groups"].str.contains(selected_blood_group, case=False)]
    if not filtered_by_group.empty:
        st.write(f"Blood Banks with {selected_blood_group}:")
        st.write(filtered_by_group[["Name", "Location", "Timings", "Contact"]])  # Show relevant columns
    else:
        st.write(f"No blood banks found for blood group {selected_blood_group}.")

# Filter by area
st.subheader("Search by Area")
selected_area = st.selectbox("Select an area:", ["All"] + areas)

if selected_area != "All":
    filtered_by_area = df[df["Location"].str.contains(selected_area, case=False)]
    if not filtered_by_area.empty:
        st.write(f"Blood Banks in {selected_area}:")
        st.write(filtered_by_area[["Name", "Location", "Timings", "Contact"]])  # Show relevant columns
    else:
        st.write(f"No blood banks found in {selected_area}.")

st.write("📞 Contact the blood bank for more details.")

import streamlit as st
import pandas as pd

# Load blood bank data from CSV
try:
    df = pd.read_csv("blood_banks.csv")
except FileNotFoundError:
    st.error("The file 'blood_banks.csv' was not found. Please ensure it exists in the same directory as this app.")
    st.stop()

# Streamlit App
st.set_page_config(page_title="Blood Bank Finder", page_icon="🩸", layout="centered")

st.title("🩸 Blood Bank Finder")
st.write("Find blood banks in Karachi with their details and available blood groups.")

# Display the blood banks in a table
st.subheader("Available Blood Banks")
st.table(df)

# Search functionality
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
        st.table(filtered_data)
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
        st.table(filtered_by_group)
    else:
        st.write(f"No blood banks found for blood group {selected_blood_group}.")

st.write("📞 Contact the blood bank for more details.")

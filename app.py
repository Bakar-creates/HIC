import streamlit as st
import pandas as pd

# Load blood bank data from CSV
df = pd.read_csv("blood_banks.csv")

# Streamlit App
st.set_page_config(page_title="Blood Bank Finder", page_icon="🩸", layout="centered")

st.title("🩸 Blood Bank Finder")
st.write("Find blood banks in Karachi with their details.")

# Display the blood banks in a table
st.subheader("Available Blood Banks")
st.table(df)

# Search functionality
st.subheader("Search for a Blood Bank")
search_term = st.text_input("Enter a location or name:")
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

st.write("📞 Contact the blood bank for more details.")


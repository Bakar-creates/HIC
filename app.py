# Streamlit App Configuration
st.set_page_config(page_title="Blood Bank Finder", page_icon="🩸", layout="centered")

# Title and Introduction
st.markdown("<h1 class='title'>🩸 Blood Bank Finder 🩸</h1>", unsafe_allow_html=True)
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

# Display results only if filters are applied
if selected_area != "All" or selected_blood_group != "All":
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
else:
    st.write("Please select an area or blood group to view available blood banks.")

# Footer with Contact Information
st.markdown("""
---
📞 Contact the blood bank directly for more information.
""")

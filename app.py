import streamlit as st
import pandas as pd
from time import sleep

# Expanded blood bank data across Pakistan
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
    {"Name": "Islamabad Blood Bank", "City": "Islamabad", "Location": "Blue Area", "Timings": "9:00 AM - 6:00 PM", "Contact": "+92-336-7651234", "Available Blood Groups": "AB+, A-, O+", "Website": "https://islamabadbloodbank.com"},
    {"Name": "Multan Blood Bank", "City": "Multan", "Location": "Cantt", "Timings": "9:00 AM - 5:00 PM", "Contact": "+92-345-6789012", "Available Blood Groups": "B+, O+", "Website": "https://multanbloodbank.com"},
    {"Name": "Faisalabad Blood Bank", "City": "Faisalabad", "Location": "Peoples Colony", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-334-5678901", "Available Blood Groups": "A-, AB+, O-", "Website": "https://faisalabadbloodbank.com"},
    {"Name": "Hyderabad Blood Bank", "City": "Hyderabad", "Location": "Latifabad", "Timings": "8:00 AM - 8:00 PM", "Contact": "+92-342-6789012", "Available Blood Groups": "A+, B-", "Website": "https://hyderabadbloodbank.com"},
    {"Name": "Sialkot Blood Bank", "City": "Sialkot", "Location": "Cantt", "Timings": "9:00 AM - 6:00 PM", "Contact": "+92-300-1236789", "Available Blood Groups": "B-, AB+", "Website": "https://sialkotbloodbank.com"},
    {"Name": "Gujranwala Blood Bank", "City": "Gujranwala", "Location": "Satellite Town", "Timings": "8:00 AM - 8:00 PM", "Contact": "+92-333-8765432", "Available Blood Groups": "A+, O+", "Website": "https://gujranwalabloodbank.com"},
    {"Name": "Abbottabad Blood Bank", "City": "Abbottabad", "Location": "Mansehra Road", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-335-9876543", "Available Blood Groups": "A-, B+", "Website": "https://abbottabadbloodbank.com"},
    {"Name": "Gilgit Blood Bank", "City": "Gilgit", "Location": "Jutial", "Timings": "9:00 AM - 5:00 PM", "Contact": "+92-346-4567890", "Available Blood Groups": "O+, AB-", "Website": "https://gilgitbloodbank.com"},
    {"Name": "Chitral Blood Bank", "City": "Chitral", "Location": "Balach", "Timings": "8:00 AM - 4:00 PM", "Contact": "+92-344-1122334", "Available Blood Groups": "A+, B-", "Website": "https://chitralbloodbank.com"},
    {"Name": "Bahawalpur Blood Bank", "City": "Bahawalpur", "Location": "Model Town A", "Timings": "9:00 AM - 7:00 PM", "Contact": "+92-348-9988776", "Available Blood Groups": "O+, A-", "Website": "https://bahawalpurbloodbank.com"},
    {"Name": "Sukkur Blood Bank", "City": "Sukkur", "Location": "Minara Road", "Timings": "8:00 AM - 6:00 PM", "Contact": "+92-349-2233445", "Available Blood Groups": "B+, AB+", "Website": "https://sukkrbloodbank.com"}
]


# Convert data to DataFrame
df = pd.DataFrame(blood_banks)

# Cache blood bank data
@st.cache_data
def get_blood_banks():
    return df

# App configuration
st.set_page_config(page_title="Blood Bank Finder Pakistan", page_icon="🩸", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Background gradient for the app */
        .stApp {
            background: linear-gradient(to bottom right, #e0f7fa, #fff8e1);
            color: #333;
        }

        /* App header styling */
        .header {
            text-align: center;
            background: linear-gradient(to right, #007bff, #00bcd4);
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            font-family: 'Poppins', sans-serif;
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 5px;
        }

        .header p {
            font-size: 1.2em;
            font-weight: 300;
        }

        /* Filter section */
        .filter-section {
            background-color: #f5f5f5;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Stylish cards */
        .card {
            background: linear-gradient(to bottom, #ffffff, #e0f7fa);
            padding: 20px;
            margin: 10px 0;
            border-radius: 15px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        /* Button for website links */
        .visit-button {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-size: 1em;
            transition: background 0.3s ease;
        }

        .visit-button:hover {
            background-color: #0056b3;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .header h1 {
                font-size: 2em;
            }
            .header p {
                font-size: 1em;
            }
            .card {
                padding: 15px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class="header">
        <h1>🩸 Blood Bank Finder Pakistan</h1>
        <p>Find blood banks near you with ease.</p>
    </div>
""", unsafe_allow_html=True)

# Debugging and Error Handling
if 'df' not in locals() or df.empty:
    st.error("Error: Blood bank data could not be loaded. Please check the source.")
    st.stop()  # Stops execution if the data is invalid
else:
    st.write("Dataframe preview:", df.head())
    cities = sorted(df["City"].unique())
    st.write("Cities:", cities)

# Filter Section
st.markdown('<div class="filter-section">', unsafe_allow_html=True)

# City Selection
if 'cities' not in locals() or not cities:
    st.error("No cities available. Please check the data source.")
else:
    selected_city = st.selectbox("Select a City:", ["All"] + cities, index=0)

# Area Selection
st.subheader("📍 Search by Area")
if selected_city != "All":
    filtered_df = df[df["City"] == selected_city]
    filtered_areas = sorted(filtered_df["Location"].unique())
else:
    filtered_df = df
    filtered_areas = sorted(df["Location"].unique())

selected_area = st.selectbox("Select an Area:", ["All"] + filtered_areas, index=0)

# Blood Group Selection
st.subheader("🔍 Search by Blood Group")
blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]  # Example blood groups
selected_blood_group = st.selectbox("Choose a Blood Group:", ["All"] + blood_groups, index=0)

st.markdown('</div>', unsafe_allow_html=True)

# Filter and Display Results
with st.spinner('Filtering blood banks...'):
    sleep(1)
    data = get_blood_banks()

    if selected_city != "All":
        data = data[data["City"] == selected_city]
    if selected_area != "All":
        data = data[data["Location"] == selected_area]
    if selected_blood_group != "All":
        data = data[data["Available Blood Groups"].str.contains(selected_blood_group, case=False, na=False)]

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
                <a class="visit-button" href="{blood_bank['Website']}" target="_blank">Visit Website</a>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No results found for the selected filters.")

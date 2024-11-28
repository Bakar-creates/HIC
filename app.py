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
    # New entries
    {"Name": "Multan Blood Bank", "City": "Multan", "Location": "Cantt", "Timings": "9:00 AM - 5:00 PM", "Contact": "+92-345-6789012", "Available Blood Groups": "B+, O+", "Website": "https://multanbloodbank.com"},
    {"Name": "Faisalabad Blood Bank", "City": "Faisalabad", "Location": "Peoples Colony", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-334-5678901", "Available Blood Groups": "A-, AB+, O-", "Website": "https://faisalabadbloodbank.com"},
    {"Name": "Hyderabad Blood Bank", "City": "Hyderabad", "Location": "Latifabad", "Timings": "8:00 AM - 8:00 PM", "Contact": "+92-342-6789012", "Available Blood Groups": "A+, B-", "Website": "https://hyderabadbloodbank.com"},
    {"Name": "Sialkot Blood Bank", "City": "Sialkot", "Location": "Cantt", "Timings": "9:00 AM - 6:00 PM", "Contact": "+92-300-1236789", "Available Blood Groups": "B-, AB+", "Website": "https://sialkotbloodbank.com"},
    {"Name": "Gujranwala Blood Bank", "City": "Gujranwala", "Location": "Satellite Town", "Timings": "8:00 AM - 8:00 PM", "Contact": "+92-333-8765432", "Available Blood Groups": "A+, O+", "Website": "https://gujranwalabloodbank.com"},
    {"Name": "Abbottabad Blood Bank", "City": "Abbottabad", "Location": "Mansehra Road", "Timings": "9:00 AM - 9:00 PM", "Contact": "+92-335-9876543", "Available Blood Groups": "A-, B+", "Website": "https://abbottabadbloodbank.com"},
]

# Convert data to DataFrame
df = pd.DataFrame(blood_banks)

# Cache blood bank data
@st.cache_data
def get_blood_banks():
    return df

# App configuration
st.set_page_config(page_title="Blood Bank Finder Pakistan", page_icon="🩸", layout="centered")

# Add custom CSS for styling
st.markdown("""
    <style>
        /* Define default font settings */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Roboto:wght@300;400&display=swap');
        
        body {
            font-family: 'Roboto', sans-serif;
            color: #333;
            background-color: #ffffff; /* Light mode background */
            transition: all 0.3s ease-in-out;
        }

        /* Styling for the title */
        .title {
            text-align: center;
            font-size: 2.5em;
            font-weight: 600;
            margin-bottom: 20px;
            color: #007bff;
            font-family: 'Poppins', sans-serif;
        }

        /* Card style */
        .card {
            background-color: #e0f7fa;
            padding: 20px;
            margin: 10px 0;
            border-radius: 12px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
            font-family: 'Roboto', sans-serif;
        }

        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        /* Select box and multiselect style */
        .stSelectbox, .stMultiselect {
            background-color: #f0f8ff;
            border-radius: 12px;
            padding: 12px;
            font-size: 1.2em;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            font-family: 'Roboto', sans-serif;
        }

        .stSelectbox:hover, .stMultiselect:hover {
            background-color: #d0e9f7;
            transform: scale(1.02);
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
        }

        .stSelectbox:focus, .stMultiselect:focus {
            border: 2px solid #007bff;
        }

        /* Styling for text input boxes */
        .stTextInput {
            background-color: #f0f8ff;
            border-radius: 12px;
            padding: 12px;
            font-size: 1.2em;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Styling the map */
        .stMap {
            border-radius: 12px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
        }

        /* Custom button styling */
        .stButton {
            background-color: #007bff;
            color: #ffffff;
            font-size: 1.1em;
            padding: 12px 24px;
            border-radius: 12px;
            border: none;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            cursor: pointer;
            font-family: 'Roboto', sans-serif;
        }

        .stButton:hover {
            background-color: #0056b3;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        /* Styling for footer */
        footer {
            text-align: center;
            margin-top: 50px;
            font-size: 1.1em;
            color: #777;
        }

        footer a {
            color: #007bff;
            text-decoration: none;
        }

        footer a:hover {
            text-decoration: underline;
        }

        /* Styling the loading indicator */
        .loading-spinner {
            text-align: center;
            margin-top: 50px;
        }

        /* Styling for mobile responsiveness */
        @media screen and (max-width: 768px) {
            .title {
                font-size: 2em;
            }

            .card {
                padding: 15px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.markdown("<h1 class='title'>Blood Bank Finder</h1>", unsafe_allow_html=True)

# Sidebar filters
st.sidebar.header("Filters")

# City filter
cities = df['City'].unique()
city = st.sidebar.selectbox("Select City", ["All"] + list(cities))

# Blood group filter
blood_groups = df['Available Blood Groups'].unique()
blood_group = st.sidebar.multiselect("Select Blood Group(s)", ["All"] + list(blood_groups))

# Search bar for blood bank name
search_term = st.sidebar.text_input("Search by Blood Bank Name")

# Filter the dataframe based on user input
filtered_df = df

if city != "All":
    filtered_df = filtered_df[filtered_df['City'] == city]

if blood_group != ["All"]:
    filtered_df = filtered_df[filtered_df['Available Blood Groups'].apply(lambda x: any(bg in x for bg in blood_group))]

if search_term:
    filtered_df = filtered_df[filtered_df['Name'].str.contains(search_term, case=False)]

# Display results with a loading indicator
with st.spinner("Loading blood banks..."):
    sleep(2)  # Simulate loading time

    if len(filtered_df) > 0:
        for index, row in filtered_df.iterrows():
            with st.expander(row['Name']):
                st.markdown(f"**City**: {row['City']}")
                st.markdown(f"**Location**: {row['Location']}")
                st.markdown(f"**Timings**: {row['Timings']}")
                st.markdown(f"**Contact**: {row['Contact']}")
                st.markdown(f"**Available Blood Groups**: {row['Available Blood Groups']}")
                st.markdown(f"[Website]({row['Website']})")
    else:
        st.warning("No blood banks found based on your criteria.")

# Footer
st.markdown("""
    <footer>
        <p>Created with ❤️ by <a href='https://www.linkedin.com'>Your Name</a></p>
    </footer>
""", unsafe_allow_html=True)

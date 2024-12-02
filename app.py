# Custom CSS for styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to bottom right, #e0f7fa, #fff8e1);
            color: #333;
        }

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
        }

        .header p {
            font-size: 1.2em;
            font-weight: 300;
        }

        .filter-section {
            background-color: #f5f5f5;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .filter-section select {
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 10px;
            border-radius: 10px;
            border: 1px solid #007bff;
            background-color: #ffffff;
        }

        .filter-section select:focus {
            border-color: #00bcd4;
            outline: none;
            box-shadow: 0 4px 10px rgba(0, 188, 212, 0.3);
        }

        .card {
            background: linear-gradient(to bottom, #ffffff, #e0f7fa);
            padding: 20px;
            margin: 10px 0;
            border-radius: 15px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .card:hover {
            transform: scale(1.05);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }

        .visit-button {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #8bc34a;  /* Changed to light green */
            color: white;
            text-decoration: none;
            border-radius: 8px;
            transition: background-color 0.3s ease;
        }

        .visit-button:hover {
            background-color: #689f38; /* Darker green on hover */
        }

    </style>
""", unsafe_allow_html=True)

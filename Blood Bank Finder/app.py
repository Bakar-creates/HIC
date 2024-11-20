from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Dummy blood bank data
blood_banks = [
    {
        "name": "City Blood Bank",
        "location": "Shahrah-e-Faisal, Karachi",
        "timings": "9:00 AM - 9:00 PM",
        "contact": "+92-300-1234567",
    },
    {
        "name": "Safe Blood Bank",
        "location": "North Nazimabad, Karachi",
        "timings": "24/7",
        "contact": "+92-300-7654321",
    },
    {
        "name": "National Blood Center",
        "location": "Clifton, Karachi",
        "timings": "10:00 AM - 8:00 PM",
        "contact": "+92-21-3456789",
    },
]

@app.route('/')
def home():
    return render_template('index.html', blood_banks=blood_banks)

@app.route('/api/blood_banks')
def get_blood_banks():
    return jsonify(blood_banks)

if __name__ == '__main__':
    app.run(debug=True)


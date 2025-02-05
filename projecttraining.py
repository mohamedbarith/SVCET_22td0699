from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend interaction

# In-memory contact list (temporary storage)
contacts = []

# Route to add a contact
@app.route('/add_contact', methods=['POST'])
def add_contact():
    data = request.json
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')

    # Ensure all fields are provided
    if name and phone and email:
        contacts.append({'name': name, 'phone': phone, 'email': email})
        return jsonify({"message": "Contact added successfully!"}), 201
    return jsonify({"error": "All fields (name, phone, email) are required!"}), 400

# Route to display all contacts
@app.route('/display_contacts', methods=['GET'])
def display_contacts():
    return jsonify(contacts)

# Route to search contacts by keyword (name)
@app.route('/search_contact', methods=['GET'])
def search_contact():
    keyword = request.args.get('keyword', '').lower()
    # Filter contacts based on the name
    filtered_contacts = [contact for contact in contacts if keyword in contact['name'].lower()]
    return jsonify(filtered_contacts)

if __name__ == '__main__':
    app.run(debug=True)


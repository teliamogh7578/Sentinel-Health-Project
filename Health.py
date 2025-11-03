from dotenv import load_dotenv
load_dotenv()
import os
import firebase_admin
from firebase_admin import credentials, auth, firestore
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests  # --- IMPORT THE NEW LIBRARY ---

# --- NEW: Import your disease database ---
from disease_db import DISEASE_KNOWLEDGE_BASE

# --- 1. INITIALIZATION ---
script_dir = os.path.dirname(os.path.abspath(__file__))
key_file_path = os.path.join(script_dir, "serviceAccountKey.json")
try:
    cred = credentials.Certificate(key_file_path)
    firebase_admin.initialize_app(cred)
except FileNotFoundError:
    print("FATAL ERROR: 'serviceAccountKey.json' not found.")
    exit()

app = Flask(__name__)
db = firestore.client()
CORS(app)

# --- 2. AUTHENTICATION HELPER ---


def get_user_from_token(request):
    try:
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return None, ("Missing authorization header", 401)

        id_token = auth_header.split(" ").pop()
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token, None
    except auth.InvalidIdTokenError:
        return None, ("Invalid auth token", 403)
    except Exception as e:
        return None, (f"An error occurred: {e}", 500)

# --- 3. UPGRADED "SOLUTION SYSTEM" ---


def trigger_high_risk_alert(uid, report):
    """
    This is your "call ambulance" feature.
    It alerts guardians/clinics for 'high' or 'critical' risk.
    """
    print(f"--- URGENT ALERT (CALL AMBULANCE/GUARDIAN) ---")
    print(f"User {uid} has a high-risk report:")
    print(f"Potential Condition: {report.get('disease_name')}")
    print(f"Recommendation: {report.get('info', {}).get('recommendation')}")
    print(f"--- ALERTING LOCAL GUARDIANS AND NEAREST HOSPITAL ---")
    pass


def get_age_group(age):
    """Converts a numerical age into a database key."""
    if age <= 2:
        return "infant"
    if age <= 12:
        return "child"
    if age <= 17:
        return "teen"
    if age <= 64:
        return "adult"
    return "senior"


def upgraded_triage_algorithm(form_data):
    """
    This is the new "brain." It searches your DB and uses age-specific logic.
    """
    symptoms = form_data.get('symptoms', [])
    age = form_data.get('age', 30)
    gender = form_data.get('gender', 'unknown')
    age_key = get_age_group(age)
    possible_conditions = []

    for disease_name, info in DISEASE_KNOWLEDGE_BASE.items():
        match_count = len(set(symptoms) & set(info['symptoms']))
        symptom_total = len(info['symptoms'])
        if symptom_total == 0:
            continue

        match_score = int((match_count / symptom_total) * 100)

        if match_count >= 2 or (match_count > 0 and match_score >= 50):
            current_risk = info['base_risk'].get(
                age_key, info['base_risk'].get('default', 'medium'))
            education = info['education'].get(age_key, info['education'].get(
                'default', 'No specific info available.'))
            recommendation = info['recommendation'].get(
                age_key, info['recommendation'].get('default', 'See a doctor.'))

            if disease_name == 'anaemia' and gender == 'female' and age_key in ['teen', 'adult']:
                current_risk = "high"

            final_info = {
                "type": info['type'],
                "education": education,
                "recommendation": recommendation,
                "specialist": info['specialist']
            }
            possible_conditions.append({
                "disease_name": disease_name,
                "risk": current_risk,
                "match_score": match_score,
                "info": final_info
            })

    if not possible_conditions:
        return [{
            "risk": "low",
            "disease_name": "Unknown/General",
            "match_score": 0,
            "info": {
                "type": "non-communicable",
                "education": "Your symptoms don't match a specific pattern. Monitor your health, stay hydrated, and rest.",
                "recommendation": "See a doctor if symptoms get worse.",
                "specialist": "General Practitioner"
            }
        }]

    risk_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    final_report = sorted(
        possible_conditions,
        key=lambda x: (
            risk_order.get(x['risk'], 99),
            -x['match_score']
        )
    )
    return final_report

# --- 4. API ENDPOINTS (The "Links") ---


@app.route("/")
def home():
    return "Sentinel Health System Backend is running!"


@app.route("/api/submit-screening", methods=['POST'])
def submit_screening():
   # decoded_token, error = get_user_from_token(request)
   # if error:
   #     return jsonify({"error": error[0]}), error[1]

   # uid = decoded_token['uid']
   # user_email = decoded_token.get('email')
    uid = "test_user_id"
    user_email = "test@example.com"
    form_data = request.json
    if not form_data or 'symptoms' not in form_data:
        return jsonify({"error": "No symptoms data provided"}), 400

    triage_results = upgraded_triage_algorithm(form_data)

    try:
        top_result = triage_results[0]
        screening_ref = db.collection('screenings').document()
        screening_ref.set({
            "submitted_by_uid": uid,
            "user_email": user_email,
            "form_data": form_data,
            "triage_results": triage_results,
            "top_result": top_result,
            "timestamp": firestore.SERVER_TIMESTAMP
        })

        if top_result['risk'] == 'high' or top_result['risk'] == 'critical':
            trigger_high_risk_alert(uid, top_result)

        return jsonify(triage_results), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500


# --- THIS IS THE MODIFIED FUNCTION ---
@app.route("/api/find-nearby-clinics", methods=['POST'])
def find_nearby_clinics():
    """
    POWERS: Find Nearest Hospitals and Clinics
    This endpoint takes a user's GPS location and returns
    a list of real places from the Google cles API.
    """
    # 1. Verify user
    decoded_token, error = get_user_from_token(request)
    if error:
        return jsonify({"error": error[0]}), error[1]

    # 2. Get GPS location from frontend
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if not latitude or not longitude:
        return jsonify({"error": "Missing GPS coordinates"}), 400

    # 3. Get your secret API key from environment variables
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        # This is a server error, not a user error
        return jsonify({"error": "Server configuration error. API key not set."}), 500

    # 4. Build the Google Maps API URL
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    radius = 5000  # 5000 meters (5km)
    keyword = "hospital"  # Search for these terms

    url = f"{base_url}?location={latitude},{longitude}&radius={radius}&type={type}&keyword=hospital&key={api_key}"


    try:
        # 5. Make the API request
        api_response = requests.get(url)
        api_response.raise_for_status()  # Raise an error on a bad response (4xx or 5xx)
        google_data = api_response.json()
        print(google_data)

        # 6. Parse the results to send a clean list to the frontend
        raw_results = google_data.get("results", [])
        clinics_list = []

        for place in raw_results:
            clinics_list.append({
                "name": place.get("name"),
                # 'vicinity' is the human-readable address
                "address": place.get("vicinity"),
                # The {lat, lng}
                "location": place.get("geometry", {}).get("location"),
                "rating": place.get("rating"),
                # True, False, or None
                "is_open": place.get("opening_hours", {}).get("open_now")
            })

        return jsonify(clinics_list)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Could not contact Google Maps API: {e}"}), 503
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500
# --- END OF MODIFIED FUNCTION ---


# (Your /api/admin/dashboard-data and /api/prevention-nudges would also go here)

# --- 5. RUN THE SERVER ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)
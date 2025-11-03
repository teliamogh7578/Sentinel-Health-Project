# Health-Project-Sentinel
Health Sentinel: An AI-Powered Wellness & Symptom Screener

Health Sentinel is a web application (built for the CacheMoney hackathon) that moves beyond simple symptom checklists. It provides users with a comprehensive, AI-powered analysis of their self-reported health data.

Instead of just storing data, this app acts as an intelligent "first opinion" by securely sending a user's symptom profile to a generative AI (Google's Gemini) for real-time analysis. The user receives an easy-to-understand breakdown of potential health risks, key concern areas, and actionable recommendations.

🚀 Key Features
Secure Authentication: Users can create an account and log in using Firebase Authentication.
Single-Page Application (SPA): A clean, loop-free user experience. The app uses JavaScript to show/hide the login and dashboard sections without ever needing to reload the page.
Comprehensive Screener: A 25-question, multi-page survey covering general wellness, pain, respiratory, digestive, and mental health.
Real-Time AI Analysis: The core of the project. User answers are sent to a Python backend, which prompts the Google Gemini API to generate a unique, holistic analysis.
Dynamic Dashboard: The user's dashboard listens directly to the Firestore database and displays the AI's analysis (Risk Level, Key Concerns, Recommendation) the moment it's ready.


🛠️ Tech Stack

This project is built with a modern, decoupled architecture.
Frontend: HTML, CSS, and vanilla JavaScript (as a Single-Page Application).
Authentication: Firebase Authentication (for user sign-up and login).
Database: Firebase Firestore (a NoSQL database to store user roles and the final AI-generated results).
Backend: Python (Flask) deployed as a separate microservice (e.g., on Render).
AI: Google Gemini Pro (via the google-generativeai Python library).

⚙️ How It Works (Data Flow)

The separation of frontend and backend allows for a secure and scalable design.
Login: User signs in on the frontend. Firebase Auth verifies them. onAuthStateChanged in app.js hides the login UI and shows the dashboard UI.
Submit: The user fills out the 25-question survey. On submit, the frontend app.js gathers all 25 answers into a JSON object.
Send to Backend: The frontend fetches the Python (Flask) backend API, securely sending the user's ID and their answers.
Prompt AI: The Python server receives the JSON, formats it into a detailed prompt, and sends it to the Google Gemini API.
Get Response: The Gemini API returns a JSON object with the analysis (e.g., { "risk": "Medium", "concerns": ["Digestive", "Sleep"], "recommendation": "..." }).
Save to DB: The Python server saves this AI response to the results collection in Firestore, using the user's ID as the document name.
Display Result: The frontend app.js, which has an active onSnapshot listener on that exact document, gets the new data instantly. It hides the "loading" spinner and displays the AI's analysis to the user.

📦 How to Run This Project Locally

This project has two parts that must be run separately.
1. Backend Server (Python)
Navigate to the /backend folder.
Create and activate a virtual environment:
python -m venv venv
.\venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Add Service Account Key: Download your service-account-key.json file from your Firebase project settings and place it in this /backend folder.
Set Environment Variables: You must set your Gemini API key in your terminal.
Windows (CMD): set GEMINI_API_KEY=YOUR_API_KEY
Windows (PowerShell): $env:GEMINI_API_KEY="YOUR_API_KEY"
Mac/Linux: export GEMINI_API_KEY="YOUR_API_KEY"
Run the Flask server:
python app.py


(The server will be running at http://127.0.0.1:5000)

2. Frontend (HTML/JS)
Add Firebase Config: Open index.html and paste your firebaseConfig object (from your Firebase project settings) into the script tag at the bottom.
Update JS: Open app.js and change the RENDER_BACKEND_URL variable to your local backend address:
const RENDER_BACKEND_URL = "[http://127.0.0.1:5000/submit](http://127.0.0.1:5000/submit)";


Run the Frontend: The easiest way is with the VS Code Live Server extension.

Right-click index.html and select "Open with Live Server".

This will open your app in a browser (e.g., at http://127.0.0.1:5500).

You can now sign up, log in, and use the full application.

# Health-Project-Sentinel
Health Sentinel — Symptom-Based Wellness Screener

Health Sentinel is a full-stack wellness screener built for a Hackathon.
It helps users understand potential health concerns by comparing their self-reported symptoms with a structured symptoms database and returning the closest matching health profile.

This provides a simple, first-opinion style interpretation of symptoms.
The system relies on pattern matching, weighted scoring, and database comparisons to determine the most relevant result.

  Note:
Parts of the project (UI scaffolding, boilerplate code) were developed with assistance from AI tools.
All system logic, data structuring, symptom-matching rules, debugging, and integration work were manually implemented by the team.

  Key Features:
Secure Authentication — Firebase signup/login.
Single-Page Architecture — No reloads; dynamic content switching using vanilla JS.
25-Question Comprehensive Screener — General wellness, pain, digestion, sleep, mental health, etc.
Pattern-Matching Engine — Matches user responses with a symptom database to find the most probable health category.
Dynamic Realtime Dashboard — Firestore onSnapshot pushes updates immediately.
Fully Decoupled Design — Frontend + backend microservice architecture.

  Tech Stack:
Frontend:
HTML, CSS, JavaScript
Firebase Authentication
Firestore (Realtime Database)
Backend
Python (Flask microservice)
Firestore Admin SDK
Custom similarity / matching logic (no AI, no ML)

  How It Works:
User logs in → Firebase verifies account.
User completes the 25-question survey.
Frontend sends user responses + UID to the backend.

  Backend performs:
symptom keyword scoring
weighted similarity matching
comparison against a predefined health-condition database
The backend identifies the closest match and writes the result to Firestore.
The frontend listens using onSnapshot() and instantly displays the matched profile.

  Running the Project Locally:
Backend Setup
cd backend
python -m venv venv
.\venv\Scripts\activate  (Windows)
source venv/bin/activate (Mac/Linux)
pip install -r requirements.txt
Add your service-account-key.json to /backend.
Start the backend:
python app.py
Frontend Setup
Paste Firebase config into index.html
Update backend URL in app.js:
const BACKEND_URL = "http://127.0.0.1:5000/submit";
Run using VS Code Live Server.

  **What I Learned While Working On This Project:**
Working on Health Sentinel helped me build experience in full-stack development and real-world deployment.
Key takeaways:
1.Frontend Development:
Building a Single-Page Application (SPA) using only vanilla JavaScript
Managing UI state changes without reloads.
Integrating Firebase Authentication into a custom UI.
2.Backend Development:
Creating a Python Flask microservice.
Handling JSON payloads from the frontend.
Implementing custom pattern-matching / similarity scoring without AI or ML models.
3.Database & Integration:
Using Firebase Firestore (both client-side and admin SDK).
Handling realtime updates with onSnapshot().
Securely mapping user IDs to their results.
4.Architecture & Deployment:
Structuring a decoupled frontend–backend system.
Working with environment variables and credentials.
Understanding how to deploy and test microservices.

  Teamwork & Hackathon Skills:
Rapid prototyping within time constraints.
Debugging AI-generated boilerplate and making it production-ready.
Writing prompts and instructions clearly when using AI tools.

  AI Assistance Disclosure:
This project was created during a short hackathon timeframe and involved significant assistance from AI coding tools for:
generating boilerplate HTML/CSS/JS
initial Flask route scaffolding
prompt formatting suggestions
**All architectural decisions, debugging, Firebase integration, API usage, and deployment steps were manually designed and executed by the team.**

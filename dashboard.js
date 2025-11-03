// --- NEW dashboard.js ---
// This file IS connected to your Python backend.

document.addEventListener("DOMContentLoaded", () => {
    const agreementModal = document.getElementById("agreement-modal");
    const agreeBtn = document.getElementById("agree-btn");
    const surveyForm = document.getElementById("survey-form");

// Show modal on page load (after login)
agreementModal.style.display = "flex";  // Makes the modal visible
surveyForm.style.display = "none";      // Hide the survey until user agrees

// When user clicks "Agree & Continue"
agreeBtn.addEventListener("click", () => {
    agreementModal.style.display = "none";  // Hide modal
    surveyForm.style.display = "block";     // Show survey form
});
//ends here the agreement statement
    const form = document.getElementById("survey-form");
    const resultsContainer = document.getElementById("results-container");
    const loading = document.getElementById("loading");

    // This maps your HTML form IDs to the symptom names your Python DB expects
    const SYMPTOM_MAP = {
        "q_fatigue": "fatigue",
        "q_fever": "fever",
        "q_headaches_general": "headache",
        "q_headaches_severe": "severe headache",
        "q_body_aches": "muscle pain",
        "q_abdominal_pain": "abdominal pain",
        "q_chest_discomfort": "chest pain",
        "q_cough": "cough",
        "q_sore_throat": "sore throat",
        "q_nasal_issues": "runny nose",
        "q_breathing_difficulty": "shortness of breath",
        "q_nausea": "nausea",
        "q_bowel_diarrhea": "diarrhea",
        "q_indigestion": "heartburn", // Mapped to 'heartburn' for GERD
        "q_urinary_frequency": "frequent urination",
        "q_urinary_pain": "painful urination",
        "q_skin_issues": "itchy rash",
        "q_vision_issues": "blurry vision",
        "q_dizziness": "dizziness",
        "q_sleep_disruption": "changes in sleep",
        "q_low_mood": "persistent sadness",
        "q_anxiety": "excessive worry",
        "q_cognitive_issues": "difficulty concentrating"
    };

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        form.style.display = "none";
        loading.style.display = "block";
        resultsContainer.innerHTML = ""; // Clear old results

        // 1. Get Age and Gender from the new HTML fields
        const age = parseInt(document.getElementById("user_age").value);
        const gender = document.getElementById("user_gender").value;

        // 2. Convert 1-5 ratings into a simple symptom list
        let symptoms_list = [];
        for (const [questionId, symptomName] of Object.entries(SYMPTOM_MAP)) {
            const rating = parseInt(document.getElementById(questionId).value);
            // If rating is 3 or higher, add it to the list
            if (rating >= 3) {
                symptoms_list.push(symptomName);
            }
        }

        // 3. Prepare the data for the backend
        const formData = {
            age: age,
            gender: gender,
            symptoms: symptoms_list
        };

        // --- THIS IS THE MOST IMPORTANT PART ---
        // This is where we call your Python API.
        // Assumes your Python server is running on http://127.0.0.1:5000

        try {
            // !! IMPORTANT: See note below about 'YOUR_AUTH_TOKEN'
            // For testing, you MUST get the user's Firebase token after they log in.
            // For now, we are bypassing this in Health.py
            // Get the REAL token from session storage
            const idToken = sessionStorage.getItem('firebaseIdToken'); 

            if (!idToken) {
                // If no token, user is not logged in. Send them back.
                alert("You are not logged in. Redirecting to login page.");
                window.location.href = "index.html";
                return;
            }

            const response = await fetch("http://127.0.0.1:5000/api/submit-screening", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    // We send a token, even if it's a test one
                    "Authorization": `Bearer ${idToken}` 
                },
                body: JSON.stringify(formData)
            });

            loading.style.display = "none";
            resultsContainer.style.display = "block";

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
            }

            // 4. Get the results back from the Python "brain"
            const triage_results = await response.json();

            // 5. Display the powerful results from the backend
            resultsContainer.innerHTML = "<h2>Your Sentinel Health Analysis</h2>";
            
            if (triage_results.length === 0) {
                 resultsContainer.innerHTML += "<p>No specific conditions matched. Please monitor your symptoms.</p>";
                 return;
            }
            
            triage_results.forEach(result => {
                const div = document.createElement("div");
                div.style.padding = "1rem";
                div.style.margin = "1rem 0";
                div.style.borderRadius = "8px";
                div.style.backgroundColor = getRiskColor(result.risk);

                div.innerHTML = `
                    <h3>${getRiskEmoji(result.risk)} ${result.risk.toUpperCase()} Risk</h3>
                    <h2>Potential Condition: ${result.disease_name}</h2>
                    <p><strong>Match Score:</strong> ${result.match_score}%</p>
                    <p><strong>Recommendation:</strong> ${result.info.recommendation}</p>
                    <p><strong>Education:</strong> ${result.info.education}</p>
                    <p><strong>Specialist:</strong> ${result.info.specialist}</p>
                `;
                resultsContainer.appendChild(div);
            });
// This shows the clinic finder button if risk is high
            const hasHighRisk = triage_results.some(r => r.risk === 'high' || r.risk === 'critical');
            const clinicsSection = document.getElementById('clinics-section');
            if (hasHighRisk) {
                clinicsSection.style.display = 'block';
            }
        } catch (error) {
            console.error("Error submitting screening:", error);
            loading.style.display = "none";
            resultsContainer.style.display = "block";
            resultsContainer.innerHTML = `<h3 style="color: red;">Error</h3>
                                          <p>Could not connect to the analysis server. Make sure your Python server is running.</p>
                                          <p>${error.message}</p>`;
        }
    });

    // Helper functions to make it look nice
    function getRiskColor(risk) {
        if (risk === "critical") return "#f8d7da";
        if (risk === "high") return "#f8d7da";
        if (risk === "medium") return "#fff3cd";
        return "#d4edda"; // low
    }
    
    function getRiskEmoji(risk) {
        if (risk === "critical") return "🚨";
        if (risk === "high") return "🔴";
        if (risk === "medium") return "🟡";
        return "🟢"; // low
    }

    // You still need your Firebase init and logout button logic here
    // e.g., document.getElementById("logout-btn")...
    // --- ✅ PASTE THIS ENTIRE BLOCK OF CODE HERE ---

    const findClinicsBtn = document.getElementById('find-clinics-btn');
    const clinicsListDiv = document.getElementById('clinics-list');

    // This runs when the user clicks the "Find Nearby Clinics" button
    findClinicsBtn.addEventListener('click', () => {
        // 1. Check if the browser can do GPS
        if (!navigator.geolocation) {
            clinicsListDiv.innerHTML = '<p style="color: red;">Geolocation is not supported by your browser.</p>';
            return;
        }

        clinicsListDiv.innerHTML = '<p>Getting your location...</p>';
        findClinicsBtn.disabled = true; // Prevent multiple clicks
        findClinicsBtn.textContent = 'Locating...';

        // 2. Get User's GPS Location
        navigator.geolocation.getCurrentPosition(async (position) => {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            clinicsListDiv.innerHTML = '<p>Finding nearby clinics...</p>';

            // 3. Get the auth token (keycard)
            // We use the SAME token from when we submitted the form
            const idToken = sessionStorage.getItem('firebaseIdToken'); 
            if (!idToken) {
                // This check is a failsafe from when we did the login page
                clinicsListDiv.innerHTML = '<p style="color: red;">You are not logged in.</p>';
                findClinicsBtn.disabled = false;
                findClinicsBtn.textContent = 'Find Nearby Clinics';
                return;
            }

            try {
                // 4. Call your Python API endpoint
                const response = await fetch("http://127.0.0.1:5000/api/find-nearby-clinics", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${idToken}` // Use the real token
                    },
                    body: JSON.stringify({
                        latitude: latitude,
                        longitude: longitude
                    })
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
                }

                const clinics = await response.json();

                // 5. Display the results
                if (clinics.length === 0) {
                    clinicsListDiv.innerHTML = '<p>No clinics found within a 50km radius.</p>';
                    return;
                }

                clinicsListDiv.innerHTML = '<h4>Clinics Found Near You:</h4>'; // Clear loading message
                
                clinics.forEach(clinic => {
                    clinicsListDiv.innerHTML += `
                        <div style="border: 1px solid #ddd; padding: 1rem; margin-bottom: 1rem; border-radius: 8px;">
                            <strong>${clinic.name}</strong>
                            <p>${clinic.address}</p>
                            <p style="display: flex; justify-content: space-between;">
                                <span><strong>Rating:</strong> ${clinic.rating || 'N/A'}</span>
                                <span>${getOpenStatus(clinic.is_open)}</span>
                            </p>
                        </div>
                    `;
                });

            } catch (error) {
                console.error("Error finding clinics:", error);
                clinicsListDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
            } finally {
                findClinicsBtn.disabled = false;
                findClinicsBtn.textContent = 'Find Nearby Clinics';
            }
        }, (error) => {
            // This runs if user denies location access
            clinicsListDiv.innerHTML = '<p style="color: red;">Could not get your location. Please enable location access in your browser settings.</p>';
            findClinicsBtn.disabled = false;
            findClinicsBtn.textContent = 'Find Nearby Clinics';
        });
    });

    // Helper function to make the open status look nice
    function getOpenStatus(isOpen) {
        if (isOpen === true) return '<strong style="color: green;">● Currently Open</strong>';
        if (isOpen === false) return '<strong style="color: red;">● Currently Closed</strong>';
        return '<strong>Status Unknown</strong>';
    }

    // --- END OF THE CODE TO PASTE ---
});
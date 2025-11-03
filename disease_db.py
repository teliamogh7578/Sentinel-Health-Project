# This is your "database" of disease knowledge.
# It has been modified to support age-specific risk and recommendations.

DISEASE_KNOWLEDGE_BASE = {

    # --- 🦠 COMMUNICABLE DISEASES ---
    # (Diseases that can spread)

    "dengue": {
        "symptoms": ["fever", "headache", "rash", "muscle pain", "joint pain"],
        "type": "communicable",
        "specialist": "General Practitioner / Hospital",
        "base_risk": {
            "infant": "critical",
            "child": "high",
            "teen": "high",
            "adult": "high",
            "senior": "high"
        },
        "education": {
            "default": "Dengue is spread by mosquitoes. To prevent it, remove any stagnant water around your home (like in buckets, pots, or old tires) where mosquitoes can breed."
        },
        "recommendation": {
            "infant": "Urgent: Go to the hospital immediately. High fever in infants can be very dangerous.",
            "default": "Urgent: See a doctor immediately for a blood test. Rest and drink plenty of fluids. Monitor for warning signs like severe abdominal pain or bleeding."
        }
    },
    "common_cold": {
        "symptoms": ["sore throat", "cough", "runny nose"],
        "type": "communicable",
        "specialist": "None (Self-care)",
        "base_risk": {
            "infant": "medium",
            "child": "low",
            "teen": "low",
            "adult": "low",
            "senior": "low"
        },
        "education": {
            "default": "A cold is a virus. The best treatment is rest, fluids, and managing symptoms. Antibiotics will not work.",
            "infant": "A cold in an infant can be serious. Use a nasal aspirator to clear their nose so they can breathe and feed. Use a cool-mist humidifier."
        },
        "recommendation": {
            "infant": "Monitor closely. See a doctor if the baby has a fever over 100.4°F (38°C), has trouble breathing, or refuses to eat.",
            "default": "Rest at home, drink warm fluids, and manage symptoms with over-the-counter medicine if needed.",
            "senior": "Rest and hydrate. See a doctor if the cough lingers or you develop a fever, as it could turn into pneumonia."
        }
    },
    "influenza": {
        "symptoms": ["fever", "cough", "sore throat", "muscle pain", "body aches", "fatigue", "headache", "runny nose"],
        "type": "communicable",
        "specialist": "General Practitioner",
        "base_risk": {
            "infant": "high",
            "child": "medium",
            "teen": "medium",
            "adult": "medium",
            "senior": "high"
        },
        "education": {
            "default": "The flu is a contagious respiratory virus. The best prevention is a yearly flu shot. Wash your hands frequently."
        },
        "recommendation": {
            "infant": "See a pediatrician immediately. Flu can be very dangerous for infants.",
            "default": "Rest, stay hydrated. See a doctor if you have trouble breathing, chest pain, or a very high fever that persists.",
            "senior": "See a doctor. Seniors are at high risk for complications like pneumonia. Antiviral medication may be an option."
        }
    },
    "covid_19": {
        "symptoms": ["fever", "cough", "fatigue", "loss of taste", "loss of smell", "shortness of breath", "sore throat"],
        "type": "communicable",
        "specialist": "General Practitioner / Hospital",
        "base_risk": {
            "infant": "high",
            "child": "medium",
            "teen": "medium",
            "adult": "medium",
            "senior": "high"
        },
        "education": {
            "default": "COVID-19 is a highly contagious virus. Prevention includes vaccination, hand washing, and wearing a mask in high-risk settings."
        },
        "recommendation": {
            "default": "Isolate yourself, rest, and hydrate. Seek urgent medical care if you have difficulty breathing, chest pain, or blue lips.",
            "senior": "Contact your doctor immediately, even with mild symptoms. You may be eligible for antiviral treatment. Seek urgent care for difficulty breathing."
        }
    },
    "strep_throat": {
        "symptoms": ["sore throat", "pain when swallowing", "fever", "swollen tonsils", "white spots on tonsils", "swollen lymph nodes"],
        "type": "communicable",
        "specialist": "General Practitioner / Urgent Care",
        "base_risk": {"default": "medium"},
        "education": {
            "default": "Strep throat is a bacterial infection. It is spread through airborne droplets from coughs or sneezes."
        },
        "recommendation": {
            "default": "See a doctor for a rapid strep test. If positive, you will need antibiotics. Finish the full course to prevent rheumatic fever."
        }
    },
    "food_poisoning": {
        "symptoms": ["nausea", "vomiting", "diarrhea", "stomach cramps", "fever"],
        "type": "communicable",
        "specialist": "None (Self-care) / General Practitioner",
        "base_risk": {
            "infant": "high",
            "child": "medium",
            "default": "low",
            "senior": "medium"
        },
        "education": {
            "default": "Caused by eating contaminated food. Prevent by washing hands, cooking food thoroughly, and refrigerating leftovers properly."
        },
        "recommendation": {
            "infant": "See a doctor. Dehydration from vomiting/diarrhea is extremely dangerous for infants.",
            "child": "Focus on hydration with electrolyte solutions (like Pedialyte). See a doctor if they can't keep liquids down or have a high fever.",
            "default": "Stay hydrated with water or electrolyte solutions. Symptoms usually pass in 1-2 days. See a doctor if you see blood or can't keep liquids down.",
            "senior": "Be very cautious with hydration. See a doctor if symptoms last more than a day, as dehydration can be severe."
        }
    },
    "conjunctivitis": {
        "symptoms": ["red eyes", "itchy eyes", "gritty feeling", "eye discharge", "crusty eyelids"],
        "type": "communicable",
        "specialist": "General Practitioner",
        "base_risk": {"default": "low"},
        "education": {
            "default": "Also known as 'pink eye,' it can be viral or bacterial and is very contagious. Wash hands often and do not share towels or pillows."
        },
        "recommendation": {
            "default": "See a doctor to determine if it's viral (must run its course) or bacterial (needs antibiotic drops). Stay home from school/work to avoid spreading."
        }
    },
    "uti": {
        "symptoms": ["painful urination", "burning sensation", "frequent urination", "urgent need to urinate", "cloudy urine", "pelvic pain"],
        "type": "communicable",
        "specialist": "General Practitioner / Urgent Care",
        "base_risk": {
            "infant": "high",
            "child": "medium",
            "default": "medium",
            "senior": "high"
        },
        "education": {
            "default": "A Urinary Tract Infection is a bacterial infection. Drink plenty of water to help flush bacteria. Wiping front-to-back can help prevent it."
        },
        "recommendation": {
            "infant": "See a doctor immediately. Symptoms might just be an unexplained fever or irritability.",
            "default": "See a doctor. You will likely need a urine test and a course of antibiotics. Do not delay, as it can spread to the kidneys.",
            "senior": "See a doctor immediately. UTIs in seniors can cause confusion and lead to serious bloodstream infections (sepsis)."
        }
    },
    "ringworm": {
        "symptoms": ["itchy rash", "ring-shaped rash", "red skin", "scaly skin", "cracked skin"],
        "type": "communicable",
        "specialist": "None (Self-care) / Pharmacist",
        "base_risk": {"default": "low"},
        "education": {
            "default": "Ringworm is a common fungal infection of the skin (not a worm). It's spread by skin-to-skin contact or touching contaminated items (towels, gym mats)."
        },
        "recommendation": {
            "default": "Keep the area clean and dry. Use an over-the-counter antifungal cream as directed."
        }
    },
    "gastroenteritis": {
        "symptoms": ["diarrhea", "vomiting", "nausea", "stomach cramps", "fever", "headache"],
        "type": "communicable",
        "specialist": "General Practitioner (if dehydration is severe)",
        "base_risk": {
            "infant": "high",
            "child": "medium",
            "default": "low",
            "senior": "medium"
        },
        "education": {
            "default": "Often called the 'stomach flu,' this is an inflammation of the stomach and intestines, usually caused by a virus (like Norovirus) or bacteria."
        },
        "recommendation": {
            "infant": "See a doctor. Dehydration is a major risk.",
            "child": "Focus on hydration with electrolyte solutions. See a doctor if they can't keep liquids down.",
            "default": "The biggest risk is dehydration. Sip small amounts of water or electrolyte drinks. Gradually reintroduce bland foods (BRAT diet: bananas, rice, applesauce, toast).",
            "senior": "Monitor for dehydration closely. See a doctor if symptoms persist, as you are more susceptible to complications."
        }
    },
    "chickenpox": {
        "symptoms": ["itchy rash", "blisters", "fever", "fatigue", "headache", "loss of appetite"],
        "type": "communicable",
        "specialist": "General Practitioner / Pediatrician",
        "base_risk": {
            "infant": "high",
            "child": "medium",
            "teen": "medium",
            "adult": "high",
            "senior": "high"
        },
        "education": {
            "default": "Chickenpox is caused by the varicella-zoster virus. It's highly contagious until all blisters have scabbed over. A vaccine is available."
        },
        "recommendation": {
            "infant": "See a doctor immediately.",
            "child": "Stay home to avoid spreading. Use calamine lotion and lukewarm oatmeal baths for itching. Do NOT give aspirin.",
            "default": "Stay home. Be aware that chickenpox in adults can be much more severe than in children. See a doctor if you develop a severe cough or breathing issues."
        }
    },
    "malaria": {
        "symptoms": ["high fever", "chills", "sweating", "headache", "nausea", "muscle pain", "fatigue"],
        "type": "communicable",
        "specialist": "Hospital / Infectious Disease Specialist",
        "base_risk": {"default": "high"},  # High for everyone
        "education": {
            "default": "Malaria is spread by infected mosquitoes, often found in tropical areas. Prevent by using mosquito nets, repellent, and antimalarial drugs if traveling."
        },
        "recommendation": {
            "default": "This is a medical emergency. Seek immediate medical care if you have these symptoms, especially after travel."
        }
    },
    "tuberculosis": {
        "symptoms": ["persistent cough", "coughing up blood", "chest pain", "night sweats", "fever", "weight loss", "fatigue"],
        "type": "communicable",
        "specialist": "Hospital / Pulmonologist",
        "base_risk": {"default": "high"},
        "education": {
            "default": "TB is a serious bacterial infection that affects the lungs. It is spread through the air when an infected person coughs or sneezes."
        },
        "recommendation": {
            "default": "Seek immediate medical attention if you have these symptoms, especially a persistent cough with blood. Treatment is long but effective."
        }
    },
    "mononucleosis": {
        "symptoms": ["extreme fatigue", "sore throat", "fever", "swollen lymph nodes", "swollen spleen", "headache"],
        "type": "communicable",
        "specialist": "General Practitioner",
        "base_risk": {"default": "medium"},
        "education": {
            "default": "Often called 'mono' or 'the kissing disease,' it's a virus spread through saliva. Avoid sharing drinks, utensils, or kissing."
        },
        "recommendation": {
            "default": "See a doctor. The main treatment is rest, fluids, and patience. Avoid contact sports for 4-6 weeks to protect your spleen."
        }
    },
    "scabies": {
        "symptoms": ["intense itching", "pimple-like rash", "burrow tracks", "itching worse at night"],
        "type": "communicable",
        "specialist": "General Practitioner / Dermatologist",
        "base_risk": {"default": "low"},
        "education": {
            "default": "Caused by a tiny mite that burrows into the skin. It spreads by prolonged skin-to-skin contact."
        },
        "recommendation": {
            "default": "See a doctor. You will need a prescription cream or lotion to kill the mites. Wash all bedding and clothing in hot water."
        }
    },
    "rabies": {
        "symptoms": ["fever","nausea","confusion", "agitation", "hydrophobia"],
        "type": "communicable",
        "specialist": "Hospital / Emergency Room",
        "base_risk": {"default": "critical"},  # Critical for all
        "education": {
            "default": "A deadly virus spread to people from the saliva of infected animals, usually through a bite. Always be cautious around wild animals."
        },
        "recommendation": {
            "default": "If bitten by any animal (wild or domestic), wash the wound immediately with soap and water for 15 minutes and go to the hospital IMMEDIATELY. Post-exposure treatment is 100% effective if given right away."
        }
    },
    "cholera": {
        "symptoms": ["profuse watery diarrhea", "vomiting", "leg cramps", "dehydration"],
        "type": "communicable",
        "specialist": "Hospital / Emergency Room",
        "base_risk": {"default": "high"},
        "education": {
            "default": "A bacterial disease spread through contaminated water. It's common in areas with poor sanitation."
        },
        "recommendation": {
            "default": "This is a medical emergency. Severe dehydration can be fatal. Seek medical help immediately for rehydration fluids (oral or IV)."
        }
    },
    "hepatitis_a": {
        "symptoms": ["fatigue", "nausea", "vomiting", "jaundice", "dark urine", "fever", "loss of appetite"],
        "type": "communicable",
        "specialist": "General Practitioner",
        "base_risk": {"default": "medium"},
        "education": {
            "default": "A viral liver infection spread through contaminated food or water (fecal-oral route). A vaccine is available."
        },
        "recommendation": {
            "default": "See a doctor for a blood test. There is no specific treatment, so rest and managing symptoms is key. Your liver will heal over time."
        }
    },
    "impetigo": {
        "symptoms": ["red sores", "honey-colored crusts", "blisters", "itchy rash"],
        "type": "communicable",
        "specialist": "Pediatrician / General Practitioner",
        "base_risk": {"default": "low"},
        "education": {
            "default": "A common and contagious skin infection (bacterial), especially in young children. Spread through direct contact or sharing items."
        },
        "recommendation": {
            "default": "See a doctor. You will need a prescription antibiotic ointment or pills. Keep the area clean and covered."
        }
    },
    "head_lice": {
        "symptoms": ["intense itching", "tickling feeling", "visible nits (eggs)", "visible lice"],
        "type": "communicable",
        "specialist": "None (Self-care) / Pharmacist",
        "base_risk": {"default": "low"},
        "education": {
            "default": "Tiny insects that feed on blood from the scalp. They spread by head-to-head contact or sharing hats, brushes, or pillows."
        },
        "recommendation": {
            "default": "Use an over-the-counter medicated shampoo (pediculicide). Use a fine-toothed nit comb to remove all eggs."
        }
    },

    # --- 🩺 NON-COMMUNICABLE DISEASES ---
    # (Chronic, lifestyle, genetic, or environmental diseases)

    "anaemia": {
        "symptoms": ["lethargy", "fatigue", "pale skin", "weakness", "dizziness", "shortness of breath", "cold hands"],
        "type": "non-communicable",
        "specialist": "General Practitioner",
        "base_risk": {
            "infant": "high",
            "child": "medium",
            "teen": "medium",
            "adult": "medium",
            "senior": "high"
        },
        "education": {
            "default": "Anaemia is often caused by a lack of iron. Good food sources of iron include red meat, spinach, lentils, and fortified cereals.",
            "infant": "Anaemia in babies can be serious. Ensure they are getting iron-fortified formula or cereal. Talk to your pediatrician.",
            "teen": "Teenagers, especially girls after starting their period, have higher iron needs.",
            "senior": "Anaemia in seniors is common but should always be investigated by a doctor, as it can be a sign of a more serious underlying issue."
        },
        "recommendation": {
            "infant": "See a pediatrician for a blood test. Do not give any supplements without a doctor's prescription.",
            "default": "Schedule a doctor's visit for a blood test. Do not take iron pills unless prescribed by a doctor.",
            "senior": "Schedule a doctor's visit for a blood test. It's important to find the cause, not just treat the symptom."
        }
    },
    "myopia": {
        "symptoms": ["squinting", "headache", "blurry vision", "trouble seeing far", "eye strain"],
        "type": "non-communicable",
        "specialist": "Optician / Optometrist",
        "base_risk": {"default": "low"},  # Low risk, but needs correction
        "education": {
            "default": "Myopia, or nearsightedness, is common. To reduce eye strain, use the 20-20-20 rule: Every 20 minutes, look at something 20 feet away for 20 seconds.",
            "child": "Myopia in children can get worse over time. Encourage outdoor play, which is shown to slow progression. Limit screen time."
        },
        "recommendation": {
            "default": "Schedule a visit with an eye doctor for a comprehensive exam.",
            "child": "Schedule a visit with an eye doctor. It is important to get this corrected so it does not interfere with learning."
        }
    },
    "asthma": {
        "symptoms": ["wheezing", "shortness of breath", "chest tightness", "coughing"],
        "type": "non-communicable",
        "specialist": "General Practitioner / Pulmonologist",
        "base_risk": {"default": "medium"},
        "education": {
            "default": "Asthma is a chronic condition where airways narrow and swell. Identify and avoid your triggers (e.g., pollen, dust, exercise, cold air)."
        },
        "recommendation": {
            "default": "See a doctor to get a proper diagnosis and a rescue inhaler (like Albuterol). A long-term controller medication may also be needed. A severe, unstoppable attack is an emergency."
        }
    },
    "hypertension": {
        "symptoms": ["often none", "headache", "dizziness", "shortness of breath", "nosebleeds", "blurry vision"],
        "type": "non-communicable",
        "specialist": "General Practitioner / Cardiologist",
        "base_risk": {"default": "medium"},
        "education": {
            "default": "High blood pressure ('Hypertension') is often called the 'silent killer' because it has no symptoms. Manage it with a low-salt diet, regular exercise, and stress reduction."
        },
        "recommendation": {
            "default": "Get your blood pressure checked regularly (at a pharmacy or clinic). See a doctor to create a management plan, which may include medication."
        }
    },
    "type_2_diabetes": {
        "symptoms": ["excessive thirst", "frequent urination", "blurry vision", "fatigue", "hunger", "slow-healing sores", "tingling in feet"],
        "type": "non-communicable",
        "specialist": "General Practitioner / Endocrinologist",
        "base_risk": {"default": "medium"},
        "education": {
            "default": "This is a condition where your body doesn't use insulin properly, leading to high blood sugar. It can often be managed or prevented with diet, exercise, and weight loss."
        },
        "recommendation": {
            "default": "See a doctor for a blood sugar test (A1C). Lifestyle changes are the first line of defense. Medication may be needed."
        }
    },
    "migraine": {
        "symptoms": ["severe headache", "throbbing pain", "nausea", "vomiting", "sensitivity to light", "sensitivity to sound", "aura"],
        "type": "non-communicable",
        "specialist": "General Practitioner / Neurologist",
        "base_risk": {"default": "medium"},
        "education": {
            "default": "A migraine is more than a bad headache; it's a neurological condition. Keep a journal to identify your triggers (e.g., stress, certain foods, lack of sleep, hormonal changes)."
        },
        "recommendation": {
            "default": "Rest in a dark, quiet room. Over-the-counter pain relievers may work, but see a doctor for prescription triptans if they don't."
        }
    },
    "gerd": {
        "symptoms": ["heartburn", "acid reflux", "chest pain", "regurgitation", "difficulty swallowing", "chronic cough", "sour taste"],
        "type": "non-communicable",
        "specialist": "General Practitioner / Gastroenterologist",
        "base_risk": {"default": "low"},
        "education": {
            "default": "Acid reflux (GERD) is when stomach acid flows back into your esophagus. Avoid trigger foods (spicy, fatty, coffee, alcohol), and don't lie down for 3 hours after eating."
        },
        "recommendation": {
            "default": "Try over-the-counter antacids or H2 blockers. If symptoms persist for more than 2 weeks, see a doctor to prevent damage to your esophagus."
        }
    },
    "anxiety_disorder": {
        "symptoms": ["excessive worry", "restlessness", "fatigue", "difficulty concentrating", "irritability", "muscle tension", "panic attacks", "sleep problems"],
        "type": "non-communicable",
        "specialist": "Therapist / Psychologist / Psychiatrist",
        "base_risk": {"default": "medium"},
        "education": {
            "default": "Anxiety is a normal emotion, but a disorder involves persistent, excessive fear that interferes with daily life. Deep breathing exercises and mindfulness can help manage symptoms."
        },
        "recommendation": {
            "default": "Talk to a trusted friend or family member. See a doctor or a mental health professional (therapist) for a diagnosis and treatment plan (therapy, medication, or both)."
        }
    },
    "depression": {
        "symptoms": ["persistent sadness", "loss of interest", "fatigue", "changes in sleep", "changes in appetite", "feelings of worthlessness", "difficulty concentrating"],
        "type": "non-communicable",
        "specialist": "Therapist / Psychologist / Psychiatrist",
        "base_risk": {"default": "high"},
        "education": {
            "default": "Depression is a serious medical illness that negatively affects how you feel, think, and act. It is treatable and is not a sign of weakness."
        },
        "recommendation": {
            "default": "This is not something to 'tough out.' Please talk to a doctor or a mental health professional. If you have thoughts of self-harm, call an emergency hotline immediately."
        }
    },
    "kidney_stones": {
        "symptoms": ["severe pain in side", "severe pain in back", "pain radiating to groin", "painful urination", "nausea", "vomiting", "blood in urine", "fever", "chills"],
        "type": "non-communicable",
        "specialist": "Urgent Care / Hospital / Urologist",
        "base_risk": {"default": "high"},
        "education": {
            "default": "Kidney stones are hard deposits made of minerals and salts. The main cause is not drinking enough water. Certain diets (high in sodium, protein) can contribute."
        },
        "recommendation": {
            "default": "This can be extremely painful. See a doctor immediately or go to urgent care, especially if you have a fever (which could mean an infection)."
        }
    },
    "osteoarthritis": {
        "symptoms": ["joint pain", "stiffness", "tenderness", "loss of flexibility", "grating sensation", "bone spurs", "pain worse after activity"],
        "type": "non-communicable",
        "specialist": "General Practitioner / Orthopedist",
        "base_risk": {"default": "low"},
        "education": {
            "default": "This is the 'wear-and-tear' type of arthritis, common in older adults or after joint injuries. Low-impact exercise (like swimming or walking) can strengthen muscles and help."
        },
        "recommendation": {
            "default": "Manage with over-the-counter pain relievers (like ibuprofen), heat/ice, and by staying active. See a doctor if pain limits your daily life."
        }
    },
    "vitamin_d_deficiency": {
        "symptoms": ["fatigue", "bone pain", "muscle weakness", "mood changes", "getting sick often", "hair loss"],
        "type": "non-communicable",
        "specialist": "General Practitioner",
        "base_risk": {"default": "low"},
        "education": {
            "default": "Your body produces Vitamin D from sunlight. It's hard to get enough from food alone. Many people are deficient, especially in winter or with darker skin."
        },
        "recommendation": {
            "default": "See a doctor for a simple blood test. Do not take high-dose supplements unless a deficiency is confirmed by your doctor."
        }
    },
    "eczema": {
        "symptoms": ["itchy skin", "dry skin", "red patches", "scaly skin", "skin inflammation", "oozing or crusting"],
        "type": "non-communicable",
        "specialist": "General Practitioner / Dermatologist",
        "base_risk": {"default": "low"},
        "education": {
            "default": "A chronic condition (atopic dermatitis) that causes the skin to become itchy and inflamed. Identify and avoid triggers (like certain soaps, fabrics, or stress)."
        },
        "recommendation": {
            "default": "Keep skin well-moisturized with a thick, unscented cream (like petroleum jelly). Avoid long, hot showers. See a doctor for prescription steroid creams if needed."
        }
    },
    "insomnia": {
        "symptoms": ["difficulty falling asleep", "waking up at night", "waking up too early", "fatigue", "irritability", "difficulty concentrating"],
        "type": "non-communicable",
        "specialist": "General Practitioner",
        "base_risk": {"default": "low"},
        "education": {
            "default": "Insomnia is a common sleep disorder. Practice good 'sleep hygiene': go to bed at the same time, avoid screens before bed, avoid caffeine late in the day, and create a dark, quiet room."
        },
        "recommendation": {
            "default": "Try improving sleep hygiene for 1-2 weeks. If it doesn't help, see a doctor. Do not rely on over-the-counter sleep aids long-term."
        }
    },
    "psoriasis": {
        "symptoms": ["red patches", "silvery scales", "dry skin", "cracked skin", "itchy skin", "joint pain"],
        "type": "non-communicable",
        "specialist": "Dermatologist / Rheumatologist",
        "base_risk": {"default": "medium"},
        "education": {
            "default": "An autoimmune condition that causes skin cells to build up rapidly, forming scales. It is not contagious. Stress and cold weather can be triggers."
        },
        "recommendation": {
            "default": "See a doctor or dermatologist for diagnosis. Treatment can include medicated creams, light therapy, or oral medications."
        }
    },
    "celiac_disease": {
        "symptoms": ["diarrhea", "bloating", "gas", "fatigue", "weight loss", "abdominal pain", "skin rash", "anaemia"],
        "type": "non-communicable",
        "specialist": "Gastroenterologist",
        "base_risk": {"default": "medium"},
        "education": {
            "default": "An autoimmune disorder where eating gluten (found in wheat, barley, and rye) damages the small intestine."
        },
        "recommendation": {
            "default": "Do NOT start a gluten-free diet yet. See a doctor for a blood test and diagnosis first. Starting the diet can make the test inaccurate."
        }
    },
    "appendicitis": {
        "symptoms": ["abdominal pain", "pain starting near navel", "pain moving to lower right", "loss of appetite", "nausea", "vomiting", "fever"],
        "type": "non-communicable",
        "specialist": "Hospital / Emergency Room / Surgeon",
        "base_risk": {"default": "critical"},
        "education": {
            "default": "An inflammation of the appendix, a small pouch attached to the large intestine. The cause is often unknown."
        },
        "recommendation": {
            "default": "This is a medical emergency. Go to the hospital or emergency room immediately. A burst appendix can be life-threatening."
        }
    },
    "glaucoma": {
        "symptoms": ["often none", "gradual loss of vision", "tunnel vision", "severe eye pain", "nausea", "halos around lights"],
        "type": "non-communicable",
        "specialist": "Ophthalmologist",
        "base_risk": {"default": "high"},
        "education": {
            "default": "A group of eye conditions that damage the optic nerve, often caused by high pressure in the eye. It can cause blindness if untreated."
        },
        "recommendation": {
            "default": "Get regular, comprehensive eye exams. Sudden, severe eye pain with nausea is an emergency—go to the ER."
        }
    },
    "crohns_disease": {
        "symptoms": ["diarrhea", "abdominal pain", "cramping", "blood in stool", "weight loss", "fatigue"],
        "type": "non-communicable",
        "specialist": "Gastroenterologist",
        "base_risk": {"default": "high"},
        "education": {
            "default": "A type of inflammatory bowel disease (IBD) that causes chronic inflammation of the digestive tract. It's an autoimmune condition."
        },
        "recommendation": {
            "default": "See a doctor if you have persistent changes in your bowel habits, especially with abdominal pain or blood."
        }
    },
    "gout": {
        "symptoms": ["severe joint pain", "intense joint pain", "redness", "swelling", "sudden attack of pain", "often in big toe"],
        "type": "non-communicable",
        "specialist": "General Practitioner / Rheumatologist",
        "base_risk": {"default": "medium"},
        "education": {
            "default": "A type of arthritis caused by a buildup of uric acid crystals in a joint. Attacks can be triggered by foods high in purines (like red meat, seafood) and alcohol."
        },
        "recommendation": {
            "default": "See a doctor during an attack for anti-inflammatory medication. Long-term medication can lower uric acid levels."
        }
    },
    "endometriosis": {
        "symptoms": ["painful periods", "pelvic pain", "pain during intercourse", "heavy bleeding", "infertility", "pain with bowel movements"],
        "type": "non-communicable",
        "specialist": "Gynecologist",
        "base_risk": {"default": "high"},
        "education": {
            "default": "A condition where tissue similar to the lining of the uterus grows outside the uterus. The pain is often dismissed as 'bad cramps.'"
        },
        "recommendation": {
            "default": "See a gynecologist if you have severe period pain that interferes with your life. Do not dismiss it as 'normal.'"
        }
    },
    "pcos": {
        "symptoms": ["irregular periods", "no periods", "heavy periods", "excess hair growth", "acne", "weight gain", "infertility"],
        "type": "non-communicable",
        "specialist": "Gynecologist / Endocrinologist",
        "base_risk": {"default": "medium"},
        "education": {
            "default": "Polycystic Ovary Syndrome is a hormonal disorder common among women of reproductive age. It can be managed with lifestyle changes and medication."
        },
        "recommendation": {
            "default": "See a doctor or gynecologist if you have very irregular periods or other symptoms. It's a manageable condition."
        }
    },
    "carpal_tunnel": {
        "symptoms": ["numbness", "tingling", "weakness", "pain in hand", "pain in wrist", "pain in forearm", "dropping objects"],
        "type": "non-communicable",
        "specialist": "General Practitioner / Orthopedist",
        "base_risk": {"default": "low"},
        "education": {
            "default": "Caused by pressure on the median nerve in your wrist. It's often related to repetitive hand motions, like typing or using tools."
        },
        "recommendation": {
            "default": "Try to rest your wrist, wear a wrist splint at night, and do gentle stretching exercises. See a doctor if it persists."
        }
    },
    "tension_headache": {
        "symptoms": ["dull ache", "headache", "pressure around forehead", "tenderness on scalp", "neck pain"],
        "type": "non-communicable",
        "specialist": "None (Self-care)",
        "base_risk": {"default": "low"},
        "education": {
            "default": "The most common type of headache, often caused by muscle tension, stress, or eye strain. Not as severe as a migraine."
        },
        "recommendation": {
            "default": "Over-the-counter pain relievers (like ibuprofen or acetaminophen) work well. Stretching, massage, and managing stress can prevent them."
        }
    }
}
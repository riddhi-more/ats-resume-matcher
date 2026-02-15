📄 ats-resume-matcher

A simple Flask web app that compares a resume with a job description and calculates an ATS (Applicant Tracking System) match score using NLP techniques. It also highlights missing keywords and generates an improved resume version with suggested additions.

🚀 Features

Compare resume vs job description

Calculate ATS match score (%) using TF-IDF + cosine similarity

Identify missing keywords from the job description

Generate an improved resume with added keywords

Simple web UI using Flask templates

🧠 How It Works

User pastes a job description and resume into the web form

App converts both texts into vectors using TF-IDF

Calculates similarity score using cosine similarity

Extracts missing keywords from the job description

Returns:

Match score

Missing keywords

Improved resume with added keywords

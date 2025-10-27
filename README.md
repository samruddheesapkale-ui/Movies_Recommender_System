🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python, Scikit-learn, Streamlit, and TMDb API.
It suggests similar movies based on your selected choice using cosine similarity on movie metadata.

🚀 Live Demo

👉 Click this link to try it out:
https://moviesrecommendersystem-85a5nnk7p3wlelzqlxkgeu.streamlit.app/

📖 Overview

This project recommends movies similar to a selected movie by comparing key features such as genres, cast, director, and keywords.
The recommendation is powered by cosine similarity on preprocessed movie data.

🧠 Tech Stack

1. Python

2. Streamlit – Front-end web app

3. Pandas / NumPy – Data manipulation

4. Scikit-learn – Similarity computation

5. TMDb API – Fetching movie posters

6. Pickle – Model and data storage

⚙️ How It Works

- The dataset (movies metadata) is cleaned and combined.

- Important features are extracted — genres, keywords, cast, director.

- A bag of words is created using CountVectorizer.

- Cosine Similarity is calculated between movies.

- When you select a movie, the system finds and displays the top 5 most similar movies with posters.

🧾 File Structure
├── app.py                  # Streamlit frontend
├── movies_dict.pkl         # Preprocessed movies dictionary
├── similarity.pkl          # Cosine similarity matrix
├── requirements.txt        # Dependencies
└── README.md               # Project documentation

🧩 Example Output

When you select Inception, the app might recommend:

Interstellar

The Prestige

The Matrix

Shutter Island

Memento

Each recommendation displays a poster fetched using the TMDb API.

💻 Run Locally

Clone the repository:

git clone https://github.com/your-username/Movie-Recommender-System.git


Navigate to the project folder:

cd Movie-Recommender-System


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

🌐 Live Application

Check it out here 👇
🔗 Movie Recommender App

🏅 Credits

Developed by Samruddhee Sapkale
Internship Project | Movie Recommendation System using Python and ML

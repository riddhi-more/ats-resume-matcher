from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    missing_keywords = []
    improved_resume = ""
    
    if request.method == "POST":
        jd = request.form["jd"]
        resume = request.form["resume"]

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([jd, resume])
        score = round(cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100, 2)

        jd_words = set(jd.lower().split())
        resume_words = set(resume.lower().split())
        missing_keywords = list(jd_words - resume_words)

        improved_resume = resume + "\n\n# Added Keywords:\n" + " ".join(missing_keywords)

    return render_template("index.html", score=score, missing=missing_keywords, improved_resume=improved_resume)

if __name__ == "__main__":
    app.run(debug=True)

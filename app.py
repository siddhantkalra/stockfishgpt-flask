from flask import Flask, request, render_template
from analyze import analyze_game
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    commentary = []
    pgn_text = ""
    
    if request.method == "POST":
        file = request.files["pgn_file"]
        if file and file.filename.endswith(".pgn"):
            pgn_text = file.read().decode("utf-8")
            commentary = analyze_game(pgn_text)

    return render_template("index.html", commentary=commentary, pgn=pgn_text)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, render_template
from analyze import analyze_game
import os
import chess.pgn
from io import StringIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    commentary = []
    pgn_text = ""
    final_fen = chess.Board().fen()  # Starting position by default

    if request.method == "POST":
        file = request.files["pgn_file"]
        if file and file.filename.endswith(".pgn"):
            pgn_text = file.read().decode("utf-8")
            commentary = analyze_game(pgn_text)

            game = chess.pgn.read_game(StringIO(pgn_text))
            final_board = game.end().board()
            final_fen = final_board.fen()

    return render_template("index.html", commentary=commentary, pgn=pgn_text, final_fen=final_fen)

if __name__ == "__main__":
    app.run(debug=True)

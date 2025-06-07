import chess.pgn
import chess.engine
import openai
import os
STOCKFISH_PATH = os.path.join(os.getcwd(), "engines", "stockfish")
from io import StringIO

# Load from environment variables (set via Codespaces or secrets manager)
openai.api_key = os.getenv("OPENAI_API_KEY")
STOCKFISH_PATH = "/usr/games/stockfish"  # adjust path if needed

def analyze_game(pgn_text):
    game = chess.pgn.read_game(StringIO(pgn_text))
    board = game.board()

    commentary = []
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)

    prev_eval = None
    move_number = 1

    for move in game.mainline_moves():
        board.push(move)
        info = engine.analyse(board, chess.engine.Limit(depth=15))
        score = info["score"].white().score(mate_score=10000)

        if prev_eval is not None:
            delta = abs(score - prev_eval)
            if delta > 100:
                comment = generate_commentary(board, move, prev_eval, score, move_number)
                commentary.append(comment)
        prev_eval = score
        move_number += 1

    engine.quit()
    return commentary

def generate_commentary(board, move, prev_eval, score, move_number):
    fen = board.fen()
    move_san = board.san(move)
    prompt = f"""
You're an expert chess coach. Evaluate the following:

- FEN: {fen}
- Move just played (move {move_number}): {move_san}
- Stockfish eval dropped from {prev_eval} to {score}

Explain why the move was inaccurate and what could have been played better. Be concise but instructive.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7,
        )
        explanation = response.choices[0].message.content.strip()
        return {
            "move": move_san,
            "eval_before": prev_eval,
            "eval_after": score,
            "comment": explanation
        }
    except Exception as e:
        return {
            "move": move_san,
            "eval_before": prev_eval,
            "eval_after": score,
            "comment": f"⚠️ Error generating comment: {str(e)}"
        }

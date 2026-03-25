# StockfishGPT

A chess game analyzer combining Stockfish engine with GPT-4o commentary. Upload a PGN file, get plain-English explanations of your mistakes and blunders.

---

## What It Does

- Upload any PGN file (exported from Chess.com, Lichess, or any client)
- Detects tactical mistakes and blunders based on evaluation score drops
- GPT-4o explains each error in plain language — positional context, what went wrong, what the better move was
- Interactive chess board UI in the browser

---

## Stack

- **Backend**: Python / Flask
- **Chess engine**: Stockfish
- **AI commentary**: OpenAI GPT-4o
- **Frontend**: HTML / JavaScript with interactive board

---

## Setup

```bash
# 1. Clone
git clone https://github.com/siddhantkalra/stockfishgpt-flask.git
cd stockfishgpt-flask

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your OpenAI key
export OPENAI_API_KEY=your-key-here

# 4. Run
python app.py
```

Then open [http://localhost:5000](http://localhost:5000), upload a PGN, and get your analysis.

Get an API key at [platform.openai.com](https://platform.openai.com).

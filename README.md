# StockfishGPT Flask Edition
# ♟️ StockfishGPT (Flask Version)

A lightweight chess game analyzer that combines the brute force of Stockfish with the language reasoning of GPT-4o.

## 🚀 Features
- Upload PGN files
- Detects mistakes/blunders based on eval drops
- GPT explains positional + tactical mistakes
- Clean UI via HTML/Flask
- Works locally or on Codespaces

## 🧪 Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your-api-key
python app.py
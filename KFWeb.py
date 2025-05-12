from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

# Set this to None until they win a game
last_win_date = None  # Example: date(2025, 5, 25)

@app.route("/")
def home():
    return render_template("index.html", last_win_date=last_win_date)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # Render uses port 10000 by default
    app.run(debug=True, host="0.0.0.0", port=port)

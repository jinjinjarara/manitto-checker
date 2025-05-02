from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

participants = ["Eunjin", "Taelim", "Caro", "Tungku", "Ari", "Jungho"]
manitto_mapping = {}

def generate_mapping():
    shuffled = participants.copy()
    while True:
        random.shuffle(shuffled)
        if all(a != b for a, b in zip(participants, shuffled)):
            break
    return dict(zip(participants, shuffled))

manitto_mapping = generate_mapping()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_manitto", methods=["POST"])
def get_manitto():
    data = request.get_json()
    name = data.get("name", "").strip()
    if name not in manitto_mapping:
        return jsonify({"error": "This name is not registered."}), 400
    return jsonify({"manitto": manitto_mapping[name]})

if __name__ == "__main__":
    app.run()

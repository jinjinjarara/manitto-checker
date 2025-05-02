
from flask import Flask, request, jsonify, render_template
import difflib

app = Flask(__name__)

manitto_mapping = {
    "Maëlle Garnier": {
        "target": "Annabel Heberle",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🕰 What’s your favorite moment of the day these days?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "안지민": {
        "target": "Valentin Vota",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "방도윤": {
        "target": "Lei Yuchen",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🗣 Do you have a phrase or expression you say a lot these days?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "mathias": {
        "target": "안지민",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🗣 Do you have a phrase or expression you say a lot these days?",
            "🕰 What’s your favorite moment of the day these days?"
        ]
    },
    "Annabel Heberle": {
        "target": "김채린",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "Alexandre Andtbacka(LOOP)": {
        "target": "방도윤",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "Valentin Vota": {
        "target": "mathias",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "김채린": {
        "target": "Alexandre Andtbacka(LOOP)",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "Lei Yuchen": {
        "target": "Maëlle Garnier",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🌴 If you could go on vacation right now, where would you go?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "Anja Zachariasen": {
        "target": "Haidar",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "Malina": {
        "target": "Anja Zachariasen",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🕰 What’s your favorite moment of the day these days?"
        ]
    },
    "Calvin Lieu": {
        "target": "조현서(LOOP)",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "Haidar": {
        "target": "Malina",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🕰 What’s your favorite moment of the day these days?"
        ]
    },
    "Quentin": {
        "target": "Me Cota",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🕰 What’s your favorite moment of the day these days?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "Me Cota": {
        "target": "김한슬",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🎧 What song or artist have you been listening to lately?"
        ]
    },
    "조현서(LOOP)": {
        "target": "Quentin",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "김한슬": {
        "target": "Calvin Lieu",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "음진희": {
        "target": "이지원",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🗣 Do you have a phrase or expression you say a lot these days?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "leon vicari": {
        "target": "Annate",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "Antonio Carusillo": {
        "target": "Ba Lam Nguyen",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🕰 What’s your favorite moment of the day these days?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "박수하(LOOP)": {
        "target": "김다경",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "김다경": {
        "target": "leon vicari",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🗣 Do you have a phrase or expression you say a lot these days?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "Annate": {
        "target": "박수하(LOOP)",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "Ba Lam Nguyen": {
        "target": "음진희",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "이지원": {
        "target": "Antonio Carusillo",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "Hannes": {
        "target": "윤제",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🕰 What’s your favorite moment of the day these days?"
        ]
    },
    "Gabriel": {
        "target": "Carolin Barth",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🎧 What song or artist have you been listening to lately?"
        ]
    },
    "김연우": {
        "target": "Jessica Schenkelberg",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "Iris Qoshi": {
        "target": "틍쿠",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "Jessica Schenkelberg": {
        "target": "Iris Qoshi",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🕰 What’s your favorite moment of the day these days?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "이민규": {
        "target": "김연우",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🕰 What’s your favorite moment of the day these days?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "Carolin Barth": {
        "target": "Hannes",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "틍쿠": {
        "target": "Gabriel",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "윤제": {
        "target": "이민규",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "윤민식": {
        "target": "Lucas",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "박소현": {
        "target": "Octave Guerini",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🕰 What’s your favorite moment of the day these days?"
        ]
    },
    "Laura Hauser": {
        "target": "Kellian",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🕰 What’s your favorite moment of the day these days?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "Kellian": {
        "target": "Vittorio Ventanni",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "🎧 What song or artist have you been listening to lately?"
        ]
    },
    "Vittorio Ventanni": {
        "target": "정수아",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🗣 Do you have a phrase or expression you say a lot these days?",
            "🎧 What song or artist have you been listening to lately?"
        ]
    },
    "Lucas": {
        "target": "윤민식",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🌴 If you could go on vacation right now, where would you go?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "Octave Guerini": {
        "target": "박소현",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "정수아": {
        "target": "Laura Hauser",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "🎧 What song or artist have you been listening to lately?"
        ]
    },
    "Louis Moretti": {
        "target": "Edanur Atak",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "신현서": {
        "target": "박소윤",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "Mounia Nasser": {
        "target": "Linus Knohl",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "Robin Ruault": {
        "target": "신현서",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "Linus Knohl": {
        "target": "Louis Moretti",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🌴 If you could go on vacation right now, where would you go?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "Edanur Atak": {
        "target": "조은진",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🌴 If you could go on vacation right now, where would you go?",
            "🕰 What’s your favorite moment of the day these days?"
        ]
    },
    "조은진": {
        "target": "Mounia Nasser",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🌴 If you could go on vacation right now, where would you go?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "박소윤": {
        "target": "Robin Ruault",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "Sabrina Barth": {
        "target": "오정원",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🎧 What song or artist have you been listening to lately?"
        ]
    },
    "Alejandre": {
        "target": "Nadyrkhano(알리나)",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "Anna Krikun": {
        "target": "Frank",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🗣 Do you have a phrase or expression you say a lot these days?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "Nadyrkhano(알리나)": {
        "target": "Anna Krikun",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🗣 Do you have a phrase or expression you say a lot these days?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "Gauthier Sorais": {
        "target": "Sabrina Barth",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🕰 What’s your favorite moment of the day these days?"
        ]
    },
    "오정원": {
        "target": "김범일",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "Frank": {
        "target": "태림",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🌴 If you could go on vacation right now, where would you go?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "김범일": {
        "target": "Gauthier Sorais",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🕰 What’s your favorite moment of the day these days?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "태림": {
        "target": "Alejandre",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    }
}
user_keys = {
    "Maëlle Garnier": "5227",
    "안지민": "3554",
    "방도윤": "7952",
    "mathias": "7450",
    "Annabel Heberle": "9786",
    "Alexandre Andtbacka(LOOP)": "5479",
    "Valentin Vota": "5312",
    "김채린": "9031",
    "Lei Yuchen": "9361",
    "Anja Zachariasen": "1458",
    "Malina": "8612",
    "Calvin Lieu": "1244",
    "Haidar": "3189",
    "Quentin": "7538",
    "Me Cota": "1922",
    "조현서(LOOP)": "1977",
    "김한슬": "6610",
    "음진희": "1695",
    "leon vicari": "8778",
    "Antonio Carusillo": "9163",
    "박수하(LOOP)": "6047",
    "김다경": "4793",
    "Annate": "3956",
    "Ba Lam Nguyen": "4406",
    "이지원": "4765",
    "Hannes": "8055",
    "Gabriel": "6466",
    "김연우": "2650",
    "Iris Qoshi": "6275",
    "Jessica Schenkelberg": "1586",
    "이민규": "6569",
    "Carolin Barth": "3243",
    "틍쿠": "8008",
    "윤제": "4662",
    "윤민식": "1817",
    "박소현": "9577",
    "Laura Hauser": "2842",
    "Kellian": "9617",
    "Vittorio Ventanni": "6873",
    "Lucas": "6391",
    "Octave Guerini": "9619",
    "정수아": "3735",
    "Louis Moretti": "7023",
    "신현서": "5641",
    "Mounia Nasser": "3129",
    "Robin Ruault": "7605",
    "Linus Knohl": "9927",
    "Edanur Atak": "1619",
    "조은진": "4691",
    "박소윤": "2135",
    "Sabrina Barth": "8315",
    "Alejandre": "2409",
    "Anna Krikun": "5976",
    "Nadyrkhano(알리나)": "2447",
    "Gauthier Sorais": "2789",
    "오정원": "4679",
    "Frank": "7260",
    "김범일": "3730",
    "태림": "8583"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_manitto", methods=["POST"])
def get_manitto():
    data = request.get_json()
    name = data.get("name", "").strip()
    code = data.get("code", "").strip()

    # Fuzzy match to closest registered name
    closest = difflib.get_close_matches(name, user_keys.keys(), n=1, cutoff=0.6)
    if not closest:
        return jsonify({"error": "Name not recognized."}), 400

    real_name = closest[0]

    # Check code
    if code != user_keys.get(real_name):
        return jsonify({"error": "Wrong code. Access denied."}), 403

    entry = manitto_mapping[real_name]
    return jsonify({
        "manitto": entry["target"],
        "missions": entry["missions"]
    })

if __name__ == "__main__":
    app.run()

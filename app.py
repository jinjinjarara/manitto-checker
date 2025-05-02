
from flask import Flask, request, jsonify, render_template
import difflib

app = Flask(__name__)

manitto_mapping = {
    "Maëlle Garnier": {
        "target": "Lei Yuchen",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🌴 If you could go on vacation right now, where would you go?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "안지민": {
        "target": "Annabel Heberle",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "방도윤": {
        "target": "Valentin Vota",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "mathias": {
        "target": "Maëlle Garnier",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🕰 What’s your favorite moment of the day these days?"
        ]
    },
    "Annabel Heberle": {
        "target": "mathias",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🕰 What’s your favorite moment of the day these days?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "Alexandre Andtbacka(LOOP)": {
        "target": "안지민",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "Valentin Vota": {
        "target": "Alexandre Andtbacka(LOOP)",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "김채린": {
        "target": "방도윤",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "🎧 What song or artist have you been listening to lately?"
        ]
    },
    "Lei Yuchen": {
        "target": "김채린",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🌴 If you could go on vacation right now, where would you go?",
            "🎧 What song or artist have you been listening to lately?"
        ]
    },
    "Anja Zachariasen": {
        "target": "김한슬",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "Malina": {
        "target": "Calvin Lieu",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "Calvin Lieu": {
        "target": "Malina",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🗣 Do you have a phrase or expression you say a lot these days?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "Haidar": {
        "target": "Me Cota",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🌴 If you could go on vacation right now, where would you go?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "Quentin": {
        "target": "조현서(LOOP)",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "Me Cota": {
        "target": "Haidar",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🎧 What song or artist have you been listening to lately?"
        ]
    },
    "조현서(LOOP)": {
        "target": "Anja Zachariasen",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🌴 If you could go on vacation right now, where would you go?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "김한슬": {
        "target": "Quentin",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "음진희": {
        "target": "Ba Lam Nguyen",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "leon vicari": {
        "target": "김다경",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "Antonio Carusillo": {
        "target": "이지원",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "박수하(LOOP)": {
        "target": "Annate",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "김다경": {
        "target": "Antonio Carusillo",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🕰 What’s your favorite moment of the day these days?"
        ]
    },
    "Annate": {
        "target": "박수하(LOOP)",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "Ba Lam Nguyen": {
        "target": "음진희",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "이지원": {
        "target": "leon vicari",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "Hannes": {
        "target": "윤제",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "Gabriel": {
        "target": "Jessica Schenkelberg",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "김연우": {
        "target": "Carolin Barth",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "Iris Qoshi": {
        "target": "Hannes",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🗣 Do you have a phrase or expression you say a lot these days?",
            "🎧 What song or artist have you been listening to lately?"
        ]
    },
    "Jessica Schenkelberg": {
        "target": "이민규",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "이민규": {
        "target": "틍쿠",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "Carolin Barth": {
        "target": "Iris Qoshi",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "틍쿠": {
        "target": "김연우",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "윤제": {
        "target": "Gabriel",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "윤민식": {
        "target": "Laura Hauser",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🕰 What’s your favorite moment of the day these days?",
            "🎧 What song or artist have you been listening to lately?"
        ]
    },
    "박소현": {
        "target": "Kellian",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "Laura Hauser": {
        "target": "박소현",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "🕰 What’s your favorite moment of the day these days?"
        ]
    },
    "Kellian": {
        "target": "정수아",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "Vittorio Ventanni": {
        "target": "Lucas",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🕰 What’s your favorite moment of the day these days?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "Lucas": {
        "target": "Octave Guerini",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "Octave Guerini": {
        "target": "Vittorio Ventanni",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎧 What song or artist have you been listening to lately?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "정수아": {
        "target": "윤민식",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🕰 What’s your favorite moment of the day these days?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "Louis Moretti": {
        "target": "Edanur Atak",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🕰 What’s your favorite moment of the day these days?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "신현서": {
        "target": "Louis Moretti",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🗣 Do you have a phrase or expression you say a lot these days?"
        ]
    },
    "Mounia Nasser": {
        "target": "조은진",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "Robin Ruault": {
        "target": "박소윤",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🕰 What’s your favorite moment of the day these days?"
        ]
    },
    "Linus Knohl": {
        "target": "Robin Ruault",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "Edanur Atak": {
        "target": "신현서",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🌴 If you could go on vacation right now, where would you go?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "조은진": {
        "target": "Linus Knohl",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🌴 If you could go on vacation right now, where would you go?",
            "🧡 What emoji do you use the most these days?"
        ]
    },
    "박소윤": {
        "target": "Mounia Nasser",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "Sabrina Barth": {
        "target": "Anna Krikun",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "Alejandre": {
        "target": "Frank",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🎒 What’s something you always carry in your bag or pocket?"
        ]
    },
    "Anna Krikun": {
        "target": "태림",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "Nadyrkhano(알리나)": {
        "target": "Sabrina Barth",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "⏰ Do you wake up without an alarm or keep snoozing it?",
            "🎧 What song or artist have you been listening to lately?"
        ]
    },
    "Gauthier Sorais": {
        "target": "Alejandre",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "오정원": {
        "target": "Gauthier Sorais",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🎒 What’s something you always carry in your bag or pocket?",
            "🌴 If you could go on vacation right now, where would you go?"
        ]
    },
    "Frank": {
        "target": "김범일",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "🍜 If you could only eat one food forever, what would it be?"
        ]
    },
    "김범일": {
        "target": "Nadyrkhano(알리나)",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🧡 What emoji do you use the most these days?",
            "⏰ Do you wake up without an alarm or keep snoozing it?"
        ]
    },
    "태림": {
        "target": "오정원",
        "missions": [
            "📸 Take a photo together (just the two of you)",
            "🍜 If you could only eat one food forever, what would it be?",
            "🕰 What’s your favorite moment of the day these days?"
        ]
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_manitto", methods=["POST"])
def get_manitto():
    data = request.get_json()
    name = data.get("name", "").strip()

    # Use fuzzy matching to find closest name
    closest = difflib.get_close_matches(name, manitto_mapping.keys(), n=1, cutoff=0.6)

    if not closest:
        return jsonify({"error": "Name not recognized. Please try again or check spelling."}), 400

    real_name = closest[0]
    entry = manitto_mapping[real_name]

    return jsonify({
        "manitto": entry["target"],
        "missions": entry["missions"]
    })

if __name__ == "__main__":
    app.run()

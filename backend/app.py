from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

REVERSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

@app.route("/text-to-morse", methods=["POST"])
def text_to_morse():
    data = request.json.get("text", "").upper()
    morse = " ".join([MORSE_CODE_DICT.get(ch, "") for ch in data if ch != " "])
    return jsonify({"result": morse})

@app.route("/morse-to-text", methods=["POST"])
def morse_to_text():
    data = request.json.get("morse", "")
    text = "".join([REVERSE_DICT.get(code, "") for code in data.split()])
    return jsonify({"result": text})

if __name__ == "__main__":
    app.run(port=5000, debug=True)

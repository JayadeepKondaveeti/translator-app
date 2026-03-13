from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():

    data = request.get_json()

    text = data["text"]
    language = data["language"]

    url = "https://api.mymemory.translated.net/get"

    params = {
        "q": text,
        "langpair": f"en|{language}"
    }

    response = requests.get(url, params=params)

    result = response.json()

    translated = result["responseData"]["translatedText"]

    return jsonify({"translated": translated})


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)

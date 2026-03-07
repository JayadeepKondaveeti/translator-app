from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    translated = ""

    if request.method == "POST":

        text = request.form["text"]
        target_language = request.form["language"]

        url = "https://api.mymemory.translated.net/get"

        params = {
            "q": text,
            "langpair": f"en|{target_language}"
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()
            translated = data["responseData"]["translatedText"]
        except:
            translated = "Translation failed. Please try again."

    return render_template("index.html", translated=translated)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

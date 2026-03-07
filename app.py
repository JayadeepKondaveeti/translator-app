from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    translated = ""

    if request.method == "POST":

        text = request.form["text"]
        target = request.form["language"]

        url = "https://api.mymemory.translated.net/get"

        params = {
            "q": text,
            "langpair": "en|" + target
        }

        response = requests.get(url, params=params)

        translated = response.json()['responseData']['translatedText']

    return render_template("index.html", translated=translated)

if __name__ == "__main__":
    app.run()
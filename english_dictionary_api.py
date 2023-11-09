from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("dictionary.csv")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def meaning(word):
    definition = df.loc[df["word"] == word]['definition'].squeeze()
    definition = definition.strip().split("\n")
    result = {"word": word, "definition": [meaning for meaning in definition]}
    return result


if __name__ == "__main__":
    app.run(debug=True)

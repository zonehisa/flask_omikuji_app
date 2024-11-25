import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/omikuji")
def omikuji():
    result = random.choice(["大吉！", "中吉", "凶..."])
    return render_template("omikuji.html", result=result)


if __name__ == "__main__":
    app.run(port=8000, debug=True)

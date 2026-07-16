from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sherlar")
def sherlar():
    return render_template("sherlar.html")

@app.route("/hikoyalar")
def hikoyalar():
    return render_template("hikoyalar.html")

@app.route("/esseylar")
def esseylar():
    return render_template("esseylar.html")

@app.route("/muallif")
def muallif():
    return render_template("muallif.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)



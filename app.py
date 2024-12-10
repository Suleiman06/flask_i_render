from Flask import Flask

app = Flask(__name__)

@app.route("/", methodss=["GET"])
def helllo():
    return "<h1>Arpan's Flask App</h1>"

if __name__ == "__main__":
    app.run
    
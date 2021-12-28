from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
      return render_template("index.html")

if __name__ == "__main__":
      app.run(port=3000, host="192.168.1.43")

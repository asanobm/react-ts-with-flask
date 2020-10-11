from flask import Flask, render_template, send_from_directory
import os
from api.controllers import get_hello

app = Flask(__name__, static_folder="build/static", template_folder="build")

app.register_blueprint(get_hello.app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/manifest.json")
def manifest():
    return send_from_directory('./build', 'manifest.json')


@app.route("/logo192.png")
def logo192():
    return send_from_directory('./build', 'logo192.png')


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 3000)), debug=True)

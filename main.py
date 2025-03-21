from flask import Flask, render_template, jsonify
from data_manager import load_data, update_data

app = Flask(__name__)

@app.route("/")
def index():
    global initial_render
    if not initial_render:
        initial_render = True
        return render_template("index.html")
    return jsonify(load_data())

@app.route("/update")
def update():
    data = update_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
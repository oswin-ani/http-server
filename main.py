from flask import Flask, render_template, jsonify
from data_manager import load_data, update_data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Рендерим шаблон без данных

@app.route("/data")
def get_data():
    return jsonify(load_data())  # Отдаем данные отдельным эндпоинтом

@app.route("/update", methods=['POST'])
def update():
    data = update_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

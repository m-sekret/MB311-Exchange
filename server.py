from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

# Зберігаємо поточні дані
exchange_data = {
        "Gold": 0.0,
        "Platinum": 0.0,
        "Silver": 0.0,
        "ABM": 0.0,
        "BTI": 0.0,
        "KO": 0.0,
        "euro_to_usd": 0.0,
        "pound_to_usd": 0.0,
        "usd_to_jpy": 0.0
}

sensors = [
        "uah_to_usd",
        "usd_to_uah"
]

@app.route('/update', methods=['POST'])
def update_exchange():
    global exchange_data
    data = request.json

    for key in sensors:
        exchange_data[key] = data.get(key, exchange_data[key])

    return jsonify({"status": "success"}), 200

@app.route('/current_exchange', methods=['GET'])
def get_exchange(): return jsonify(exchange_data), 200

@app.route('/')
def index(): return render_template('index.html')

if __name__ == '__main__': app.run(debug=True, host='0.0.0.0')

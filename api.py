from flask import Flask, jsonify
from data_collection import fetch_economic_data
from crisis_detection import detect_crisis

app = Flask(__name__)

@app.route('/api/economic_data', methods=['GET'])
def get_economic_data():
    data = fetch_economic_data()
    return jsonify(data)

@app.route('/api/crisis_detection', methods=['GET'])
def get_crisis_detection():
    predictions = detect_crisis()
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
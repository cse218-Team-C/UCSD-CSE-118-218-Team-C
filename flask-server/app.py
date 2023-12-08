from flask import Flask, jsonify
from moisture_sensor import get_moisture_readings_from_channel

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/moisture', methods=['GET'])
def get_moisture():
    moisture_level = get_moisture_readings_from_channel()
    return jsonify({'moisture_level': moisture_level})

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

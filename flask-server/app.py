from flask import Flask, jsonify
from moisture_sensor import get_moisture_readings_from_channels

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/moisture/<int:channel>', methods=['GET'])
def get_moisture(channel):
    # TODO update to support list of channels later
    moisture_level = get_moisture_readings_from_channels([channel])
    return jsonify({'channel': channel, 'moisture_level': moisture_level})

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

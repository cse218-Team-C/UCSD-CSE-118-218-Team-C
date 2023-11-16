from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/moisture', methods=['GET'])
def get_moisture():
    # TODO: Replace with actual moisture level retrieval code
    moisture_level = 0
    return jsonify({'moisture_level': moisture_level})

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')

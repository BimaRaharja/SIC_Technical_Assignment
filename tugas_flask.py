from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def receive_data():
    if request.method == ('GET','POST'):
        data = request.get_json()
        temperature = data.get('temperature')
        humidity = data.get('humidity')
        
        response = {
            "message": "Data received",
            "temperature": temperature,
            "humidity": humidity
        }
        return jsonify(response)
    else:
        return jsonify({"message": "Send POST requests to this endpoint"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

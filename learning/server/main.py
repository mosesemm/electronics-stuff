from flask import Flask, jsonify, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route('/api/test/<id>', methods=['GET'])
def test(id):

    return jsonify({'id':id})

@app.route('/api/on', methods=['GET'])
def on_():
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.OUT)
    GPIO.output(27,GPIO.HIGH)
    return jsonify({'status':'on'})

@app.route('/api/off', methods=['GET'])
def off_():
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.OUT)
    GPIO.output(27,GPIO.LOW)
    GPIO.cleanup()
    return jsonify({'status':'off'})

@app.route('/api/test', methods=['POST'])
def test2():
    print(request.json)
    return jsonify({'results': 'working'})


if __name__ == "__main__":
    app.run( host="0.0.0.0", port=8080)

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route('/api/test/<id>', methods=['GET'])
def test(id):
    return jsonify({'id':id})


@app.route('/api/test', methods=['POST'])
def test2():
    print(request.json)
    return jsonify({'results': 'working'})


if __name__ == "__main__":
    app.run( host="0.0.0.0", port=8080)

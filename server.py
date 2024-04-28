from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return request.json

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
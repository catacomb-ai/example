import os
from flask import Flask, request, jsonify
from system import *

app = Flask(__name__)
system = System()

@app.route("/predict", methods=['POST'])
def predict():
    input_object = request.get_json()['input']
    return jsonify(output=system.output(input_object))

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int(os.getenv('PORT', 5000)), debug=True)

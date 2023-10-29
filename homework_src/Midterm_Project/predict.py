import pickle

from flask import Flask
from flask import jsonify
from flask import request


def load(filename: str):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


dv = load('dv.bin')
dv_dtc = load('dv_dtc.bin')
dv_rcf = load('dv_rcf.bin')
model_lr = load('model.bin')
model_dtc = load('model_dtc.bin')
model_rcf = load('model_rcf.bin')

app = Flask('midterm-project')


@app.route('/predict/lr', methods=['POST'])
def predict_lr():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model_lr.predict(X)[0]
    is_fraud = round(float(y_pred), 3)

    result = {
        'is_fraud': is_fraud,
        'Transaction is fraud': bool(is_fraud)
    }

    return jsonify(result)


@app.route('/predict/dtc', methods=['POST'])
def predict_dtc():
    client = request.get_json()

    X = dv_dtc.transform([client])
    y_pred = model_dtc.predict(X)[0]
    is_fraud = round(float(y_pred), 3)

    result = {
        'is_fraud': is_fraud,
        'Transaction is fraud': bool(is_fraud)
    }

    return jsonify(result)


@app.route('/predict/rcf', methods=['POST'])
def predict_rcf():
    client = request.get_json()

    X = dv_rcf.transform([client])
    y_pred = model_rcf.predict(X)[0]
    is_fraud = round(float(y_pred), 3)

    result = {
        'is_fraud': is_fraud,
        'Transaction is fraud': bool(is_fraud)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)

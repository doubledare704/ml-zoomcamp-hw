from flask import Flask
from flask import jsonify
from flask import request

from homework_src.HW5.utils import dv, model

app = Flask('credict-card')


@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]
    get_card_probability = round(float(y_pred), 3)
    get_card = y_pred >= 0.5

    result = {
        'get_card_probability': get_card_probability,
        'get_card': bool(get_card)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)

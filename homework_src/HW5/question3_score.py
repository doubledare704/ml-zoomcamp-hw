from homework_src.HW5.utils import model, dv

client = {"job": "retired", "duration": 445, "poutcome": "success"}

X = dv.transform([client])
y_pred = model.predict_proba(X)[0, 1]

print(round(y_pred, 3))

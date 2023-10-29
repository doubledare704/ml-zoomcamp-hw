import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def saver(data, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)


def main():
    def train_lr(fraud_train, fraud_y_train, c=1.0):
        dicts = fraud_train[columns].to_dict(orient='records')

        d_vectorized = DictVectorizer()
        fraud_x_train = d_vectorized.fit_transform(dicts)

        cur_model = LogisticRegression(solver='liblinear', C=c, max_iter=1000, random_state=1)
        cur_model.fit(fraud_x_train, fraud_y_train)

        return d_vectorized, cur_model

    def train_dtc(fraud_train, fraud_y_train):
        dicts = fraud_train[columns].to_dict(orient='records')

        d_vectorized = DictVectorizer()
        fraud_x_train = d_vectorized.fit_transform(dicts)

        cur_model = DecisionTreeClassifier(max_depth=10, random_state=1)
        cur_model.fit(fraud_x_train, fraud_y_train)

        return d_vectorized, cur_model

    def train_rcf(fraud_train, fraud_y_train):
        dicts = fraud_train[columns].to_dict(orient='records')

        d_vectorized = DictVectorizer()
        fraud_x_train = d_vectorized.fit_transform(dicts)

        cur_model = RandomForestClassifier(max_depth=10, n_estimators=10, random_state=1)
        cur_model.fit(fraud_x_train, fraud_y_train)

        return d_vectorized, cur_model

    credit_fraud_df = pd.read_csv("./credit_fraud_detection/creditcard_2023.csv")
    credit_fraud_df.drop(columns=["id"], inplace=True)

    df_full_train, df_test = train_test_split(credit_fraud_df, test_size=0.2, random_state=1)

    columns = list(credit_fraud_df.columns)
    columns.remove('Class')

    print("Starting training...")

    y_train = df_full_train.Class.values
    del df_full_train['Class']
    del df_test['Class']

    dv, model = train_lr(df_full_train, y_train, c=0.1)

    print("Saving model to disk...")

    saver(dv, "dv.bin")
    saver(model, "model.bin")

    print("Model and vectorizer are saved to disk.")

    # Create Decision Tree classifer object
    print("Training model...")
    # Train Decision Tree Classifer
    dv_dtc, dtc = train_dtc(df_full_train, y_train)
    saver(dtc, "model_dtc.bin")
    saver(dv_dtc, "dv_dtc.bin")
    print("Saving model to disk...")

    print("Training model...")
    dv_rcf, rcf = train_rcf(df_full_train, y_train)
    saver(rcf, "model_rcf.bin")
    saver(dv_rcf, "dv_rcf.bin")
    print("Saving model to disk...")


main()

from prefect import flow, task

import mlflow
import mlflow.sklearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


@task
def load_data():

    data = load_iris()

    X = data.data
    y = data.target

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


@task
def train_model(X_train, X_test, y_train, y_test):

    mlflow.set_experiment("Prefect_SVM_Experiment")

    c_values = [0.1, 1, 10]

    for c in c_values:

        with mlflow.start_run(run_name=f"SVM_C_{c}"):

            model = SVC(C=c)

            model.fit(X_train, y_train)

            predictions = model.predict(X_test)

            accuracy = accuracy_score(y_test, predictions)

            mlflow.log_param("C", c)

            mlflow.log_metric("accuracy", accuracy)

            mlflow.sklearn.log_model(model, "svm_model")

            print(f"C={c} Accuracy={accuracy}")


@flow
def svm_training_workflow():

    X_train, X_test, y_train, y_test = load_data()

    train_model(
        X_train,
        X_test,
        y_train,
        y_test
    )


if __name__ == "__main__":

    svm_training_workflow()
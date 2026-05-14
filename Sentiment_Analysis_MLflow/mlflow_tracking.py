import os

os.environ["MLFLOW_TRACKING_URI"] = "file:./mlruns"

import mlflow
import mlflow.sklearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()

X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create experiment
mlflow.set_experiment("SVM_Experiment")

# Hyperparameter runs
c_values = [0.1, 1, 10]

for c in c_values:

    with mlflow.start_run(run_name=f"SVM_C_{c}"):

        # Model
        model = SVC(C=c)

        # Train
        model.fit(X_train, y_train)

        # Predict
        predictions = model.predict(X_test)

        # Accuracy
        accuracy = accuracy_score(y_test, predictions)

        # Log parameters
        mlflow.log_param("C", c)

        # Log metrics
        mlflow.log_metric("accuracy", accuracy)

        # Log model
        mlflow.sklearn.log_model(model, "svm_model")

        print(f"C={c} Accuracy={accuracy}")
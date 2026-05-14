# Sentiment Analysis with MLflow and Prefect

## Project Overview

This project demonstrates the integration of **MLflow** for experiment tracking and model management along with **Prefect** for workflow orchestration and scheduling.

The project trains an SVM model using Scikit-learn and tracks:

* Parameters
* Metrics
* Model artifacts
* Hyperparameter experiments
* Model registry and tagging

Additionally, a Prefect workflow is implemented to automate the machine learning pipeline execution.

---

# Technologies Used

* Python
* Scikit-learn
* MLflow
* Prefect
* Pandas
* NumPy
* VS Code

---

# Features Implemented

## MLflow Features

* Experiment Tracking
* Parameter Logging
* Metric Logging
* Artifact Logging
* Hyperparameter Tuning
* Compare Runs Visualization
* Model Registry
* Model Tagging

## Prefect Features

* Workflow Automation
* Task Orchestration
* Flow Execution Monitoring
* Prefect Dashboard Visualization

---

# Project Structure

```text
Sentiment_Analysis_MLflow/
│
├── screenshots/
├── mlflow_tracking.py
├── prefect_workflow.py
├── requirements.txt
├── README.md
├── mlruns/
└── venv/
```

---

# MLflow Experiment Tracking

The project uses MLflow tracking APIs to:

* Log Parameters
* Log Metrics
* Log Model Artifacts
* Compare Multiple Runs
* Register Models
* Add Model Tags

Hyperparameter tuning was performed using different SVM `C` values:

* C = 0.1
* C = 1
* C = 10

---

# Model Performance

| Model Run | Accuracy |
| --------- | -------- |
| SVM_C_0.1 | 0.9667   |
| SVM_C_1   | 1.0000   |
| SVM_C_10  | 1.0000   |

---

# Prefect Workflow

A Prefect workflow was created to automate:

1. Data Loading
2. Model Training
3. Experiment Logging
4. Workflow Monitoring

The workflow was executed successfully using the Prefect dashboard.

---

# Screenshots

## MLflow Experiment Runs

![Experiment Runs](screenshots/1_experiment_runs.png)

## Compare Runs Visualization

![Compare Runs](screenshots/2_compare_runs.png)

## Individual Run Details

![Run Details](screenshots/3_run_details.png)

## Model Registry

![Model Registry](screenshots/4_model_registry.png)

## Model Tags

![Model Tags](screenshots/5_model_tags.png)

## Prefect Dashboard

![Prefect Dashboard](screenshots/6_prefect_dashboard.png)

## Prefect Flow Run

![Prefect Flow Run](screenshots/7_prefect_flow_run.png)

## Prefect Task Execution

![Prefect Tasks](screenshots/8_prefect_tasks.png)

---

# How to Run the Project

## Step 1: Create Virtual Environment

```bash
python -m venv venv
```

## Step 2: Activate Virtual Environment

```bash
venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Run MLflow Tracking

```bash
python mlflow_tracking.py
```

## Step 5: Start MLflow UI

```bash
python -m mlflow ui --backend-store-uri ./mlruns
```

Open:

```text
http://127.0.0.1:5000
```

## Step 6: Run Prefect Workflow

```bash
python prefect_workflow.py
```

## Step 7: Start Prefect Dashboard

```bash
prefect server start
```

Open:

```text
http://127.0.0.1:4200
```

---

# Conclusion

This project demonstrates practical MLOps concepts including:

* Experiment tracking
* Model management
* Workflow orchestration
* Hyperparameter tuning
* Dashboard monitoring

using MLflow and Prefect.

# 🚢 Titanic Survival Prediction — MLOps Project

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%20Pipeline-success)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange)

## 📌 Project Overview

The **Titanic Survival Prediction MLOps Project** demonstrates an end-to-end machine learning workflow, from model training and saving to API deployment and continuous integration.

The model predicts whether a passenger survived the Titanic disaster based on passenger-related input features.

This project integrates Machine Learning, FastAPI, Docker, and GitHub Actions to build and validate a machine learning application.

## 🎯 Objectives

* Train and test a machine learning model using the Titanic dataset.
* Save the trained model as `model.joblib`.
* Build a REST API using FastAPI for predictions.
* Containerize the application using Docker.
* Write automated API tests using pytest.
* Configure a GitHub Actions CI pipeline to automatically run tests and build the Docker image.

## 🛠️ Technologies Used

* **Python 3.11** — Programming language
* **Pandas & NumPy** — Data processing
* **Scikit-learn** — Machine learning
* **Joblib** — Model serialization
* **FastAPI** — REST API development
* **Uvicorn** — ASGI server
* **Pytest** — Automated testing
* **Docker** — Application containerization
* **GitHub Actions** — Continuous Integration
* **Google Colab / Jupyter Notebook** — Model training and experimentation

## 📊 Dataset

**Dataset:** Titanic — Machine Learning from Disaster
**Source:** Kaggle

Dataset page: https://www.kaggle.com/competitions/titanic

The dataset contains passenger information such as age, sex, passenger class, fare, and survival status.

**Target variable:** `Survived`

* `0` — Did not survive
* `1` — Survived

> Note: The model's exact input features depend on the preprocessing and training pipeline used when creating `model.joblib`.

## 🏗️ Project Architecture

```text
Titanic_MLOps/
│
├── app/
│   ├── main.py
│   └── tests/
│       └── test_api.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── model.joblib
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## ⚙️ How It Works

1. **Data Preparation:** The Titanic dataset is prepared for machine learning.
2. **Model Training:** A machine learning model is trained and evaluated in Google Colab or Jupyter Notebook.
3. **Model Serialization:** The trained model is saved as `model.joblib`.
4. **API Development:** FastAPI loads the saved model and exposes an endpoint for predictions.
5. **Testing:** Pytest checks the API's functionality.
6. **Containerization:** Docker packages the application and its dependencies.
7. **Continuous Integration:** GitHub Actions installs dependencies, runs tests, and builds the Docker image whenever changes are pushed to GitHub.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shivam94566/CA_AIOPS.git
cd CA_AIOPS
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the FastAPI Application

```bash
python -m uvicorn app.main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## 🧪 Run Automated Tests

Run the following command from the project root:

```bash
python -m pytest app/tests -v
```

The tests validate the API functionality and help detect regressions.

## 🐳 Run with Docker

### 1. Build the Docker Image

```bash
docker build -t titanic-mlops .
```

### 2. Start the Container

```bash
docker run -d --name titanic-api -p 8000:8000 titanic-mlops
```

### 3. Access the API

Open:

http://127.0.0.1:8000/docs

### 4. Stop the Container

```bash
docker stop titanic-api
```

To remove the container:

```bash
docker rm titanic-api
```

> If a container named `titanic-api` already exists, remove it before creating another container with the same name.

## 🔄 GitHub Actions CI Pipeline

The project includes a GitHub Actions workflow at:

`.github/workflows/ci.yml`

The pipeline automatically performs these steps:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs the required dependencies.
4. Runs automated API tests.
5. Builds the Docker image.

The workflow runs on pushes and pull requests targeting the `main` branch.

**Pipeline status:** The CI workflow has been executed successfully, with the API tests and Docker image build passing.

View the workflow runs:

https://github.com/Shivam94566/CA_AIOPS/actions

## 📈 Key Features

* End-to-end machine learning workflow
* Saved and reusable ML model
* REST API for real-time predictions
* Interactive Swagger API documentation
* Automated API testing
* Docker-based deployment
* GitHub Actions continuous integration
* Automated Docker image build

## 🔮 Future Improvements

* Add model performance metrics such as accuracy, precision, recall, and F1-score.
* Add input validation and more comprehensive API tests.
* Deploy the API to a cloud platform.
* Add model versioning and experiment tracking.
* Introduce continuous deployment (CD).
* Add monitoring for prediction requests and model performance.

## 👨‍💻 Author

**Shivam Bhardwaj**
B.Tech Computer Science Engineering Student

GitHub: https://github.com/Shivam94566

## 📄 License

This project is intended for educational and academic purposes.

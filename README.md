# Salary Predictor ML API

This project is a simple Machine Learning (ML) API built with **FastAPI**. The API predicts the annual salary of an employee in USD based on their years of experience using a linear regression model.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Model](#model)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dockerization](#dockerization)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Overview
The project implements a simple linear regression model trained on a dataset containing years of experience and corresponding salaries. The model is then served via a RESTful API using FastAPI, allowing users to predict salaries based on input years of experience.

## Dataset
The dataset used for training the model is `Salary_dataset.csv`, which contains the following columns:
- **YearsExperience**: Number of years of experience (float)
- **Salary**: Annual salary in USD (float)

### Example:
| YearsExperience | Salary  |
|-----------------|---------|
| 1.1             | 39343.0 |
| 2.0             | 46205.0 |
| 3.2             | 60150.0 |

## Model
The model is a simple linear regression model trained using the `scikit-learn` library. It takes the `YearsExperience` as input and predicts the `Salary`.

## Project Structure
├── main.py # Code to clean data, train model, and export it as joblib ├── app.py # FastAPI application for serving the model ├── User.py # Pydantic model for input validation ├── requirements.txt # Python dependencies ├── linear_regression_model.joblib # Saved model in joblib format ├── Salary_dataset.csv # Dataset used for training ├── Dockerfile # Docker configuration file └── README.md # Project documentation


## Installation

### Prerequisites
- Python 3.8 or higher
- Docker (if you want to run the application in a container)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/kamalalalul/salary_predictor.git
   cd salary-predictor-ml-api
2. **Create a virtual environment and activate it:**

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the dependencies:**

pip install -r requirements.txt

4. **Run the FastAPI application:**
uvicorn app:app --reload

5. **Access the API:** 
Open your browser and go to http://127.0.0.1:8000.

## Dockerization
To run the application using Docker:

1. Build the Docker image:

docker build -t salary-predictor.

2. Run the Docker container:

docker run -d -p 8000:8000 salary-predictor

3. Access the API: Open your browser and go to http://localhost:8000.


## API Endpoints
1. Root Endpoint
URL: /
Method: GET
Description: Returns a welcome message.
Response:
json
Copy code
{
  "message": "Salary Predictor ML API. This model predicts the annual salary of an employee in USD based on their years of experience. It is a simple linear regression model created using a 1-feature dataset."
}
2. Predict Salary
URL: /salary/predict
Method: POST
Description: Predicts the salary based on years of experience.
Request Body:

{
  "years": 5.0
}

Response:

{
  "prediction": 76543.21
}

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
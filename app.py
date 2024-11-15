import uvicorn
from fastapi import FastAPI
import joblib
from User import Employee

app = FastAPI()
joblib_in = open("linear_regression_model.joblib","rb")
model=joblib.load(joblib_in)


@app.get('/')
def index():
    return {'message': 'Salary Predictor ML API. This model predicts the annual salary of an employee in USD based on their years of experience.It is a simple linear regression model created using 1 feature dataset.'}

@app.post('/salary/predict')
def predict_salary(data:Employee):
    data = data.dict()
    years=data['years']

    prediction = model.predict([[years]])
    
    return {
        'prediction': prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class LoanRequest(BaseModel):
    name: str
    monthly_income: float
    monthly_expenses: float
    loan_amount: float
    interest_rate: float


@app.post("/financial-analysis")
def financial_analysis(data: LoanRequest):

    surplus = data.monthly_income - data.monthly_expenses

    return {
        "borrower": data.name,
        "monthly_surplus": surplus,
        "loan_amount": data.loan_amount,
        "interest_rate": data.interest_rate,
        "status": "Financial analysis completed successfully"
    }


@app.get("/")
def home():
    return {"message": "FinRelief AI Backend Running"}

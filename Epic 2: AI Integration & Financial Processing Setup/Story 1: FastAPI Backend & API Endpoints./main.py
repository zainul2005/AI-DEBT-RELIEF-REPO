from fastapi import FastAPI

app = FastAPI(title="FinRelief AI API")

@app.get("/")
def home():
    return {"message": "Welcome to FinRelief AI Backend"}

@app.get("/health")
def health():
    return {"status": "Backend is running"}

@app.post("/login")
def login():
    return {"message": "Login endpoint"}

@app.get("/loans")
def get_loans():
    return {"message": "Loan API"}

@app.post("/settlement-prediction")
def settlement_prediction():
    return {"message": "Settlement Prediction API"}

@app.post("/ai-negotiation")
def ai_negotiation():
    return {"message": "AI Negotiation API"}

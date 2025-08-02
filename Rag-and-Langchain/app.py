# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from evaluate_scorecard import evaluate  # Only import what you need

app = FastAPI()

class ScoreRequest(BaseModel):
    company_name: str
    top_k: Optional[int] = 3  # Not currently used, but could be passed later

@app.post("/score")
def score_pitchdeck(req: ScoreRequest):
    try:
        result = evaluate(req.company_name)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
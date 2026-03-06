from fastapi import FastAPI
from schemas import Agent4Request
from bias_engine import BiasEngine

app = FastAPI()

bias_engine = BiasEngine()


@app.post("/audit_candidate")

def audit_candidate(data: Agent4Request):

    result = bias_engine.compute_fair_score(
        data.jd,
        data.profile,
        data.assessment
    )

    return {
        "candidate_id": data.profile.candidate_id,
        "bias_checked": True,
        "fair_score": result["fair_score"],
        "breakdown": result
    }
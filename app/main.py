from fastapi import FastAPI, HTTPException, status

from app.schemas import GuardrailResponse, UserQuery
from app.services import GuardrailService

app = FastAPI(
    title="AI Guardrail Backend Service",
    description="Week 1 Capstone Project validating incoming LLM Prompts.",
    version="1.0.0",
)


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """Service health state checkpoint endpoint."""
    return {"status": "healthy", "service": "ai-guardrail-api"}


@app.post("/validate", response_model=GuardrailResponse, status_code=status.HTTP_200_OK)
def validate_prompt(payload: UserQuery):
    """
    Ingests prompts, runs security rules engines, and returns clear validation flags.
    """
    try:
        response = GuardrailService.analyze_prompt(payload)
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal processing failure: {str(e)}",
        )

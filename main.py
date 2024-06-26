"""
Application for calculating payment schedules and profitability

author: Konstantin Koshelev

tasks history: test_task
"""

from fastapi import FastAPI
from fastapi import Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.calculation import calculate_deposit_profitability_scheduler
from app.schema import Deposit
from typing import Dict

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse({'error': str(exc)}, status_code=400)


@app.get("/health")
async def healthcheck():
    """
    endpoint for health check
    :return:
    """
    return Response(content=str({"HealthCheck": "OK"}))


@app.post('/deposits/v1/profitability_scheduler')
async def post_profitability_scheduler(deposit: Deposit) -> Dict[str, float]:
    schedule = calculate_deposit_profitability_scheduler(deposit)
    return schedule


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

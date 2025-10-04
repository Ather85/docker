# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from deployment-ready-ga2-013181!"}

@app.post("/analytics")
async def analytics(data: dict):
    # Example dummy response
    return {"status": "received", "payload": data}

from fastapi import FastAPI

app = FastAPI(
    title="Sentinel Factory Platform",
    description="A cyber-physical systems monitoring and audit platform",
    version="0.1.0"
)

@app.get("/")
def health_check():
    return {"status": "ok", "system": "sentinel"}

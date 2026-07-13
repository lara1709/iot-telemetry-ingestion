from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return{"message": "IoT Telemetry API is running"}
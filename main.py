from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def boot():
    return {"Hello"}
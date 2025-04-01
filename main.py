from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Mera Bot Chal Gaya!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"Hello": name}

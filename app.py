from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def reservations():
    return "hola mundo"
from fastapi import FastAPI

app = FastAPI()

users_db = ["Alice", "Bob", "Charlie"]

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/users")
def get_users():
    return {"users": users_db}
from fastapi import FastAPI

app = FastAPI()

# We create a route (ex: http://localhost:8030/score)
@app.get("/score")
def get_score():
    # We will put our algo logic later
    # For now we just send a message to our front
    return {"status": "success", "message": "Semeos backend answers perfectly !"}
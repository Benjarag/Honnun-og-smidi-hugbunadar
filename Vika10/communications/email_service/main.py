from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class SendEmailRequest(BaseModel):
    email: str
    message: str


@app.post("/emails/")
async def create_item(email: SendEmailRequest):
    print(f"{email.email} - {email.message}")
    return email.email


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from src.agent import process_message


app = FastAPI(
    title="E-commerce AI Support Agent",
    description="API para atendimento inteligente de e-commerce.",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


# Arquivos estáticos
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# Página principal
@app.get("/")
def root():
    return FileResponse("static/index.html")


# Endpoint de chat
@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    response = process_message(request.message)

    return {
        "response": response
    }
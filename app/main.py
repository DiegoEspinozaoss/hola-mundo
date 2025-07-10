from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.crawler import buscar_noticia_google

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <h1 style='text-align: center;'>Hola Mundo</h1>
    <p style='text-align: center;'>Ve a <code>/noticia</code> para buscar una noticia</p>
    """

@app.get("/noticia")
def get_noticia():
    resultado = buscar_noticia_google("guerra Israel e Irán")
    return resultado

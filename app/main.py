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
@app.get("/noticia", response_class=HTMLResponse)
def get_noticia_html():
    resultado = buscar_noticia_google("guerra Israel e Irán")
    
    if "error" in resultado:
        return f"<h2>Error: {resultado['error']}</h2>"

    titulo = resultado["titulo"]
    url = resultado["url"]
    
    return f"""
    <h1>Resultado de la búsqueda</h1>
    <p><strong>Título:</strong> {titulo}</p>
    <p><a href="{url}" target="_blank">Ver noticia</a></p>
    """


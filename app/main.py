from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from app.crawler import buscar_noticia_google

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
    <head>
        <meta charset="utf-8">
        <title>Hola Mundo</title>
    </head>
    <body>
        <h1 style='text-align: center;'>Hola Mundo</h1>
        <div style='text-align: center;'>
            <button onclick="buscarNoticia()">Buscar Noticia</button>
        </div>

        <script>
        async function buscarNoticia() {
            try {
                const response = await fetch('/noticia');
                const data = await response.json();
                if (data.url) {
                    window.open(data.url, '_blank');
                } else {
                    alert("No se encontró la noticia");
                }
            } catch (error) {
                alert("Error al buscar la noticia");
            }
        }
        </script>
    </body>
    </html>
    """

@app.get("/noticia")
def get_noticia():
    resultado = buscar_noticia_google("guerra Israel e Irán")
    return JSONResponse(content=resultado)

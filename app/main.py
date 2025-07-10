from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head><title>Hola Mundo</title></head>
        <body>
            <h1 style='text-align: center; font-family: sans-serif;'>Hola Mundo</h1>
        </body>
    </html>
    """


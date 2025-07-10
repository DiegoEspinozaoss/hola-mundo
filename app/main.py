from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from app.crawler import buscar_noticia_google
import requests
import os

app = FastAPI()

# Página principal con botón
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
            <button onclick="buscar()">Buscar noticia y resumir</button>
        </div>
        <pre id="resultado" style="text-align:center;"></pre>
        <script>
            async function buscar() {
                const response = await fetch('/resumen');
                const data = await response.json();
                document.getElementById("resultado").textContent = JSON.stringify(data, null, 2);
            }
        </script>
    </body>
    </html>
    """

# Endpoint que llama al crawler y luego a GPT-2
@app.get("/resumen")
def resumen_noticia():
    resultado = buscar_noticia_google("guerra Israel e Irán")

    if "error" in resultado:
        return JSONResponse(content={"error": resultado["error"]})

    titulo = resultado["titulo"]

    # Enviar a GPT-2 usando Hugging Face Inference API
    HF_API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")  # Debes configurarlo en Render
    API_URL = "https://api-inference.huggingface.co/models/gpt2"

    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {
        "inputs": f"Resume brevemente: {titulo}"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        gpt_output = response.json()

        texto_generado = gpt_output[0]["generated_text"]
        return {
            "titulo": titulo,
            "resumen": texto_generado
        }

    except Exception as e:
        return {"error": str(e)}

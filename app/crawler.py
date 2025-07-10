import os
import requests

def buscar_noticia_google(query: str):
    api_key = os.getenv("SERPAPI_API_KEY")
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "hl": "es",
        "gl": "cl",
        "api_key": api_key,
    }
    response = requests.get(url, params=params)
    data = response.json()

    try:
        resultado = data["organic_results"][0]
        titulo = resultado.get("title")
        link = resultado.get("link")
        return {"titulo": titulo, "url": link}
    except:
        return {"error": "No se encontró resultado"}

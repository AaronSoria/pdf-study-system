import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def process_chunk(chunk, model="qwen2.5-coder:7b"):
    prompt = f"""
Reestructura este contenido para estudio:

- resume conceptos clave
- organiza en secciones
- usa lenguaje claro
- no pierdas información importante

Contenido:
{chunk}
"""

    res = requests.post(OLLAMA_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })

    return res.json()["response"]
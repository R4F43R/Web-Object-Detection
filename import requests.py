import requests
import base64

def detect_with_google_vision(image_path, api_key):
    with open(image_path, "rb") as image_file:
        content = base64.b64encode(image_file.read()).decode("utf-8")
    url = f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"
    body = {
        "requests": [{
            "image": {"content": content},
            "features": [{"type": "OBJECT_LOCALIZATION"}]
        }]
    }
    response = requests.post(url, json=body)
    return response.json()

# Uso:
# result = detect_with_google_vision("ruta/a/imagen.jpg", "TU_API_KEY")
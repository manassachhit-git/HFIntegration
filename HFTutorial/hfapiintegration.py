import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {
    "Authorization": "Bearer YOUR_HF_API_KEY"
}

payload = {
    "inputs": "Hugging Face provides APIs to run ML models easily."
}

response = requests.post(API_URL, headers=headers, json=payload)
print(response.json())
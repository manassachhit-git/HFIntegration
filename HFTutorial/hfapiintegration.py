import requests

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"
headers = {
    "Authorization": "Bearer YOUR_HF_API_KEY"
}

payload = {
    "inputs": "Hugging Face provides APIs to run ML models easily."
}

response = requests.post(API_URL, headers=headers, json=payload)
print(response.json())
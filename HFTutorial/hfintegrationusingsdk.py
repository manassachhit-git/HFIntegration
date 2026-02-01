from huggingface_hub import InferenceClient

client = InferenceClient(
    model="facebook/bart-large-cnn",
    token="YOUR_HF_API_KEY"
)

result = client.summarization(
    "The router endpoint is now mandatory for inference."
)

print(result)

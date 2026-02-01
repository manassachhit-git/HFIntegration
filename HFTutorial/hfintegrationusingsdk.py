from huggingface_hub import InferenceClient


# using hugging face client
client = InferenceClient(
    model="facebook/bart-large-cnn",
    token="YOUR_HF_API_KEY"
)

# using client
result = client.summarization(
    "The router endpoint is now mandatory for inference."
)

print(result)

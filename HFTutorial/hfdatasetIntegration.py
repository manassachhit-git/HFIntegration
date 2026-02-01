from datasets import load_dataset
from huggingface_hub import InferenceClient
import os


# using imdb dataset from huggingface to select one dataset consisting review.
dataset = load_dataset("imdb", split="test")
print("-------------------------------------------------------------------------------")
print("Data:",dataset[0])

client = InferenceClient(
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    token=os.getenv("HF_TOKEN")
)

# Take one sample from dataset
text = dataset[0]["text"]

# binary classifier that returns scores (positive and negative) for all labels.
result = client.text_classification(text)
print(result)
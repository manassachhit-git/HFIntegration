from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from transformers.utils.logging import set_verbosity_error

set_verbosity_error()

# Load Hugging Face text-generation pipeline (NOT summarization)
hf_pipeline = pipeline(
    "text-generation",
    model="facebook/bart-large-cnn",
    device=-1
)

# Wrap inside LangChain
llm = HuggingFacePipeline(pipeline=hf_pipeline)

# Prompt template
template = PromptTemplate.from_template(
    "Summarize the following text in simple English so that a {age}-year-old can understand it.\n\n{text}\n\nSummary:"
)

# Build chain
summarizer_chain = template | llm

# User input
text_to_summarize = input("\nEnter text to summarize:\n")
age = input("Enter target age for simplification:\n")

# Invoke chain
summary = summarizer_chain.invoke({
    "text": text_to_summarize,
    "age": age
})

print("\n🔹 Generated Summary:")
print(summary)

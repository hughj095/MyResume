### This file uses Hugging Face's transformers module to ingest a dataset through a RAG solution 
###  and output a context to train the OpenAI API within the token limitation.

import openai
import torch
from transformers import DPRQuestionEncoder, DPRQuestionEncoderTokenizer, DPRContextEncoder, DPRContextEncoderTokenizer
from datasets import load_dataset
import faiss

# Set up OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Load the models and tokenizers
question_encoder = DPRQuestionEncoder.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
question_tokenizer = DPRQuestionEncoderTokenizer.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
context_encoder = DPRContextEncoder.from_pretrained("facebook/dpr-ctx_encoder-single-nq-base")
context_tokenizer = DPRContextEncoderTokenizer.from_pretrained("facebook/dpr-ctx_encoder-single-nq-base")

# Load the dataset
dataset = load_dataset('wikipedia', '20220301.simple', split='train[:1%]')
docs = dataset['text']

# Encode the documents
context_embeddings = []
for doc in docs:
    inputs = context_tokenizer(doc, return_tensors='pt', max_length=512, truncation=True)
    embedding = context_encoder(**inputs).pooler_output.detach().cpu().numpy()
    context_embeddings.append(embedding)

context_embeddings = torch.tensor(context_embeddings).squeeze(1)

# Build the FAISS index
index = faiss.IndexFlatL2(context_embeddings.shape[1])
index.add(context_embeddings.numpy())

def retrieve(query, k=5):
    inputs = question_tokenizer(query, return_tensors='pt')
    question_embedding = question_encoder(**inputs).pooler_output.detach().cpu().numpy()
    D, I = index.search(question_embedding, k)
    retrieved_docs = [docs[i] for i in I[0]]
    return retrieved_docs

def summarize_documents(documents):
    summaries = []
    for doc in documents:
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Summarize the following document:\n\n{doc}",
            max_tokens=150,
            temperature=0.5
        )
        summaries.append(response.choices[0].text.strip())
    return summaries

def generate_response(query):
    retrieved_docs = retrieve(query)
    summaries = summarize_documents(retrieved_docs)
    context = " ".join(summaries)
    prompt = f"Question: {query}\nContext: {context}\nAnswer:"
    
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150,
        temperature=0.5
    )
    return response.choices[0].text.strip()

# Example usage
query = "What is the capital of France?"
response = generate_response(query)
print(response)

# Gen AI Training Day Workshop

## What are these workshops for?

These workshops were developed for in-person instructor-lead training.

https://www.awstrainingday.ca/


## Workshops Outline

### Beginner Workshop

- `001.ipynb` (10 mins)
  - Boto3 Client
  - Zero-Shot
  - Single Turn Conversation
  - Bedrock Runtime and InvokeModel
  - Comparing Models
    - Amazon Titan Text Express V1 
    - Claude Haiku 3
  - Load Local Files
    - Use Amazon Q Developer to generate function

- `002.ipynb` (10 mins)
  - Few-Shot
  - In-Context Learning
  - Packaging Function

- `003.ipynb` (30 mins)
  - Multi-turn Conversation
  - Multi-turn with Invoke Model
  - Multi-turn with Converse API
  - Session or Chat History Management (Knowledgebase)
  - NOTES:
    - Message History (how is the conversation being chained)
    - Summarization (what happens if hte message history gets too long?)

- `004.ipynb` (30 mins)
  - reAct Reasoning
  - Tool Use
  - Gaurd Rails
  
- `005.ipynb` (10 mins)
  - Generate a frontend using Gradio
  - Generate a frontend using Streamlit
  - Generate a frontend using v0

### Intermediate Workshop

#### OpenVino
- How to configure JupyterLabs on a VM
- run a model using hugging face
- run a model using hugging face + OpenVino
- run a model using hugging face + OpenVino + Quantization

#### OPEA
- How to right-size compute resources for LLMs
- How to deploy Mega-services for OPEA

## Prerequisite Setup 

- [AWS Setup](./docs/aws-setup.md)
- [Hugging Face Setup](./docs/hf-setup.md)

## Refernece Materials

These are other workshops or repositories that cover similar topics: 
- https://github.com/aws-samples/amazon-bedrock-workshop
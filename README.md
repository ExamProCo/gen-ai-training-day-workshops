# Gen AI Training Day Workshop

## Beginner Workshop

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

## Setup

### Install AWS CLI

We don't directly need the AWS CLI but its useful to have around for debugging or quickly creating on off resources like an S3 Bucket

```sh
chmod u+x ./bin/install_aws_cli
./bin/install_aws_cli
```

> SageMaker StudioLabs JuypterLabs Workspace will have AWS CLI preinstalled

### Configure your AWS Credentials

You can set your AWS Credentials two ways:
- Env Vars
- AWS Credentials Profile


Cloud developer enviroments will require you set env vars since they can't persist or store an `~/.aws/credentaisls` file:

```sh
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_DEFAULT_REGION="ca-central-1"
```

Local developer enviroments you can use AWS configure which will persist or store credentials in a `~/.aws/credentaisls` file:

```sh
aws configure
```

> Please consider there can be limitations of models or features based on selected region. In worst-case we will fallback to nearest best suppported region>

> SageMaker StudioLabs JuypterLabs Workspace will use your user roll for permissions so you don't need to set credentinals

## Refernece Materials

These are other workshops or repositories that cover similar topics: 
- https://github.com/aws-samples/amazon-bedrock-workshop
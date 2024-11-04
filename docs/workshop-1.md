## 0. Starting Point

Logged into the AWS Management Console.

- We plan to do everything in `us-west-2`
    - Different regions can have different model avaliablity and to ensure we have all avaliable models we are going to work in AWS's primary region.

## Cost Guestimation

- $0.10 USD - SageMaker Studio Notebook

## 1. Launch and Prepare ML-Ready Dev Environment

We are going to use SageMaker Studio Notebooks.

- Create your SageMaker domain by choosing `Quick setup for a single user`
    - This will take between 5-10 mins
    - While waiting for our domain to provision we'll cover basics of LLMs
- Within SageMaker Console go to `Studio` and  `Open Studio`
    - ~1m for SageMaker Studio to open
    - There is no cost opening SageMaker Studio, however there are similar UX experiences like SageMaker Canvas which will cost to launch their interface.
- Within SageMaker Studio go to `Jupyter Labs` and `Create JupyterLab Space`
    - Provide any name
    - Sharing should be set to `private`
    - Wait for the space to create
- Run Space (launch with default settings)
    - ml.t3.medium 
        - 2vCPUs,4 GiB
        - $0.05 / hour (~35.60 USD / month)
        - 250 hours - Free Tier usage per month for the first 2 months
    - SageMaker Distrubtion 2.0
    - 5 GB storage
    Consideration: Because we plan to use Amazon Bedrock for workshop 1 you could technically do this entire workshop in a local development enviroment or any non GPU enviroment. 
    - ~3mins to start the space
- `Open JupyterLab` to launch the notebook
- Lefthand side click `Git` tab and `Clone a Repository`
    - Provide in the `Git repositories URL(.git):` the following value:
        `https://github.com/ExamProCo/gen-ai-training-day-workshops.git`

## Notebook Considerations

All of our notebooks are going to utilized the default `(Python ipykernal)`.

The runtime will come preinstalled with multiple python libraries. So if you attempting to run these workshops locally you may need to install more libraries.

### 3. Request Model Access for Amazon Bedrock Models

- Goto `Amazon Bedrock Console` in the left hand column in under `Bedrock Configurations` go to `Model Access`
- Choose to `Enable all models`
    - Note that some models will not be enabled
    - Note that some models require additional information to activate
    - Note that some models require time either seconds, minutes or days to get access

## 4. 001 Learn the Basics of LLMs

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

### Tip 1: Always check your python version

In my experience, when working with AI workloads, due to rapid pace of library development often you run into depedency conflicts. 

Always check your Python version as a starting point.

### Tip 2: Always use conda and create a new Python enviroment for each AI workload

In my experience, when working with multiple AI projects you can quickly run into depedency conflicts because different projects will rely on different versions of a python library due to different featureset.

Always use conda and create a python enviroment.

In this case of this workshop we are skipping this step.

### Tip 3: When install libraries remember to restart your Kernal

When you are working with Jupyter Notebooks you will sometimes be installing libraries eg. `%pip install pytorch`

For them to take affect you will need to restart your kernal, however any variables you have set will be cleared and so you will need to rerun previous cells, normally for the start.

### Tip 4: Be aware there are lots of different clients for Amazon Bedrock

- bedrock (controlling infrastructure and settings of bedrock)
- bedrock-runtime (invoking LLMs in bedrock)
- bedrock-agent (working with Amanzon Bedrock Agent for a full agentic workflow)

[Search of Boto3 Bedrock clients](
https://boto3.amazonaws.com/v1/documentation/api/1.35.6/search.html?q=bedrock&check_keywords=yes&area=default)

### Tip 5: Different models have different prompt optimizations

If you read the documentation or model card of an LLM. They will describe the best way to prompt the model.

- Amazon Titan eg. `{{double brackets}}`
- Anthropic Claude eg. `<xml>tags</xml>`

### Tip 6: Invoke Model has different body parameters and ouputs for different models.

If you compare 
- Titan Express
- Claude 2
- Claude 3 Haiku

You will notice their inputs are different because these are the underlying parameters required for these APIs.

InvokeModel does not standardize the inputs.

Also notice that Claude 3 Haiku follow a soon to be familary json message structure format.

This is called the Messages API and we will see that many latest LLMs model follow the json message json structure.

### Tip 7. Manage Your Prompts In A Modaular External Way

In development you can provide prompts inline, however as you need to evaluate multiple models and multiple prompts you want to manage your prompts externally.

The easist way is load a local text file.

There are more advanced ways like using Amazon Bedrock Prompt Management.

### Tip 8. Single-Turn convesation is create for traditionals ML tasks 

A single-turn conversation returns a single response, and an LLM can serve the same purpose as traditional ML models that perform single outputs eg. Classification, Regression, Catagorization

The trade-off is that it can be more computational expensive to use an LLM however it requires less ML knowledge to implement these kind of tasks.

In the case you need raw performance at scale you may want to use or train an ML model for predictions.

## 5. 002 Documenting Towards Production

- `002.ipynb` (10 mins)
  - Few-Shot
  - In-Context Learning
  - Packaging Function

### Tip 1: In-Context Learning

We can "train" the model to perform tasks through prompting intially what we want to do.

This is called `prompt engineering` and `In-Context learning` means any information we provide upfront the model needs to learn from.

- Tell what do: You are a japanese language teacher
- Provide it knowledge: Provide examples of outputs

### Tip 2: Slowly move your code from Juypter Notebooks to Production Code

Jupyter notebooks are great for documenting and experimenting, however we *generally wouldn't want to put a Jupyer Notebook into production. 

We would want rework out code into regular coding files and define functions and classes.

Think of workflow (Andrew's Personal opinion):
- Get it working in Jupyter Notebook
- Start refacting in another Juypter Notebook as functions
- Start refacting in your code as classes.

> Notice how we have to change the way our prompt works when its not in a function and within a function

## 6. 003 Building Code For Production

- `003.ipynb` (30 mins)
  - Multi-turn Conversation
  - Multi-turn with Invoke Model
  - Multi-turn with Converse API
  - Session or Chat History Management (Knowledgebase)
  - NOTES:
    - Message History (how is the conversation being chained)
    - Summarization (what happens if the message history gets too long?)

### Tip 1: System Prompt Templates

Look at the prompt template we used.

### Tip 2: As a conversation grows so does your context window because you are feeding in the previous text.

The reason why LLMs can more expensive as the conversation goes is because you appending the ouputs to your message history, and everytime you invoke the model you passing in the full history.

Eventually you will exhaust resources, or there will be so much information your LLM will start performing poorly.


> Think of the snake the eats it own tail.

### Tip 3: Sqlite is a great small database when rapidly protoyping LLM workflows

Sqlite will produce a single file representing your database, that allows you to store relational data.

 Its a good start for:
 - session management
 - simple vectorstore

 ### Tip 4: ConverseAPI is better for conversations

 AWS first came out with InvokeModel and its still used for single-turn conversations.

 For multi-turn conversations you want to use converse API because it standardize on the messages API format and it has additional functionality like tool use.

### Tip 5 ConverseAPI instance will remember chat history

With InvokeModel if you were to pass the same chat history with no changes it will just work.

With ConverseAPI it will remember the conversation, so you'll need to progress the conversation.

 ### Tip 6: Use Streaming for immediate feedback

 You can use the streaming API so that users can start seeing output response immediately.

 ## 04 Building an Agent

 - `004.ipynb` (30 mins)
  - reAct Reasoning
  - Tool Use
  - Gaurd Rails

### Tip 1: What makes and Agent an agent is when it has agency

When an agent can go beyond a multiple-turn conversation to take external action like:
- Using a RAG (retriving data before it replies)
- Decide to call external functions (tool use)
- Self-reflect the conversation befor replying

Then we are describing "agency", because its going beyond the confines of a simple convesration.

 ## 05 Fast Prototyping Frontends

 - `005.ipynb` (10 mins)
  - Generate a frontend using Gradio
  - Generate a frontend using Streamlit
  - Generate a frontend using v0

### Tip 1: Easy frameworks to get going

There are frameworks that make it easy to develop a frontend website to serve your models UI, not something you would want for production.

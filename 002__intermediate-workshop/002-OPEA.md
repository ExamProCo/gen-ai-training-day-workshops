## !Important Please do this ahead of time!

Create a Hugging Face account and accept terms for Llama-3.2-1B
https://huggingface.co/meta-llama/Llama-3.2-1B

This can take minutes to hours for approval.

## Create Role to use SSM Sessions Manager

- Create new role
- Choose `EC2`
- Choose `Ubunutu 24.04 LTS`
- Add the policy `AmazonSSMManagedInstanceCore`
- Name the role `SSMforEC2`

## Launch an EC2 instance

- m7i.4xlarge
- 80 GB
- Proceed with no key pair
- Choose SSMforEC2 Role
- Open port 80 to the internet `0.0.0.0/0`
    - this can be set with `Allow HTTP traffic from the internet`

## Connect via Sessions Manager

Click `Connect` and Launch with Sessions Manager

Switch users

```sh
sudo su - ubuntu
```

## Clone the MegaServices Repo

```sh
git clone https://github.com/opea-project/GenAIExamples.git
```

## Install and Test Docker

Install docker using the bash script included in the repo.
We'll need to give ourselves permissions to execute the file.
```sh
cd GenAIExamples/ChatQnA/docker_compose
chmod +x ./install_docker.sh
./install_docker.sh
```

> Maybe we can juse source ./install_docker.sh to not require to change permissions

When install we are required to sudo to use docker.
This will cause us issues in future cases so we'll
change it so we can use docker sudoless.

```sh
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
```

Test docker

```sh
docker run hello-world
```

## Set HuggingFace Credentials

Get your API key and set it:

```sh
export HUGGINGFACEHUB_API_TOKEN="YOUR_KE"
```

## Setup Env Vars

We need to setup the host IP (the public facing IP address)
Since we are not using proxy eg. Jumpbox we set our proxy to localhost

```sh
export host_ip=$(hostname -I | awk '{print $1}')
export no_proxy="localhost"
```

```sh
cd intel/cpu/xeon/
vi set_env.sh
```

Using vi, we need to change the LLM.
We are doing this because this is a small model requiring less compute and memory.
However the instance we prepped is sufficient for the original Mistral 7B model.

```sh
export LLM_MODEL_ID="meta-llama/Llama-3.2-1B"
```

```sh
chmod +x ./set_env.sh
source ./set_env.sh
```

Confirm the env vars were set:

```sh
env | grep _MODEL
```

## Startup up containers

```sh
docker compose -f compose.yaml up -d
```

> We can just write docker compose up, the repo contains more than once compose file so we are just being verbose in our selection.

Wait for all services to start

## Ensure TGI service is connected

Our model is being served by Text Generation Inference (TGI).
This is what is downloading the model from hugging face and allowing us to do inference.

We need to ensure its in a connected state so lets check its logs.

We can list all containers see if TGI died
```sh
docker ps -a # look for tgi-service unique id, show all in case one fails
```

We will want to format the columns to make our lives easier
```sh
docker ps --format "{{.ID}} {{.Names}} {{.Ports}}" | column -t
```

Here are some commonly used placeholders for --format:
{{.ID}}: Container ID
{{.Image}}: Image name
{{.Command}}: Command used to start the container
{{.CreatedAt}}: Creation date and time
{{.RunningFor}}: Uptime
{{.Ports}}: Port mappings
{{.Status}}: Status of the container
{{.Names}}: Container name

```sh
docker logs TGI_SERVICE_ID
```

## Test Service

```sh
curl http://$host_ip:8888/v1/chatqna \
-H "Content-Type: application/json" \
-d '{
    "messages": "What is the revenue of Nike in 2023?"
}'
```
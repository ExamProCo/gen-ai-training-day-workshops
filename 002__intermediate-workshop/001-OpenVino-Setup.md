## Specs

- m7i.xlarge
- 50 GB
- SSMEC2Role
- open port 8888 for your IP address

## Switch Users

```sh
sudo su - ubuntu
```

## Install Conda and Jupyter Lab

```sh
mkdir -p /home/ubuntu/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /home/ubuntu/miniconda3/miniconda.sh
bash /home/ubuntu/miniconda3/miniconda.sh -b -u -p /home/ubuntu/miniconda3
rm /home/ubuntu/miniconda3/miniconda.sh
source /home/ubuntu/miniconda3/bin/activate
conda init --all          
conda create --name openvino python=3.10.0 -y
conda activate openvino
conda install -c conda-forge tensorflow jupyterlab -y
```

## Run Jupyter Lab

```sh
jupyter lab --ip 0.0.0.0
```



## Install Miniconda

```sh
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
source ~/miniconda3/bin/activate
conda init --all
```

## Create Env

```sh
conda create --name openvino python=3.10.0
conda activate openvino
```

## Install Deps

```sh
conda install -c conda-forge tensorflow jupyterlab
```

## Start Jupypter Lab

```sh
jupyter lab --ip 0.0.0.0
```


## CloudFormation EC2 - Gitpod

- Configure AWS Creds
```
aws configure
```

- Deploy CFN Stack

```
aws cloudformation deploy --template-file ./002__intermediate-workshop/cfn/openvino.yaml --stack-name bayko-test --capabilities CAPABILITY_NAMED_IAM --parameter-overrides InstanceType=t3.medium VpcId=vpc-c3be22b9
```
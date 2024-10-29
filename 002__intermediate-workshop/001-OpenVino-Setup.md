## Specs

- m7i.xlarge
- 50 GB
- SSMEC2Role
- open port 8888 for your IP address

## Switch Users

```sh
sudo su - ubuntu
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
#!/bin/bash
mkdir -p /home/ubuntu/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh
bash /tmp/miniconda.sh -b -u -p /home/ubuntu/miniconda3

source /home/ubuntu/miniconda3/bin/activate
conda init --all          
conda create --name openvino python=3.10.0 -y
conda activate openvino
conda install -c conda-forge tensorflow jupyterlab ffmpeg -y

jupyter lab --no-browser --allow-root --ip 0.0.0.0
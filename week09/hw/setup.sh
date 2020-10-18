#!/bin/bash
EFS_IP=172.31.11.130 #ENTER YOUR EFS MOUNT IP HERE FROM aws efs create-mount-target command
GIT_REPO=https://github.com/MIDS-scaling-up/v2.git # replace with your repo if desired.
GIT_FOLDER=w251

# Mount data dir
cd ~
mkdir ~/data
sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport $EFS_IP:/ ~/data

# setup NVIDIA docker runtime
sudo tee /etc/systemd/system/docker.service.d/override.conf <<EOF
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd --default-shm-size="1G"                            --host=fd://                            --storage-driver=overlay2 --add-runtime=nvidia=/usr/bin/nvidia-container-runtime
LimitMEMLOCK=infinity
LimitSTACK=67108864
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker

# Build and run container
cd ~/data
git clone $GIT_REPO $GIT_FOLDER
cd ~/data/$GIT_FOLDER/week09/hw/docker
docker build . -t openseq2seq
docker run --runtime=nvidia -d --name openseq2seq --net=host -e SSH_PORT=4444 -v ~/data:/data -p 6006:6006 openseq2seq
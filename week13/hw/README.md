# Homework 13: Deep Learning SDK (the unofficial one, by Dustin Franklin)

We find that Dusty's repo has been one of the best places to find cool examples and cool code for doing something practical, so hopefully you'll enjoy it as well.  In this homework, you'll be using transfer learning to create a model that classifies plants, directly on your Jetson!

## Set up your default Docker runtime to Nvidia
Edit /etc/docker/daemon.json and add `"default-runtime": "nvidia"`
```
{
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    },

    "default-runtime": "nvidia"
}
```
Now restart docker, e.g. `service docker restart`

## Set up and build the docker image
Review Dusty's [github repo](https://github.com/dusty-nv/jetson-inference), then build the container:
```bash
$ git clone --recursive https://github.com/dusty-nv/jetson-inference
$ cd jetson-inference
$ docker/build.sh
```

## Start the runtime
Assuming we have the image built, let's start it!
```bash
$ docker/run.sh
```

## Training the model
We suggest that you loosely follow [these instructions](https://github.com/dusty-nv/jetson-inference/blob/master/docs/pytorch-plants.md) to train at least two networks: ResNet18 and Wide ResNet 50-2 on the PlantCLEF dataset.  Just a few notes:
* Review the [repo](https://github.com/dusty-nv/pytorch-classification) and the [train script](https://github.com/dusty-nv/pytorch-imagenet/blob/master/train.py)
* Please use [the original pytorch example script](https://github.com/pytorch/examples/blob/master/imagenet/main.py) for training as it is more up to date
* Once again, please use python3 for all commands
* Train for 100 epochs 
* ResNet18 / Wide ResNet 50-2 Hint: review the [TorchVision model catalog](https://pytorch.org/docs/stable/torchvision/models.html)
* Adjust batch size as necessary


## Train.py Args

```
root@w251-xavier:/jetson-inference/python/training/classification# python3 train.py -h
usage: train.py [-h] [--model-dir MODEL_DIR] [-a ARCH] [--resolution N] [-j N]
                [--epochs N] [--start-epoch N] [-b N] [--lr LR] [--momentum M]
                [--wd W] [-p N] [--resume PATH] [-e] [--pretrained]
                [--world-size WORLD_SIZE] [--rank RANK] [--dist-url DIST_URL]
                [--dist-backend DIST_BACKEND] [--seed SEED] [--gpu GPU]
                [--multiprocessing-distributed]
                DIR

PyTorch ImageNet Training

positional arguments:
  DIR                   path to dataset

optional arguments:
  -h, --help            show this help message and exit
  --model-dir MODEL_DIR
                        path to desired output directory for saving model
                        checkpoints (default: current directory)
  -a ARCH, --arch ARCH  model architecture: alexnet | densenet121 |
                        densenet161 | densenet169 | densenet201 | googlenet |
                        inception_v3 | mnasnet0_5 | mnasnet0_75 | mnasnet1_0 |
                        mnasnet1_3 | mobilenet_v2 | resnet101 | resnet152 |
                        resnet18 | resnet34 | resnet50 | resnext101_32x8d |
                        resnext50_32x4d | shufflenet_v2_x0_5 |
                        shufflenet_v2_x1_0 | shufflenet_v2_x1_5 |
                        shufflenet_v2_x2_0 | squeezenet1_0 | squeezenet1_1 |
                        vgg11 | vgg11_bn | vgg13 | vgg13_bn | vgg16 | vgg16_bn
                        | vgg19 | vgg19_bn | wide_resnet101_2 |
                        wide_resnet50_2 (default: resnet18)
  --resolution N        input NxN image resolution of model (default: 224x224)
                        note than Inception models should use 299x299
  -j N, --workers N     number of data loading workers (default: 2)
  --epochs N            number of total epochs to run
  --start-epoch N       manual epoch number (useful on restarts)
  -b N, --batch-size N  mini-batch size (default: 8), this is the total batch
                        size of all GPUs on the current node when using Data
                        Parallel or Distributed Data Parallel
  --lr LR, --learning-rate LR
                        initial learning rate
  --momentum M          momentum
  --wd W, --weight-decay W
                        weight decay (default: 1e-4)
  -p N, --print-freq N  print frequency (default: 10)
  --resume PATH         path to latest checkpoint (default: none)
  -e, --evaluate        evaluate model on validation set
  --pretrained          use pre-trained model
  --world-size WORLD_SIZE
                        number of nodes for distributed training
  --rank RANK           node rank for distributed training
  --dist-url DIST_URL   url used to set up distributed training
  --dist-backend DIST_BACKEND
                        distributed backend
  --seed SEED           seed for initializing training.
  --gpu GPU             GPU id to use.
  --multiprocessing-distributed
                        Use multi-processing distributed training to launch N
                        processes per node, which has N GPUs. This is the
                        fastest way to use PyTorch for either single node or
                        multi node data parallel training
```


## To submit
Please submit the time it took you to train the model along with the final accuracy top1/top5 that you were able to achieve. Did you get better results with Wide ResNet50 or ResNet18? What training parameters you adjusted? Why? How long did the training take you? Please save your trained model, we'll use it for the lab. Also please review the architecture of the [Wide ResNet 50-2](https://pytorch.org/hub/pytorch_vision_wide_resnet/) network, we will discuss it in class.


Credit / no credit only

# Submission

The results were better with the Wide ResNet50 rather than ResNet 18. The only paramater I adjusted was the epochs, because training the resnet50 would've taken over a day. 

| Model             | Epochs | Training Time | Acc@1    | Acc@5  |
| --------          | ------ | ------------- | ------   | ------ |
| ResNet18          | 35     | ~3 hours      | 38.943   | 74.273 |
| Wide ResNet 50-2  | 20     | ~14.5 hours   | 40.176   | 77.797 |

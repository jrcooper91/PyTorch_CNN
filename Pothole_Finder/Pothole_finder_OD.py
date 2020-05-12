#Script written by Jennifer Cooper to train a set of dashcam data to detect potholes, stoplights, and cars. Python 3.73. On redbud, Redhat Enterprise Linux 6 with 4 cores.

from __future__ import division

from models import *
from utils.utils import *
from utils.datasets import *
from utils.parse_config import *

import os
import sys
import time
import datetime
import argparse

import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision import transforms
from torch.autograd import Variable
import torch.optim as optim
#import torch.optim as opt
import warnings
warnings.filterwarnings("ignore")

epochs     = 10   #how many times to repeat each set of batches
batch_size = 64  #how many images per batch
conf_thres = 0.8 #object confidence threshold
nms_thres  = 0.4 #iou thresshold for non-maximum suppression
img_size   = 416 #default required for Yolov3

checkpoint_interval = 2 #interval between saving model weights
checkpoint_dir      = '/data2/jrcooper/PyTorch_Training/Potholes/data/checkpoint'

#paths to important files 
image_folder      = '/data2/jrcooper/PyTorch_Training/Potholes/data/train/images'
model_config_path = '/data2/jrcooper/PyTorch_Training/Potholes/data/config/yolov3.cfg'
weights_path      = '/data2/jrcooper/PyTorch_Training/Potholes/data/config/yolov3.weights'
class_path        = '/data2/jrcooper/PyTorch_Training/Potholes/data/config/tesla_dashcam.names'
data_config_path  = '/data2/jrcooper/PyTorch_Training/Potholes/data/config/tesla_dashcam.data'

os.makedirs("checkpoint", exist_ok=True)

classes = load_classes(class_path)
print(classes)

# Get data configuration
train_path = '/data2/jrcooper/PyTorch_Training/Potholes/data/train.txt'

# Get more important parameters
learning_rate = 0.001 #rate of change in loss gradient 
momentum = 0.9        #accumulation of past gradients to determine best direction to continue
decay = 0.0005        
burn_in = 1000
n_cpu=8         #threads to use, each core has 2 threads

# Initiate model
model = Darknet(model_config_path)
model.load_weights(weights_path)
model.to('cpu')
model.train()

#This initiates the training. Each epoch takes approximately 2.5 hours to complete on a mid-2014 MacBook Pro with 8GB of memory and an Intel Core i5 processor.
#The weight file from each epoch is automatically saved in the 'checkpoint' directory. It will be loaded below. 
dataloader = torch.utils.data.DataLoader(
    ListDataset(train_path), batch_size=16, shuffle=False, num_workers=n_cpu)

Tensor = torch.FloatTensor

optimizer = torch.optim.Adam(filter(lambda p: p.requires_grad, model.parameters())) #Adaptive Moment Optimization

for epoch in range(epochs):
    for batch_i, (_, imgs, targets) in enumerate(dataloader):
        imgs = Variable(imgs.type(Tensor))
        targets = Variable(targets.type(Tensor), requires_grad=False)

        optimizer.zero_grad()
        #print(targets)
        loss = model(imgs, targets)

        loss.backward()
        optimizer.step()

        print(
            "[Epoch %d/%d, Batch %d/%d] [Losses: x %f, y %f, w %f, h %f, conf %f, cls %f, total %f, recall: %.5f, precision: %.5f]"
            % (
                epoch,
                #opt.epochs,
                epochs,
                batch_i,
                len(dataloader),
                model.losses["x"],
                model.losses["y"],
                model.losses["w"],
                model.losses["h"],
                model.losses["conf"],
                model.losses["cls"],
                loss.item(),
                model.losses["recall"],
                model.losses["precision"],
            )
        )

        model.seen += imgs.size(0)

    if epoch % checkpoint_interval == 0:
        model.save_weights("%s/%d.weights" % (checkpoint_dir, epoch))

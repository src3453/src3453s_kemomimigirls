import os
import cv2
import numpy as np

HEADS_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/textures/src/rabbit/heads"

heads = os.listdir(HEADS_DIR)
colors = {}

for head_name in heads:
    head = cv2.imread(os.path.join(HEADS_DIR,head_name),cv2.IMREAD_UNCHANGED)
    colors[head_name.split(".")[0]]=[tuple(head[23,12,:][[2,1,0,3]])]
print(colors)
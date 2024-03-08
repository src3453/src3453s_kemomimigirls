import os
import cv2
import numpy as np
import re

HEADS_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/textures/entity/fox"

heads = os.listdir(HEADS_DIR)

for head_name in heads:
    if head_name.endswith(".png"):
        if re.findall("sleep",head_name) == []:
            head = cv2.imread(os.path.join(HEADS_DIR,head_name),cv2.IMREAD_UNCHANGED)
            result = head.copy()
            result[30,9,:] = head[29,9,:]
            result[29,9,:] = head[30,9,:]
            result[30,14,:] = head[29,14,:]
            result[29,14,:] = head[30,14,:]
            cv2.imwrite(os.path.join(HEADS_DIR,head_name),result)
            print(head_name)

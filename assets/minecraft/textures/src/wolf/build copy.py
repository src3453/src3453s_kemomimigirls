import os
import cv2
import numpy as np

HEADS_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/textures/entity/wolf"
SLEEP_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/textures/src/cat/sleep"

heads = os.listdir(HEADS_DIR)
sleep_path = os.listdir(SLEEP_DIR)[0]

for head_name in heads:
    if head_name.endswith(".png"):
        head = cv2.imread(os.path.join(HEADS_DIR,head_name),cv2.IMREAD_UNCHANGED)
        sleep = cv2.imread(os.path.join(SLEEP_DIR,sleep_path),cv2.IMREAD_UNCHANGED)
        result = head
        for y in range(result.shape[0]):
            for x in range(result.shape[1]):
                if sleep[y,x,3] != 0:
                    sleep[y,x,3] = 255
                    if all(sleep[y,x,:] == (185, 206, 255, 255)):
                        result[y,x,:] = head[28,10,:]
                    else:
                        result[y,x,:] = sleep[y,x,:]
        cv2.imwrite(os.path.join(HEADS_DIR,head_name),result)
        print(head_name)
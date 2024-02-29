import os
import cv2
import numpy as np

HEADS_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/textures/entity/catcwd/heads"
COSTUMES_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/textures/entity/catcwd/costumes"
OUTPUT_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/optifine/random/entity/cat/"

heads = os.listdir(HEADS_DIR)
costumes = os.listdir(COSTUMES_DIR)

for head_name in heads:
    for costumes_name in costumes:
        head = cv2.imread(os.path.join(HEADS_DIR,head_name),cv2.IMREAD_UNCHANGED)
        costume = cv2.imread(os.path.join(COSTUMES_DIR,costumes_name),cv2.IMREAD_UNCHANGED)
        result = head | costume
        cv2.imwrite(os.path.join(OUTPUT_DIR,head_name.split(".")[0]+costumes_name),result)
        print(head_name.split(".")[0]+costumes_name)
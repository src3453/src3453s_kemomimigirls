import os
import cv2
import numpy as np

HEADS_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/textures/src/cat/heads"
COSTUMES_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/textures/src/cat/costumes"
SLEEP_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/textures/src/cat/sleep"
OUTPUT_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/optifine/random/entity/cat/"

colors = {"all_black":[(25,18,18,255)],
"british_shorthair":[(165,165,165,255)],
"calico":[(45,45,45,255),(202,202,202,255),(255,149,61,255)],
"jellie":[(138,115,107,255)],
"persian":[(255,203,137,255)],
"ragdoll":[(224,186,163,255)],
"red":[(255,155,88,255)],
"siamese":[(157,124,103,255)],
"tabby":[(110,62,33,255)],
"black":[(255,192,241,255)],
"white":[(228,228,228,255)]}
mask_colors = [(255,0,255,255),(127,0,255,255),(255,0,127,255)]

heads = os.listdir(HEADS_DIR)
costumes = os.listdir(COSTUMES_DIR)
sleeps = os.listdir(SLEEP_DIR)[0:1]

for head_name in heads:
    for costume_name in costumes:
        for i,sleep_name in enumerate(sleeps):
            head = cv2.imread(os.path.join(HEADS_DIR,head_name),cv2.IMREAD_UNCHANGED)
            costume = cv2.imread(os.path.join(COSTUMES_DIR,costume_name),cv2.IMREAD_UNCHANGED)
            sleep = cv2.imread(os.path.join(SLEEP_DIR,sleep_name),cv2.IMREAD_UNCHANGED)
            color_name = head_name.split(".")[0]
            costume = costume[:,:,[2,1,0,3]]
            if color_name == "calico":
                for y in range(costume.shape[0]):
                    for x in range(costume.shape[1]):
                        if all(costume[y,x,:] == mask_colors[0]):
                            costume[y,x,:] = colors[color_name][0]
                        if all(costume[y,x,:] == mask_colors[1]):
                            costume[y,x,:] = colors[color_name][1]
                        if all(costume[y,x,:] == mask_colors[2]):
                            costume[y,x,:] = colors[color_name][2]
                            
            else:
                for y in range(costume.shape[0]):
                    for x in range(costume.shape[1]):
                        if all(costume[y,x,:] == mask_colors[0]):
                            costume[y,x,:] = colors[color_name][0]
                        if all(costume[y,x,:] == mask_colors[1]):
                            costume[y,x,:] = np.clip(np.array(colors[color_name][0])*1.02,0,255)
                        if all(costume[y,x,:] == mask_colors[2]):
                            costume[y,x,:] = np.clip(np.array(colors[color_name][0])*0.98,0,255)
            costume = costume[:,:,[2,1,0,3]]
            result = head
            for y in range(result.shape[0]):
                for x in range(result.shape[1]):
                    if costume[y,x,3] != 0:
                        costume[y,x,3] = 255
                        result[y,x,:] = costume[y,x,:]
            for y in range(result.shape[0]):
                for x in range(result.shape[1]):
                    if sleep[y,x,3] != 0:
                        sleep[y,x,3] = 255
                        result[y,x,:] = sleep[y,x,:]
            cv2.imwrite(os.path.join(OUTPUT_DIR,head_name.split(".")[0]+str(int(costume_name.split(".")[0])+i*16)+".png"),result)
            print(head_name.split(".")[0]+str(int(costume_name.split(".")[0])+i*16)+".png")
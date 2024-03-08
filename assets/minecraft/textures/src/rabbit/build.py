import os
import cv2
import numpy as np

HEADS_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/textures/src/rabbit/heads"
COSTUMES_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/textures/src/rabbit/costumes"
OUTPUT_DIR = "/home/src3453/.local/share/multimc/instances/1.20.1/.minecraft/resourcepacks/src3453s_foxgirl/assets/minecraft/optifine/random/entity/rabbit/"

colors = {'salt': [(149, 149, 149, 255)], 'caerbannog': [(217, 217, 217, 255)], 'toast': [(48, 48, 48, 255)], 'brown': [(88, 48, 38, 255)], 'gold': [(255, 191, 137, 255), (255, 225, 151, 255)], 'black': [(37, 14, 14, 255)], 'white': [(217, 217, 217, 255)], 'white_splotched': [(173, 126, 185, 255)]}
mask_colors = [(255,0,255,255),(127,0,255,255),(255,0,127,255)]

heads = os.listdir(HEADS_DIR)
costumes = os.listdir(COSTUMES_DIR)

for head_name in heads:
    formatted_name = head_name.split(".")[0][:-1]
    for i,color in enumerate(colors[formatted_name]):
        for costume_name in costumes:
            head = cv2.imread(os.path.join(HEADS_DIR,head_name.split(".")[0][:-1]+str(i)+".png"),cv2.IMREAD_UNCHANGED)
            costume = cv2.imread(os.path.join(COSTUMES_DIR,costume_name),cv2.IMREAD_UNCHANGED)
            color_name = formatted_name
            costume = costume[:,:,[2,1,0,3]]
            for y in range(costume.shape[0]):
                for x in range(costume.shape[1]):
                    if all(costume[y,x,:] == mask_colors[0]):
                        costume[y,x,:] = color
                    if all(costume[y,x,:] == mask_colors[1]):
                        costume[y,x,:] = np.clip(np.array(color[0])*1.02,0,255)
                    if all(costume[y,x,:] == mask_colors[2]):
                        costume[y,x,:] = np.clip(np.array(color[0])*0.98,0,255)
            costume = costume[:,:,[2,1,0,3]]
            result = head
            for y in range(result.shape[0]):
                for x in range(result.shape[1]):
                    if costume[y,x,3] != 0:
                        costume[y,x,3] = 255
                        result[y,x,:] = costume[y,x,:]
            cv2.imwrite(os.path.join(OUTPUT_DIR,formatted_name+str(int(costume_name.split(".")[0])+i*len(costumes))+".png"),result)
            print(formatted_name+str(int(costume_name.split(".")[0])+i*len(costumes))+".png")
import os
import cv2
import numpy as np

HEADS_DIR = r"C:\Users\y2k34\AppData\Roaming\.minecraft\resourcepacks\src3453s_foxgirl\assets\minecraft\textures\src\fox\heads"
COSTUMES_DIR = r"C:\Users\y2k34\AppData\Roaming\.minecraft\resourcepacks\src3453s_foxgirl\assets\minecraft\textures\src\fox\costumes"
BOTTOMS_DIR = r"C:\Users\y2k34\AppData\Roaming\.minecraft\resourcepacks\src3453s_foxgirl\assets\minecraft\textures\src\fox\bottoms"
SLEEP_DIR = r"C:\Users\y2k34\AppData\Roaming\.minecraft\resourcepacks\src3453s_foxgirl\assets\minecraft\textures\src\fox\sleep"
OUTPUT_DIR = r"C:\Users\y2k34\AppData\Roaming\.minecraft\resourcepacks\src3453s_foxgirl\assets\minecraft\textures\src\fox\outputs\\"

colors = {
    "orange":[(0xff,0x9c,0x1e,255)],
    "arctic":[(0xd4,0xe8,0xee,255)],
    "black" :[(0x26,0x1b,0x1b,255)],
    "cherry":[(0xff,0x95,0x95,255)],
    "golden":[(0xff,0xd4,0x8a,255)],
    "brown" :[(0x79,0x34,0x1a,255)],
    "silver":[(0xb9,0xb9,0xb9,255)],
    "lavender":[(0xc5,0x7f,0xeb,255)],
    }
mask_colors = [(255,0,255,255)]

heads = os.listdir(HEADS_DIR)
costumes = os.listdir(COSTUMES_DIR)
bottoms = os.listdir(BOTTOMS_DIR)
sleeps = os.listdir(SLEEP_DIR)[0:1]
index = 1 

for head_name in heads:
    for bottoms_name in bottoms:
        for costume_name in costumes:
            for i,sleep_name in enumerate(sleeps):
                head = cv2.imread(os.path.join(HEADS_DIR,head_name),cv2.IMREAD_UNCHANGED)
                costume = cv2.imread(os.path.join(COSTUMES_DIR,costume_name),cv2.IMREAD_UNCHANGED)
                bottoms_img = cv2.imread(os.path.join(BOTTOMS_DIR,bottoms_name),cv2.IMREAD_UNCHANGED)
                sleep = cv2.imread(os.path.join(SLEEP_DIR,sleep_name),cv2.IMREAD_UNCHANGED)
                color_name = head_name.split(".")[0]
                costume = costume[:,:,[2,1,0,3]]
                for y in range(costume.shape[0]):
                    for x in range(costume.shape[1]):
                        if all(costume[y,x,:] == mask_colors[0]):
                            costume[y,x,:] = colors[color_name][0]
                costume = costume[:,:,[2,1,0,3]]
                result = head
                for y in range(result.shape[0]):
                    for x in range(result.shape[1]):
                        if bottoms_img[y,x,3] != 0:
                            bottoms_img[y,x,3] = 255
                            result[y,x,:] = bottoms_img[y,x,:]
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
                _index = str(index)
                cv2.imwrite(os.path.join(OUTPUT_DIR+"fox"+_index+".png"),result)
                print("fox"+_index+".png")
                cv2.imwrite(os.path.join(OUTPUT_DIR+"fox_sleep"+_index+".png"),result)
                print("fox_sleep"+_index+".png")
                cv2.imwrite(os.path.join(OUTPUT_DIR+"snow_fox"+_index+".png"),result)
                print("snow_fox"+_index+".png")
                cv2.imwrite(os.path.join(OUTPUT_DIR+"snow_fox_sleep"+_index+".png"),result)
                print("snow_fox_sleep"+_index+".png")
                cv2.imshow("result",result)
                cv2.waitKey(1)
                index+=1
open(OUTPUT_DIR+"fox.properties","w").write(f"texture.1=1-{index-1}")
print(f"write .properties {index-1}")
cv2.destroyAllWindows()

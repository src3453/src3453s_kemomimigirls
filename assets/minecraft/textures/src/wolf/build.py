import os
import cv2
import numpy as np
from tqdm import tqdm

BASE_DIR = r"C:\Users\y2k34\AppData\Roaming\.minecraft\resourcepacks\src3453s_foxgirl\assets\minecraft\textures\src\wolf"
HEADS_DIR = BASE_DIR + r"\heads"
COSTUMES_DIR = BASE_DIR + r"\costumes"
BOTTOMS_DIR = BASE_DIR + r"\bottoms"
SLEEP_DIR = BASE_DIR + r"\sleep"
SPECIAL_DIR = BASE_DIR + r"\special"
OUTPUT_DIR = r"C:\Users\y2k34\AppData\Roaming\.minecraft\resourcepacks\src3453s_foxgirl\assets\minecraft\optifine\random\entity\wolf\\"
OUTPUT_DIR_VANILLA = r"C:\Users\y2k34\AppData\Roaming\.minecraft\resourcepacks\src3453s_foxgirl\assets\minecraft\textures\entity\wolf"

"""colors = {
    "orange":[(0xff,0x9c,0x1e,255)],
    "arctic":[(0xd4,0xe8,0xee,255)],
    "black" :[(0x26,0x1b,0x1b,255)],
    "cherry":[(0xff,0x95,0x95,255)],
    "golden":[(0xff,0xd4,0x8a,255)],
    "brown" :[(0x79,0x34,0x1a,255)],
    "silver":[(0xb9,0xb9,0xb9,255)],
    "lavender":[(0xc5,0x7f,0xeb,255)],
    }"""
mask_colors = [(255,0,255,255)]

heads = os.listdir(HEADS_DIR)
costumes = np.array(os.listdir(COSTUMES_DIR))
bottoms = np.array(os.listdir(BOTTOMS_DIR))
sleeps = os.listdir(SLEEP_DIR)[0:1]
specials = os.listdir(SPECIAL_DIR)


for j,head_name in enumerate(heads):
    index = 1 
    indices1 = (np.linspace(0,39461*(94621.39301*(j+1)),4)%len(costumes)).astype(int)
    indices2 = (np.linspace(0,39023*(14813.59233*(j+1)),4)%len(bottoms)).astype(int)
    for bottoms_name in bottoms[indices2]:
        for costume_name in costumes[indices1]:
            for i,sleep_name in enumerate(sleeps):
                head = cv2.imread(os.path.join(HEADS_DIR,head_name),cv2.IMREAD_UNCHANGED)
                costume = cv2.imread(os.path.join(COSTUMES_DIR,costume_name),cv2.IMREAD_UNCHANGED)
                bottoms_img = cv2.imread(os.path.join(BOTTOMS_DIR,bottoms_name),cv2.IMREAD_UNCHANGED)
                sleep = cv2.imread(os.path.join(SLEEP_DIR,sleep_name),cv2.IMREAD_UNCHANGED)
                special = cv2.imread(os.path.join(SPECIAL_DIR,specials[0]),cv2.IMREAD_UNCHANGED)
                color_name = head_name.split(".")[0]
                costume = costume[:,:,[2,1,0,3]]
                for y in range(costume.shape[0]):
                    for x in range(costume.shape[1]):
                        if all(costume[y,x,:] == mask_colors[0]):
                            costume[y,x,:] = head[16,16,[2,1,0,3]]#colors[color_name][0]
                costume = costume[:,:,[2,1,0,3]]
                result = head
                for y in range(result.shape[0]):
                    for x in range(result.shape[1]):
                        if bottoms_img[y,x,3] != 0:
                            bottoms_img[y,x,3] = 255
                            result[y,x,:] = bottoms_img[y,x,:]
                for y in (range(result.shape[0])):
                    for x in range(result.shape[1]):
                        if index == 16: 
                            if all(special[y,x,:] == mask_colors[0]):
                                special[y,x,:] = head[16,16,[0,1,2,3]]#colors[color_name][0]
                            if all(special[y,x,:] == (0,255,0,255)):
                                result[y,x,:] = (0,0,0,0)
                                special[y,x,:] = (0,0,0,0)
                            if special[y,x,3] != 0:
                                special[y,x,3] = 255
                                result[y,x,:] = special[y,x,:]
                        else:
                            if all(costume[y,x,:] == (0,255,0,255)):
                                result[y,x,:] = (0,0,0,0)
                                costume[y,x,:] = (0,0,0,0)
                            if costume[y,x,3] != 0:
                                costume[y,x,3] = 255
                                result[y,x,:] = costume[y,x,:]
                for y in range(result.shape[0]):
                    for x in range(result.shape[1]):
                        if sleep[y,x,3] != 0:
                            sleep[y,x,3] = 255
                            result[y,x,:] = sleep[y,x,:]
                if index != 1:
                    _index = str(index)
                else:
                    _index = ""
                    cv2.imwrite(os.path.join(OUTPUT_DIR_VANILLA,""+head_name.split(".")[0]+str(_index+".png")),result)
                    cv2.imwrite(os.path.join(OUTPUT_DIR_VANILLA,""+head_name.split(".")[0]+str("_angry"+_index+".png")),result)
                    cv2.imwrite(os.path.join(OUTPUT_DIR_VANILLA,""+head_name.split(".")[0]+str("_tame"+_index+".png")),result)
                cv2.imwrite(os.path.join(OUTPUT_DIR,""+head_name.split(".")[0]+str(_index+".png")),result)
                cv2.imwrite(os.path.join(OUTPUT_DIR,""+head_name.split(".")[0]+str("_angry"+_index+".png")),result)
                cv2.imwrite(os.path.join(OUTPUT_DIR,""+head_name.split(".")[0]+str("_tame"+_index+".png")),result)
                print(""+head_name.split(".")[0]+str(_index+".png")+f" ({head_name:<16}, {costume_name:<24}, {bottoms_name:<24})")
                #cv2.imshow("result",result)
                #cv2.waitKey(1)
                index+=1
#open(OUTPUT_DIR+"fox.properties","w").write(f"texture.1=1-{index-1}")
#print(f"write .properties {index-1}")
cv2.destroyAllWindows()

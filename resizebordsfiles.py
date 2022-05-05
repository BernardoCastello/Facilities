import os
import numpy as np
import cv2

path = f"path"     # path to file with images
for count, filename in enumerate(os.listdir(path)):              
    namefile = path + "\\" + filename                 # exact image
    im = cv2.imread(namefile)

    border = cv2.copyMakeBorder(
    im,
    top=0,             # add pixels on top of the image
    bottom=0,          # add pixels below the image
    left=25,          # add pixels to the left of the image
    right=25,         # add pixels to the right of the image
    borderType=cv2.BORDER_CONSTANT,
    value=[0, 0, 0]             # RGB color
    )

    n = str(count+1).zfill(5)   #rename file name with leading zeros
    cv2.imwrite(f"path.png", border)   # final path to file with images


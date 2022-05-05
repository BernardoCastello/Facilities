import os
import numpy as np
import cv2

for i in range(1):                         
    path = f"initial\\path\\{n}.png"     # path to file with images
    im = cv2.imread(path)


    border = cv2.copyMakeBorder(
    im,
    top=0,             # add pixels on top of the image
    bottom=0,          # add pixels below the image
    left=256,          # add pixels to the left of the image
    right=256,         # add pixels to the right of the image
    borderType=cv2.BORDER_CONSTANT,
    value=[0, 0, 0]             # RGB color
    )
    print(i)

    n = str(i).zfill(5)   #rename file name with leading zeros
    cv2.imwrite(f"final\\path{n}.png", border)   # final path to file with images

from PIL import Image
import cv2
import numpy as np


def QuantizeToGivenPalette(im, palette):
    distance = np.linalg.norm(im[:,:,None] - palette[None,None,:], axis=3)


    palettised = np.argmin(distance, axis=2).astype(np.uint8)

    return palettised

im=cv2.imread("0.png",cv2.IMREAD_COLOR)

inPalette = np.array([
   [0,0,0],             # black
   [0,0,255],           # red
   [0,255,0],           # green
   [255,0,0],           # blue
   [255,255,255]],      # white
   )

r = QuantizeToGivenPalette(im,inPalette)


LUT = np.zeros((5,3),dtype=np.uint8)
LUT[0]=[255,255,255]  # white
LUT[1]=[255,255,0]    # cyan
LUT[2]=[255,0,255]    # magenta
LUT[3]=[0,255,255]    # yellow
LUT[4]=[0,0,0]        # black


result = LUT[r]
cv2.imwrite('0.png', result)

im = Image.open("0.png")
imP = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=10)
imP.putpalette([
    0, 85, 255,
    0, 0, 170, 
    255, 255, 0, 
    0, 0, 255,
    0, 170, 255,
    85, 255, 170,
    255, 85, 0,
    170, 255, 85,
    0, 255, 255,
    255, 170, 0,
    170, 0, 0,
    255, 0, 0,
    0, 0, 0])

im2 = Image.open("0.png")
imP.save('0.png', optimize = 1) 


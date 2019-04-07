import scipy.misc as smisc
import numpy as np
import matplotlib.pylab as plt
import cv2

# image = cv2.imread('ramen.jpg')
# image = smisc.imread('ramen.jpg')
# image = smisc.imread('short-story.jpg')
image = smisc.imread('carabiner.jpg')
mindim = min(image.shape[:2])

image_r = smisc.imresize(image, 0.86)
# image_r = image_r[:,45:255,:]
# image_l = np.zeros((2*image_r.shape[0],2*image_r.shape[1],3))

image_l = np.zeros((426,426,3))
# image_l[:213, 30:243, :] = image

offset = 45
imry, imrx, imch = image_r.shape
image_l[:imry,offset:imrx+offset,:] = image_r

smisc.imsave('carabiner4x.jpg', image_l)


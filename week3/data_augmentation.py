import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow import keras
import random

def Visualize(images, name):
    plt.figure()
    plt.imshow(images)
    plt.title(name)
    
#fix path to your path
path = 'F:/AIschool/data/slytherin.jpg'
img = np.array(Image.open(path))
resize = tf.image.resize(img,(200,250))

#rotate original image (1=90', 2=180' ...)
rotate = tf.image.rot90(img, random.randint(0,4))

#filp left-right / up-down
flip_LR = tf.image.random_flip_left_right(img)
flip_UD = tf.image.random_flip_up_down(img)

#Color Augmentation
hue = tf.image.random_hue(img, 0.5)
saturation = tf.image.random_saturation(img, 0.1, 0.5)
brightness = tf.image.random_brightness(img,0.1)
contrast = tf.image.random_contrast(img, 0.1, 0.5)

#crop
random_crop = tf.image.random_crop(img,(150,250,3))

Visualize(img, 'Origin')
Visualize(resize, 'Resize')
Visualize(rotate, 'Rotate')
Visualize(flip_LR, 'Flip Left-Right')
Visualize(flip_UD, 'Flip Up-Down')
Visualize(hue, 'HUE')
Visualize(saturation, 'SATURATION')
Visualize(brightness, 'BRIGHTNESS')
Visualize(contrast, 'CONTRAST')
Visualize(random_crop, 'Random Crop')

plt.show()
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

def Visualize(image, x, y):
    plt.figure()
    plt.imshow(image.reshape(x,y),cmap='Grays')

#temp 3x3x1
image = np.array([[[[1],[2],[3]],
                   [[4],[5],[6]],
                   [[7],[8],[9]]]], dtype = np.float32)

#temp 2x2x1 kernel to calculate convolution layer 
kernel = np.array([[[[1.]],[[1.]]],
                      [[[1.]],[[1.]]]])

#image shape : (num of image, width, height, channel)
print('Image shape:', image.shape)
#kernel shape : (width, height, channel, num of kernel)
print('Kernel shape:', kernel.shape)

Visualize(image, 3, 3)

kernel_init = tf.constant_initializer(kernel)

conv2d = keras.layers.Conv2D(filters=1, kernel_size=2, padding='VALID', kernel_initializer=kernel_init)(image)
Visualize(conv2d(), 2, 2)
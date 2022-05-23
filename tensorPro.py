import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# print(tf.__version__)
fashion_mnist = tf.keras.datasets.fashion_mnist
dataset = np.array(fashion_mnist)
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
print(len(train_labels))
print(train_images.shape)
print(train_labels)
print(test_images.shape)
# hello
plt.figure()
plt.imshow











from tensorflow.keras.models import load_model
import tensorflow as tf 
from keras.preprocessing.image import load_img, img_to_array 
import cv2
import glob

model = load_model("/home/akugyo/Documents/GitHub/prism/hakunamatata0.h5")
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.summary()

data = "/home/akugyo/Prism/Sample/*"

for images in glob.glob(data):
    img = tf.keras.utils.load_img(images)
    img = img.resize((256, 256))
    img = img_to_array(img) 
    img = img.reshape( -1,256, 256,3)
    y_pred=model.predict(img)
    heh=tf.nn.softmax(y_pred[0])
    if (heh[0] + heh[1] > 0.40):
        print(images)
from tensorflow.keras.models import load_model
import tensorflow as tf 
from keras.preprocessing.image import load_img, img_to_array 
import cv2

model = load_model("/home/akugyo/hakunamatata.h5")
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.summary()
img = tf.keras.utils.load_img("/home/akugyo/Downloads/SharetoStudent/mfhdrinput_20221028171157_1_cam0_ev-2.00_0_4000x3060.jpg")
img = img.resize((256, 256))
img = img_to_array(img) 
img = img.reshape( -1,256, 256,3)
y_pred=model.predict(img)
heh=max(enumerate(y_pred[0]),key=lambda x: x[1])[0]
print(y_pred)
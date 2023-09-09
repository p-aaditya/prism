from tkinter import *
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from tkinter import filedialog
from keras.preprocessing.image import load_img, img_to_array 
import cv2
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras import models
import tensorflow as tf
variable=load_model('hakunamatata.h5')
root = Tk()
root.resizable(width=True, height=True)
dic = {0:"corrupted",1:"partial",2:"no"}
def openfn():
    global filename
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    global img1
    x = openfn()
    img = Image.open(x)
    img = img.resize((256, 256))
    img.save("trial.png")
    img1 = ImageTk.PhotoImage(img)
    panel = Label(root, image=img1)
    panel.image = img1
    panel.pack()
def add_here():
    variable=load_model("D:\\6th SEM\\DIP LAB\\dip_project\\hakunamatata.h5")
    variable.summary()
    img = tf.keras.utils.load_img(filename)
    img = img.resize((256, 256))
    img = img_to_array(img) 
    img = img.reshape( -1,256, 256,3)
    alpha=cv2.imread("trial.png")
    #plt.imshow(alpha)
    print(alpha.shape)
    y_pred=variable.predict(img)
    heh=max(enumerate(y_pred[0]),key=lambda x: x[1])[0]
    message = Label(root,text=y_pred)
    message.pack()
btn = Button(root, text='open image', command=open_img).pack()
btn1 = Button(root, text="predict",command=add_here).pack()
root.mainloop()

import pickle
import os.path

import tkinter.messagebox
from tkinter import *
from tkinter import simpledialog

import PIL
import PIL.Image, PIL.ImageDraw
import PIL
import cv2 as CV
import numpy as np

from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

class DrawingClassifier: 

 def  __init__(self):
    self.class1, self.class2, self.class3 = None, None, None
    self.class1_counter, self.class2_counter, self.class3_counter = None, None, None
    self.clf = None
    self.proj_name = None
    self.root = None
    self.image1 = None

    self.status_label = None
    self.canvas = None
    self.draw = None 


    self.brush_width = 15

    self.classes_prompt()
    self.init_gui


def classes_prompt(self):
    msg =Tk()
    msg.withdraw()

    self.proj_name = simpledialog.askstring("Draw Perdiction")
    if os.path.exsist(self.prod_name):
       with open(f"{self.proj_name}/{self.proj_name}_data.pickel", "rb") as f:
        data = pickle.load(f)
        self.class1 = data['c1']
        self.class2 = data['c2']
        self.class3 = data['c3']
        self.class1_counter = data['c1c']
        self.class2_counter = data['c2c']
        self.class3_counter = data['c3c']
        self.clif = data['clf']
        self.proj_name = data['pname']
    else:
      self.class1 = simpledialog.askstring("Class 1"," What is the first class called", parent=msg)
      self.class2 = simpledialog.askstring("Class 2"," What is the second class called", parent=msg)
      self.class3 = simpledialog.askstring("Class 3"," What is the third class called", parent=msg)

    self.class1_counter = 1
    self.class2_counter = 1
    self.class3_counter = 1

    self.clf = LinearSVC()

    os.mkdir(self.proj_name)
    os.chdir(self.proj_name)
    os.mkdir(self.class1)
    os.mkdir(self.class2)
    os.mkdir(self.class3) 
    os.chdir("..")

def init_gut(self):
    WIDTH = 500
    HEIGHT = 500
    WHITE = (255, 255, 255)

    self.root = Tk()
    self.root.title(f"NuturalNine Drawing Classifier Alpha v0.2 - {self.proj_name}") 

    self.canvas = Canvas(self.root, width=WIDTH-10, height=HEIGHT-10, bg="white")
    self.canvas.pack(expand=YES, fill=BOTH)
    self.canvas.bind("<B1-Motion", self.paint)
    
    self.image1 = PIL.Image.new("RGB", (WIDTH, HEIGHT), WHITE)
    self.draw = PIL.ImageDraw.Draw(self.image1)

    btn_frame = tkinter.Frame(self.root)
    btn_frame.pack(fill=X, side=BOTTOM)
    

def paint(self, event):
   pass
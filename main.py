#%%

import tkinter as tk
import os
from datetime import datetime
root=tk.Tk()
root.configure(background="white")
path1 = os.path.dirname(os.path.realpath(__file__))
def image_capture():
     os.chdir(path1)
     os.system("python imageCapture.py")

def recognize():
    os.chdir(path1)
    os.system("python recognize.py")

def attendance():
    os.chdir(path1+"/"+ "attendance sheet")
    os.startfile(os.getcwd()+'\\'+str(str(datetime.now().month)+'.xlsx'))   
def register():
    os.chdir(path1)
    os.system("python NewImageGenrator.py")      
def train():
    os.chdir(path1)
    os.system("python train.py")
root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")
tk.Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky='N'+'E'+'W'+'S',padx=5,pady=5)
tk.Button(root,text="Register",font=("times new roman",20),bg="#0D47A1",fg='white',command=register).grid(row=6,columnspan=2,sticky='W'+'E'+'N'+'S',padx=5,pady=5)
tk.Button(root,text="Train Model",font=("times new roman",20),bg="#0D47A1",fg='white',command=train).grid(row=9,columnspan=2,sticky='W'+'E'+'N'+'S',padx=5,pady=5)
tk.Button(root,text="Image Capture",font=("times new roman",20),bg="#0D47A1",fg='white',command=image_capture).grid(row=12,columnspan=2,sticky='W'+'E'+'N'+'S',padx=5,pady=5)
tk.Button(root,text="Recognize",font=("times new roman",20),bg="#0D47A1",fg='white',command=recognize).grid(row=15,columnspan=2,sticky='W'+'E'+'N'+'S',padx=5,pady=5)
tk.Button(root,text="Attendance Sheet Of Present Month",font=("times new roman",20),bg="#0D47A1",fg='white',command=attendance).grid(row=18,columnspan=2,sticky='W'+'E'+'N'+'S',padx=5,pady=5)
root.mainloop()

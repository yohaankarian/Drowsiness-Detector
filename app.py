from pathlib import Path
import tkinter as tk
import customtkinter as ctk
import torch
import numpy as np

import cv2
from PIL import Image, ImageTk
import vlc

app = tk.Tk() #initialising the tkinter GUI applicaton
app.geometry("600x600") #specifying the geometry of the window
app.title("Drowsiness Detector")
ctk.set_appearance_mode("dark") #Using custom tkinter

vidFrame = tk.Frame(height = 480, width = 600) #Specifying the frame size of the video frame in the tkinter window
vidFrame.pack()
vid = ctk.CTkLabel(vidFrame)
vid.pack()
counter = 0 #intialising the counter for the drowsiness detector
counterLabel = ctk.CTkLabel(text = counter , height=40, width=120, text_font=("Arial",20),text_color = "white",fg_color = "teal") #Using custom tkinter to create a Label which updates the value of the counter as it increases
counterLabel.pack(pady=10)

def reset_counter(): #function to reset the counter
    global counter
    counter = 0
resetButton = ctk.CTkButton(text = "Reset Counter" , command = reset_counter , height=40, width=120, text_font=("Arial",20),text_color = "white",fg_color = "teal") #initialising the button to reset the counter variable
resetButton.pack()
model = torch.hub.load('ultralytics/yolov5','custom', path ='models/last.pt',force_reload = True) 

cap = cv2.VideoCapture(0) #Capturing the video input from camera number 0 i.e the main camera of the given system

def detect(): #function for detection
    global counter
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame) #passing the image frames to the model
    img = np.squeeze(results.render()) 

    if len(results.xywh[0]) > 0: #Storing the results from the 3D arrays to the variables dconf and dclass
        dconf = results.xywh[0][0][4]
        dclass = results.xywh[0][0][5]

        if dconf.item()  > 0.5 and dclass.item() == 1.0: #Block of code for exectution of the drowsiness detection, if the value is above 0.85 and if a face is detected, audio will play with the intention of waking up the drowsy person
            p = vlc.MediaPlayer(f"file:///1.wav")#selecting the audio file to play when the condition is satisfied
            p.play()
            counter += 1  #incrementing the counter when the condition is satisfied
    #for running the webcam within the object
    imgarr = Image.fromarray(img) #rendering webcam images
    imgtk = ImageTk.PhotoImage(imgarr) 
    vid.imgtk = imgtk
    vid.configure(image=imgtk)
    vid.after(10,detect)#looping within itself
    counterLabel.configure(text=counter)

detect() #running the detect funtion
app.mainloop() #running the tkinter GUI application
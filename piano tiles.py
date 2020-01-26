'''
This project uses mouse to play piano tiles automatically.
go to this website to start piano tiles
https://www.silvergames.com/en/piano-tiles
and set scaling to 80%
firstly keep mouse position to the left of the screen and run the program.
then switch to the website of piano tiles and move the move the mouse to start position 
and click the start button
'''
import cv2
from PIL import ImageGrab
import time
from pynput.mouse import Button,Controller
import numpy as np
from pynput.keyboard import Key,Listener
mouse = Controller()
keyboard = Listener()
time.sleep(2)

while mouse.position[0]<400 :
    1

while mouse.position[0]>350 :
    s = cv2.cvtColor(np.array(ImageGrab.grab()), cv2.COLOR_BGR2GRAY)
    for i in {550,650,800,900}:
        for j in {687}:
            if(s[j,i]<50):
                mouse.move(i/1.25-mouse.position[0],j/1.25-mouse.position[1])
                mouse.click(Button.left,1)
print('exit')
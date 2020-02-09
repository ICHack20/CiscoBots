import cv2 
import numpy as np
from PIL import Image

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
frame_counter = 0
frames = []

while ret==True and frame_counter <5:
    ret, frame = cap.read()
    frame_counter += 1
    cv2.imshow('b', frame)
    frames.append(frame)
    k = cv2.waitKey(30) & 0xFF
    if k==27:
        break

avg_img = np.zeros(shape=[480, 640, 3], dtype=np.uint8)

for i in range(len(frames)):
    avg_img = avg_img + frames[2]

#avg_img = avg_img/(len(frames)-1)

cv2.imwrite('H:\\ICHack\\avg_img.jpg', avg_img)
cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
ret, frame = cap.read()


while ret== True:
    ret, frame = cap.read()
    for a in range(3):
        for i in range(480):
            for j in range(640):
                if frame[i,j,a] > 100:
                    frame[i,j,a] = frame[i,j,a] + 50
                    
    img_sub = frame - avg_img
    obj_1, th1 = cv2.threshold(img_sub[:,:,1], 150, 255, cv2.THRESH_BINARY)
    obj_2, th2 = cv2.threshold(img_sub[:,:,2], 150, 255, cv2.THRESH_BINARY)
  
    cv2.imshow('c', th1)
    cv2.imshow('f', th2)
    k = cv2.waitKey(30) & 0xFF1
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()

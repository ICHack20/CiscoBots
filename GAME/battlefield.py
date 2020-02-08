import numpy as np
import cv2

field_w = 500 #height and wifth of the battlefield
field_h = 500

framein = np.zeros((field_w, field_h, 3), dtype="uint8")
cv2.imshow('try', framein)

# Set the border of the field
corner_pointer = 0
boundary_corners = [(0, 0),(0, 0)]
set_boundary = True

def define_corners(event, x, y, flags, userdata):
    global corner_pointer
    global first_point
    if (event == cv2.EVENT_LBUTTONDOWN and corner_pointer != 5):
        boundary_corners[corner_pointer] = (x, y)
        if (corner_pointer == 0):
            first_point = (x, y)
            print(first_point)
        corner_pointer = corner_pointer + 1

        if (corner_pointer%2 == 0):
            draw_lines(boundary_corners[0], boundary_corners[1])
            boundary_corners[0] = boundary_corners[1]
            corner_pointer = 1

    if (event == cv2.EVENT_RBUTTONDOWN):
        boundary_corners[corner_pointer] = first_point
        draw_lines(boundary_corners[0], boundary_corners[1])
        corner_pointer = 5
        border_set_done()

    
def draw_lines(corners1, corners2):
    cv2.line(framein, corners1, corners2, (255, 0, 0), 3)
    cv2.imshow('try', framein)

def border_set_done():
    set_boundary = False

#while (True):
    #cv2.imshow('try', framein)
cv2.setMouseCallback('try', define_corners)
    #if (set_boundary == False):
        #break
while (True):
    cv2.imshow('try', framein)
    if (set_boundary == False):
        break

#Get the pixels of the border
print('dai dai che ce la si fa')
border_px = np.where(framein == (255, 0, 0))








cv2.waitKey(0)
cv2.destroyAllWindows()

class boundary:
    def __init__(self, image):
        self.border = np.where(image == (255, 0, 0))


#class bot:

import numpy as np
import cv2

field_w = 500 #height and wifth of the battlefield
field_h = 500
framein = np.zeros((field_w, field_h, 3), dtype="uint8")
#cv2.line(framein, (100, 100), (90, 90), (255, 0, 0), 3)

corner_pointer = 0
boundary_corners = [(0, 0),(0, 0)]
corner_pointer = 0
#cv2.rectangle(iminput, boundary_corners[0], boundary_corners[1], (255, 0, 0), 5)
#cv2.polylines(framein, [boundary_corners], True, (255, 0, 0), 3)

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

    
def draw_lines(corners1, corners2):
    cv2.line(framein, corners1, corners2, (255, 0, 0), 3)
    cv2.imshow('try', framein)

cv2.imshow('try', framein)
cv2.setMouseCallback('try', define_corners)

cv2.waitKey(0)
cv2.destroyAllWindows()

# class boundary:
#     def __init__(self, corner_coordintes):
#         self.corners = corner_coordintes

#     def create_rectangle(self):
#         cv2.rectangle(img, self.corners[0], self.corners[1], (255, 0, 0), 5)

#class bot:

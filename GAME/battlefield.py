import numpy as np
import cv2

class Arena:
    def __init__(self, image):
        self.corner_pointer = 0
        self.boundary_corners = [(0, 0),(0, 0)]
        self.first_point = (0, 0)
        self.set_boundary = True
        self.image = image

    def define_corners(self, event, x, y, flags, userdata):
        if (event == cv2.EVENT_LBUTTONDOWN and self.corner_pointer != 5):
            self.boundary_corners[self.corner_pointer] = (x, y)
            if (self.corner_pointer == 0):
                self.first_point = (x, y)
                print(self.first_point)
            self.corner_pointer = self.corner_pointer + 1

            if (self.corner_pointer%2 == 0):
                self.draw_lines(self.boundary_corners[0], self.boundary_corners[1])
                self.boundary_corners[0] = self.boundary_corners[1]
                self.corner_pointer = 1

        if (event == cv2.EVENT_RBUTTONDOWN):
            self.boundary_corners[self.corner_pointer] = self.first_point
            self.draw_lines(self.boundary_corners[0], self.boundary_corners[1])
            self.corner_pointer = 5
            self.border_set_done()
        
        return self.border_set_done

        
    def draw_lines(self, corners1, corners2):
        cv2.line(self.image, corners1, corners2, (255, 0, 0), 3)
        cv2.imshow('try', framein)

    def border_set_done(self):
        print('in')
        self.set_boundary = False

    def show(self):
        cv2.imshow('try', self.image)
    
    def set_borders(self):
        while(self.set_boundary):
            cv2.setMouseCallback('try', self.define_corners)
            cv2.waitKey(1)


field_w = 500 #height and wifth of the battlefield
field_h = 500

framein = np.zeros((field_w, field_h, 3), dtype="uint8")
cv2.imshow('try', framein)

arena = Arena(framein)
arena.set_borders()

#Get the pixels of the border
print("out of the loop")
border_px = np.where(framein == (255, 0, 0))
print(len(border_px))
print(border_px[0])
print(border_px[0])
print(border_px[0])



cv2.waitKey(0)
cv2.destroyAllWindows()

class boundary:
    value = (255, 0, 0)

#class bot1:



#class bot:
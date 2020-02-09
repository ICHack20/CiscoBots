import numpy as np
import cv2
import argparse
import time

class Arena:
    def __init__(self, image):
        self.corner_pointer = 0
        self.boundary_corners = [(0, 0),(0, 0)]
        self.first_point = (0, 0)
        self.set_boundary = True
        self.image = image
        
    def set_frame(self, image):
        self.image = image

    def define_corners(self, event, x, y, flags, userdata):
        if (event == cv2.EVENT_LBUTTONDOWN and self.corner_pointer != 5):
            self.boundary_corners[self.corner_pointer] = (x, y)
            if (self.corner_pointer == 0):
                self.first_point = (x, y)
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
        cv2.line(self.image, corners1, corners2, (255, 0, 0), 2)
        cv2.imshow('try', self.image)

    def border_set_done(self):
        self.set_boundary = False

    def show(self):
        cv2.imshow('try', self.image)
    
    def set_borders(self):
        cv2.setMouseCallback('try', self.define_corners)



# construct the argument parser and parse the arguments
def get_trackers(ret, frame):
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", type=str,
        help="path to input video file")
    ap.add_argument("-t", "--tracker", type=str, default="kcf",
        help="OpenCV object tracker type")
    args = vars(ap.parse_args())

    # initialize a dictionary that maps strings to their corresponding
    # OpenCV object tracker implementations
    OPENCV_OBJECT_TRACKERS = {
        "csrt": cv2.TrackerCSRT_create,
        "kcf": cv2.TrackerKCF_create,
        "boosting": cv2.TrackerBoosting_create,
        "mil": cv2.TrackerMIL_create,
        "tld": cv2.TrackerTLD_create,
        "medianflow": cv2.TrackerMedianFlow_create,
        "mosse": cv2.TrackerMOSSE_create
    }
    # initialize OpenCV's special multi-object tracker
    trackers = cv2.MultiTracker_create()
    
    obj_locations = []

    # loop over frames from the video stream
    
    ret, frame = vs.read()
    frame = frame[1] if args.get("video", False) else frame
    
    # check to see if we have reached the end of the stream
    if frame is None:
        return 0
    # grab the updated bounding box coordinates (if any) for each
    # object that is being tracked
    (success, boxes) = trackers.update(frame)

    # loop over the bounding boxes and draw then on the frame
    colors = [((0, 255, 0)), (255, 0, 0)]
    col_str = ['g','b']
    for i, box in enumerate(boxes):
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), colors[i], 2)
        obj_locations.append([(x, y), (x + w, y + h), col_str[i]])
    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the 's' key is selected, we are going to "select" a bounding
    # box to track
    if key == ord("s"):
        # select the bounding box of the object we want to track (make
        # sure you press ENTER or SPACE after selecting the ROI)
        box = cv2.selectROI("Frame", frame, fromCenter=False,
                showCrosshair=True)

        # create a new object tracker for the bounding box and add it
        # to our multi-object tracker
        tracker = OPENCV_OBJECT_TRACKERS[args["tracker"]]()
        trackers.add(tracker, frame, box)
        #
    # if the `q` key was pressed, break from the loop
    elif key == ord("q"):
        return 0

    # if we are using a webcam, release the pointer
    if not args.get("video", False):
        vs.release()

    # otherwise, release the file pointer
    else:
        vs.release()

    # close all windows
    cv2.destroyAllWindows()

    return obj_locations

vs = cv2.VideoCapture(0)
ret, frame = vs.read()
cv2.imshow("try", frame)
print("lala land")

arena = Arena(frame)
while(arena.set_boundary):
    ret, frame = vs.read()
    arena.set_frame(frame)
    arena.set_borders()
    cv2.waitKey(1)


while ret:
    ret, frame = vs.read()
    obj_locations = get_trackers(ret, frame)
    if obj_locations == 0:
        break
    print(obj_locations)

#Get the pixels of the border
print(frame[arena.first_point[1], arena.first_point[0], :])

# cv2.line(anatra, (100, 100), (100, 103), (255, 0, 0), 2)


print("out of the loop")
border_px = np.where(np.all(frame == (255, 0, 0), -1))
# border_px = np.reshape(border_px, (len(border_px[0]),3))
# print(len(border_px))
# print(border_px[0])
# print(border_px[0])



cv2.waitKey(0)
cv2.destroyAllWindows()

class boundary:
    value = (255, 0, 0) 
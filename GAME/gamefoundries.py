import argparse
import numpy as np
import cv2
import time

class Arena:
    def __init__(self, image, frame_name):
        self.corner_pointer = 0
        self.boundary_corners = [(0, 0),(0, 0)]
        self.first_point = (0, 0)
        self.corners = []
        self.set_boundary = True
        self.image = image
        self.frame_name = frame_name

    def define_corners(self, event, x, y, flags, userdata):
        if (event == cv2.EVENT_LBUTTONDOWN and self.corner_pointer != 5):
            self.boundary_corners[self.corner_pointer] = (x, y)
            if (self.corner_pointer == 0):
                self.first_point = (x, y)
            self.corners.append((x, y))
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
        cv2.imshow(self.frame_name, self.image)

    def border_set_done(self):
        self.set_boundary = False
    
    def set_borders(self):
        while(self.set_boundary):
            cv2.setMouseCallback(self.frame_name, self.define_corners)
            cv2.waitKey(1)
    
    def get_corners(self):
        return self.corners
    
    # def set_borders(self):
    #     cv2.setMouseCallback('try', self.define_corners)
    
    def get_border_boolean(self):
        return self.set_boundary

# construct the argument parser and parse the arguments
def get_trackers(vs, frame_name, corners):
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

    ret, frame = vs.read()
    
    obj_locations = []

    # loop over frames from the video stream
    while ret:
        ret, frame = vs.read()
        frame = frame[1] if args.get(frame_name, False) else frame
        
        # check to see if we have reached the end of the stream
        if frame is None:
            break
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
        cv2.polylines(frame, [corners], (255,0,0), 2)
        cv2.imshow(frame_name, frame)
        key = cv2.waitKey(1) & 0xFF

        # if the 's' key is selected, we are going to "select" a bounding
        # box to track
        if key == ord("s"):
            # select the bounding box of the object we want to track (make
            # sure you press ENTER or SPACE after selecting the ROI)
            box = cv2.selectROI(frame_name, frame, fromCenter=False,
                    showCrosshair=True)

            # create a new object tracker for the bounding box and add it
            # to our multi-object tracker
            tracker = OPENCV_OBJECT_TRACKERS[args["tracker"]]()
            trackers.add(tracker, frame, box)
            #
        # if the `q` key was pressed, break from the loop
        elif key == ord("q"):
            break

    # if we are using a webcam, release the pointer
    if not args.get(frame_name, False):
        vs.release()

    # otherwise, release the file pointer
    else:
        vs.release()

    # close all windows
    cv2.destroyAllWindows()

    return obj_locations

frame_name = "try"
vs = cv2.VideoCapture(0)
ret, frame = vs.read()
while (ret):
    ret, frame = vs.read()
    cv2.imshow(frame_name, frame)
    k = cv2.waitKey(1)
    if k==102:
        break

print("lala land")

arena = Arena(frame, frame_name)
arena.set_borders()

# arena = Arena(frame)
# cv2.setMouseCallback('try', arena.define_corners)
# while(arena.get_border_boolean and ret):
#     ret, frame = vs.read()
#     arena.set_frame(frame)
#     arena.set_borders()
#     cv2.waitKey(1)

#Get the pixels of the border
corners = np.asarray(arena.get_corners())
border_px = np.where(np.all(frame == (255, 0, 0), -1))

obj_locations = get_trackers(vs, frame_name, corners)
print(obj_locations)

# while ret:
#     ret, frame = vs.read()
#     obj_locations = get_trackers(ret, frame)
#     if obj_locations == 0:
#         break
#     print(obj_locations)




cv2.waitKey(0)
cv2.destroyAllWindows()

class boundary:
    value = (255, 0, 0) 
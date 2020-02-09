# USAGE
# python multi_object_tracking.py --video videos/soccer_01.mp4 --tracker csrt

# import the necessary packages
import argparse
import time
import cv2
import numpy as np

# construct the argument parser and parse the arguments
def get_trackers():
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
    obj_location = []
    col_str = ['g','b']
    j = 0
    # initialize OpenCV's special multi-object tracker
    trackers = cv2.MultiTracker_create()

    vs = cv2.VideoCapture(0)
    ret, frame = vs.read()
    
    obj_locations = []

    # loop over frames from the video stream
    while ret:
        ret, frame = vs.read()
        frame = frame[1] if args.get("video", False) else frame
        
        # check to see if we have reached the end of the stream
        if frame is None:
            break
        # grab the updated bounding box coordinates (if any) for each
        # object that is being tracked
        (success, boxes) = trackers.update(frame)
        obj_location.append((boxes,col_str[0:j]))
        
        #print(success,boxes)
        
        # loop over the bounding boxes and draw then on the frame
        colors = [((0, 255, 0)), (255, 0, 0)]
        #col_str = ['g','b']
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
            j+=1

        # if the `q` key was pressed, break from the loop
        elif key == ord("q"):
            break
        
    # if we are using a webcam, release the pointer
    if not args.get("video", False):
        vs.release()

    # otherwise, release the file pointer
    else:
        vs.release()

    # close all windows
    cv2.destroyAllWindows()

    return obj_location
    
boxes = get_trackers()
boxes = np.asarray(boxes)
print(boxes[-1])

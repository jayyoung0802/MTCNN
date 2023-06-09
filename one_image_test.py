#coding:utf-8
import sys
import argparse
from training.mtcnn_model import P_Net, R_Net, O_Net
from tools.loader import TestLoader
from detection.detector import Detector
from detection.fcn_detector import FcnDetector
from detection.MtcnnDetector import MtcnnDetector
import cv2
import os
import numpy as np 


test_mode = "ONet"
thresh = [0.1, 0.15, 0.6]
min_face_size = 24
stride = 2
detectors = [None, None, None]
prefix = ['./tmp/model/pnet/pnet', './tmp/model/rnet/rnet', './tmp/model/onet/onet']
epoch = [30, 30, 2]
batch_size = [2048, 64, 16]
model_path = ['%s-%s' % (x, y) for x, y in zip(prefix, epoch)]


PNet = FcnDetector(P_Net, model_path[0])
detectors[0] = PNet

# load rnet model
if test_mode in ["RNet", "ONet"]:
    RNet = Detector(R_Net, 24, batch_size[1], model_path[1])
    detectors[1] = RNet

# load onet model
if test_mode == "ONet":
    ONet = Detector(O_Net, 48, batch_size[2], model_path[2])
    detectors[2] = ONet

mtcnn_detector = MtcnnDetector(detectors=detectors, min_face_size=min_face_size,
                               stride=stride, threshold=thresh)

test="./test.jpg"
im = cv2.imread(test)
all_boxes,landmarks = mtcnn_detector.detect_one_image(im)

print(all_boxes)
print(landmarks)
count = 0
image = cv2.imread(test)
for bbox in all_boxes[count]:
    cv2.putText(image,str(np.round(bbox[4],2)),(int(bbox[0]),int(bbox[1])),cv2.FONT_HERSHEY_TRIPLEX,1,color=(255,0,255))
    cv2.rectangle(image, (int(bbox[0]),int(bbox[1])),(int(bbox[2]),int(bbox[3])),(0,0,255))
    for landmark in landmarks[count]:
        for i in range(len(landmark)//2):
            cv2.circle(image, (int(landmark[2*i]),int(int(landmark[2*i+1]))), 3, (0,0,255))
# cv2.imshow("test",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imwrite('test-1.png',image)

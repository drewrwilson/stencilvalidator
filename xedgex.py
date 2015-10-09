#!/usr/bin/env python

'''
This sample demonstrates Canny edge detection.
Usage:
  edge.py [<video source>]
  Trackbars control edge thresholds.
'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2

import numpy

# relative module
# import video

# built-in module
import sys


if __name__ == '__main__':
    print(__doc__)

    try:
        fn = sys.argv[1]
    except:
        fn = 0

    def nothing(*arg):
        pass

    cv2.namedWindow('edge')
    cv2.createTrackbar('thrs1', 'edge', 2000, 5000, nothing)
    cv2.createTrackbar('thrs2', 'edge', 4000, 5000, nothing)

    # cap = video.create_capture(fn)
    while True:
        # flag, img = cap.read()
        img  = cv2.imread('test-stencils/invalid-black-lives-matter-stencil.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thrs1 = cv2.getTrackbarPos('thrs1', 'edge')
        thrs2 = cv2.getTrackbarPos('thrs2', 'edge')
        print(thrs1) #2000
        print(thrs2) #4000
        edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)

        contours, heirarchy = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        print(len(contours))
        red = numpy.array([255,0,0])
        vis = img.copy()
        cv2.drawContours(vis, contours, -1, red, 2)

        # one line of code that has number of edge2sf
        # vis /= 2
        # vis[edge != 0] = (0, 255, 0)
        cv2.imshow('edge', vis)
        ch = cv2.waitKey(5) & 0xFF
        if ch == 27:
            break
    cv2.destroyAllWindows()

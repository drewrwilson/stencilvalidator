#! /usr/bin/env python

import sys
import cv2

sys.argv.pop(0)

for arg in sys.argv:
  print 'Looking at "' + arg + '".'
  
  image = cv2.imread(arg)
  image = cv2.bitwise_not(image)
  detector = cv2.SimpleBlobDetector()
  blobs = detector.detect(image)
  number_of_blobs = len(blobs)
  valid = number_of_blobs == 0

  print str(valid)
  print 'Found ' + str(number_of_blobs) + ' blobs.'
  print '\n'

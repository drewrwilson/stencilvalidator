import cv2

class StencilValidator:

  def __init__(self, path):
    self.path = path

  def image(self):
    cv2.imread(self.path)
 
  def inverted_image(self):
    cv2.bitwise_not(self.image)
  
  def detector(self):
    cv2.SimpleBlobDetector()
  
  def number_of_blobs(self):
    len(self.detector.detect(self.image))    

  def valid(self):
    return self.number_of_blobs == 0   # we don't yet know if this is the correct, may need to update this later

import cv2
import time
import os

label = "A"
if not os.path.exists(directory):
  os.makedirs(directory)
vidcap = cv2.VideoCapture(0)

vidcap.set(CV_CAP_PROP_FRAME_WIDTH,640);
vidcap.set(CV_CAP_PROP_FRAME_HEIGHT,480);

success,image = vidcap.read()
count = 0
success = True
while count < 100:
  success,image = vidcap.read() 
  cv2.imwrite(label +"/"+label+"%d.jpg" % count, image)  # save as JPG file  
  print("CAPTURED: "+label+"%d.jpg", %count)
  count += 1
  time.sleep(5)

import numpy as np
import cv2
#from matplotlib import pyplot as plt

img = cv2.imread('a.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(corners)

for i in corners:
    print(corners)
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
cv2.imshow("a",img)
cv2.waitKey(0)
#plt.imshow(img),plt.show()
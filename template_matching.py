
import cv2
import numpy as np
count=[0 ,0 ,0,0]
threshold=[0.9,0.9,0.85,0.9]
img_bgr= cv2.imread('myphoto.png')
img_gray=cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

#template=cv2.imread('template3.png',cv2.IMREAD_GRAYSCALE)
#w,h=template.shape[::-1]
templates = [ cv2.imread('template'+str(i)+'.png',cv2.IMREAD_GRAYSCALE) for i in range(1,5) ]
w1,h1=templates[0].shape[::-1]
w2,h2=templates[1].shape[::-1]
w3,h3=templates[2].shape[::-1]
w4,h4=templates[3].shape[::-1]

result1=cv2.matchTemplate(img_gray,templates[0],cv2.TM_CCOEFF_NORMED)
result2=cv2.matchTemplate(img_gray,templates[1],cv2.TM_CCOEFF_NORMED)
result3=cv2.matchTemplate(img_gray,templates[2],cv2.TM_CCOEFF_NORMED)
result4=cv2.matchTemplate(img_gray,templates[3],cv2.TM_CCOEFF_NORMED)

loc1=np.where(result1>=threshold[0])
loc2=np.where(result2>=threshold[1])
loc3=np.where(result3>=threshold[2])
loc4=np.where(result4>=threshold[3])

for pt1 in zip(*loc1[::-1]):
    cv2.rectangle(img_bgr,pt1,(pt1[0]+w1,pt1[1]+h1),(0,255,0),2)
    count[0]=count[0]+1
for pt2 in zip(*loc2[::-1]):
    cv2.rectangle(img_bgr,pt2,(pt2[0]+w2,pt2[1]+h2),(255,0,0),2)
    count[1]=count[1]+1
for pt3 in zip(*loc3[::-1]):
    cv2.rectangle(img_bgr,pt3,(pt3[0]+w3,pt3[1]+h3),(0,0,255),2)
    count[2]=count[2]+1
for pt4 in zip(*loc4[::-1]):
    cv2.rectangle(img_bgr,pt4,(pt4[0]+w3,pt4[1]+h3),(0,0,255),2)
    count[3]=count[3]+1



print "Circle"
print count[0]
print "Square"
print count[1]
print "Star"
print count[2]
print "Triangle"
print count[3]

cv2.imshow("image",img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2,time
video = cv2.VideoCapture(0)
a=1
while True:
    a=a+1
    check,frame = video.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(frame)
    cv2.imshow("capture",frame)
    key = cv2.waitKey(1)
    if key ==ord('a'):
        break
print(a)
video.release()
cv2.destroyAllWindows()

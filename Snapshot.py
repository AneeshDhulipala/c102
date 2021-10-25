import cv2
def takeSnapshot():
    obj=cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=obj.read()
        cv2.imwrite('Snapshot1.jpg',frame)
        result = False
    obj.release()
    cv2.destroyAllWindows()
takeSnapshot()

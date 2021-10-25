import cv2
import dropbox
import time 
import random
startTime = time.time()
def takeSnapshot():
    number = random.randint(0,100)
    obj=cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=obj.read()
        imageName='img'+str(number)+'.png'
        cv2.imwrite(imageName,frame)
        result = False
        startTime=time.time
    return imageName
    print('snapshot Taken')
    obj.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token = "sl.A7Avy2uZwJZnb0WMHczxLhfTARZRWDM7YFVExyioI4aYXvCsQjOigcpabA8-uwd8rTNKssXjYEcyBmjaKt27jFKgN7bwu86YGZdekSKMWtO2G4Jz2_nCzhuvph-wABmet94u-WQ"
    file =img_name
    file_from = file
    file_to="/test_dropbox/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - startTime) >= 5):
            name = takeSnapshot()
            upload_file(name)

main()
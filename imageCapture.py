import os
import cv2 as cv

pic_no=0	
print("Enter name for directory")
path1=os.path.dirname(os.path.realpath(__file__))
os.chdir(path1)
file=input()
fa=cv.CascadeClassifier('hfd.xml')
path=rdir_path = os.path.dirname(os.path.realpath(__file__))+"/output"
os.chdir(path)
os.makedirs(file)
cam=cv.VideoCapture(0)
ret,frame=cam.read()  
while ret:
            ret,frame=cam.read() 
            gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
            faces=fa.detectMultiScale(gray,1.3,3)
            cv.imshow("live",frame)
            for (x,y,w,h) in faces:
                pic_no=pic_no+1
                cv.rectangle(frame, (x, y), (x + w, y + h), (255,0, 0), 2)
                roi_color = frame[y:y + h, x:x + w]
                print(" Object found. Saving locally.\n")    
                cv.imwrite(file+'/'+str(pic_no)+ '.jpg', roi_color)
                if(cv.waitKey()==27):
                    break
            if cv.waitKey(10001)==27:
                    break
        
frame=cv.flip(frame,1)
cv.destroyAllWindows()
cam.release()

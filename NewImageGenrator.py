from keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array
import cv2 as cv
import os

pic_no=0
path=os.path.dirname(os.path.realpath(__file__))
path1=os.path.dirname(os.path.realpath(__file__))+"\students"
os.chdir(path)
print("Enter your name")
file=input()
fa=cv.CascadeClassifier('hfd.xml')
os.chdir(path1)
os.makedirs(file)
cam=cv.VideoCapture(0)
ret,frame=cam.read()    
while ret:
            ret,frame=cam.read() 
            gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
            faces=fa.detectMultiScale(gray,1.3,3)
            cv.imshow("live",frame)
            if(pic_no==16):
                break
            for (x,y,w,h) in faces:
                cv.rectangle(frame, (x, y), (x + w, y + h), (0,0, 0), 2)
                roi_color = frame[y:y + h, x:x + w]
                print("[INFO] Object found. Saving locally.\n")    
                cv.imwrite(file+'/'+'x'+str(pic_no+1)+ '.jpg', roi_color)
                pic_no=pic_no+1
                if cv.waitKey(100)==27:
                    break
            
frame=cv.flip(frame,1)
cv.destroyAllWindows()
cam.release()
datagen=ImageDataGenerator(
        rotation_range=40,
        width_shift_range=.2,
       height_shift_range=.2,
       rescale=1./255,
       shear_range=.2,
       zoom_range=.2,
       horizontal_flip=True,
       fill_mode='nearest'
        )
img=load_img(path1+'/' + file+'/'+'x1.jpg')
x=img_to_array(img)
x=x.reshape((1,)+x.shape)
i=0
for batch in datagen.flow(x,batch_size=1,save_to_dir=(path1+'/' + file),save_prefix=(i),save_format='jpg') :
    i+=1
    if i>100:
        break
k=1
path3=os.path.dirname(os.path.realpath(__file__))+'/'+file+'/'
for filename in os.listdir(path3):
    dst='('+str(k)+')'+".jpg"
    src=path3+filename
    dst=path3+dst
    os.rename(src,dst)    
    k+=1
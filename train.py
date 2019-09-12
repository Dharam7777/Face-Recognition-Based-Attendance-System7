from keras.models import Sequential
from keras.layers import Flatten,Dense,Activation,BatchNormalization,Dropout
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.constraints import maxnorm
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import os
import cv2 as cv
import numpy as np
x_data=[] #features
y_data=[]   #labels
seed=77
    
model=Sequential()

fp = os.path.dirname(os.path.realpath(__file__))
os.chdir(fp)     
students=os.listdir('students')
num_classes=len(students)
for label in students:  
        for i in os.listdir('students/'+label):
    				  img=cv.imread('students'+'/'+label+'/'+i,1)
    				  print(img)
    				  img=cv.resize(img,(32,32))
    				  img=img.astype('float')/255.0
    				  img=np.expand_dims(img,axis=0)  				
    				  x_data.append(img)
    				  y_data.append((label))
    				 
label_encode=LabelEncoder()
y_data=label_encode.fit_transform(y_data)            
x_data=np.array(x_data,dtype='float') 
#print(x_data.shape ) # shape of x is (400, 1, 160, 160, 3)
y_data=np.array(y_data,dtype='float')
y_data=np.reshape(y_data,(len(y_data),1) )
x_data=np.reshape(x_data,(len(x_data),32,32,3))
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.2,random_state=77)

y_train=np_utils.to_categorical(y_train)
y_test=np_utils.to_categorical(y_test)

model.add(Conv2D(32 , (3, 3), input_shape=(32,32,3), activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))
model.add(BatchNormalization())
	 
model.add(Conv2D(128, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Flatten())
model.add(Dropout(0.2))

model.add(Dense(128, kernel_constraint=maxnorm(3)))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Dense(num_classes))
model.add(Activation('softmax'))

epochs =50
optimizer = 'adam'
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])    
np.random.seed(seed)
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=epochs, batch_size=20)
#print(x_train[0])
os.chdir(fp+"/model")
model.save("cnn"+str(num_classes)+".model")
#print(model.evaluate(x_test,y_test)) 

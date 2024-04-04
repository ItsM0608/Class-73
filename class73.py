import cv2
from keras.models import load_model
import numpy as np


np.set_printoptions(suppress=True)
model=load_model('keras_model.h5', compile=False)
class_names=open("labels.txt","r").readlines()


camera=cv2.VideoCapture(0)

while True:
    dummy,image= camera.read()
    image=cv2.flip(image,1)
    resizedImage= cv2.resize(image, (224,224), interpolation=cv2.INTER_AREA)


    try:
        image=cv2.putText(resizedImage,class_names[2:],(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)
        image=cv2.putText(resizedImage,str(np.round(confidenceScore*100))[:-2],(10,40),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)

    except Exception as e:
        pass


    cv2.imshow("window",image)
    image=np.asarray(resizedImage,dtype=np.float32).reshape(1,224,224,3)
    image=(image/127.5)-1
    #print(image)

    predicition=model.predict(image)
    print("what is predicition: ",predicition)

    class_name=class_names[index]

    index=np.argmax(predicition)
    class_names=class_names[index]

    confidenceScore= predicition[0][index]

    if cv2.waitKey(25) == 32:
        break

camera.release()
cv2.destroyAllWindows()
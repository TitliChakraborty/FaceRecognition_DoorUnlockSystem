import cv2
import serial
import time
import pyttsx3
confidence=0
def TaskExecution():
     #p.press('esc')
     print("Authentication Successful")
     #print("Door opening")
     #speak("Face recognition complete..it is matching with database...welcome..Door is openning for 5 seconds")
     ard = serial.Serial('com5' ,9600)
     time.sleep(2)
     var = 'a'
     c=var.encode()
     ard.write(c)
     time.sleep(4)
     #print("Door is closing")
     exit()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",140)
engine.setProperty("volume",1000)


recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
recognizer.read('trainer/trainer.yml')   #load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


id = 2 #number of persons you want to Recognize


#names = ['','']  #names, leave first empty bcz counter starts from 0

#cam = cv2.VideoCapture('RecogSample\\face.7.jpg')
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
cam.set(3, 640) # set video FrameWidht
cam.set(4, 480) # set video FrameHeight

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

# flag = True

while True:

    ret, img =cam.read() #read the frames using the above created object

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

    faces = faceCascade.detectMultiScale( 
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

        # Check if accuracy is less them 100 ==> "0" is perfect match 
        if (accuracy < 100):
            confidence = round(100 - accuracy)
            #id = names[id]
            accuracy = "  {0}%".format(round(100 - accuracy))
            #print(accuracy)
            #TaskExecution()

        else:
            id = "unknown"
            confidence = round(100 - accuracy)
            accuracy = "  {0}%".format(round(100 - accuracy))
            # print("Face is Unknown")
            # exit()
        

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        #cv2.putText(img,  "Successfull",(x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 
    time.sleep(4)
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

    if confidence>=45:
        TaskExecution()
    else:
        print("Face is Unknown")
        #speak("face is not matching..please try again")
        ard = serial.Serial('com5' ,9600)
        time.sleep(2)
        var = 'u'
        c=var.encode()
        ard.write(c)
        time.sleep(4)
        print("Door is closing")
        exit()



    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()
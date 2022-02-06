#face detection with python and opencv
"""call two important moudle to work with them
Open cv and numpy"""
import cv2

face = cv2.CascadeClassifier('Face.xml') # call train haarcascade datas

cam = cv2.VideoCapture(0) # Capture video with main device camera

while(True): # read all frames
    _, frame = cam.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # change colors to gray for detect better faces
    faces = face.detectMultiScale(frame)

    for (x, y, w, h) in faces: # draw rectangle environs the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    cv2.imshow("Face", frame) # Show window using frame from camera

    if cv2.waitKey(1) & 0XFF == ord("0"):
        break

cam.release()
cv2.destroyAllWindows()
#Codded by ALIREZA RAHIMI
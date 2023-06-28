import cv2

cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while(True):
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lists = cascade.detectMultiScale(frame_gray, minSize=(100, 100))
    if len(lists):
        for (x,y,w,h) in lists:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), thickness=2)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
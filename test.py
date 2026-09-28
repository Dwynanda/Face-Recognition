import cv2

detect = cv2.CascadeClassifier("ref.xml")
cam = cv2.VideoCapture(0)

def face(frame):
    grei = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    wajah = detect.detectMultiScale(grei, scaleFactor=1.1, minSize=(200,200))
    return wajah

def boxes(frame):
    for x, y, w, h, in face(frame):
        cv2.rectangle(frame, (x, y,), (x + w, y + h), (0, 0, 255), 2)

def reset():
    cam.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        _, frame = cam.read()
        boxes(frame)
        cv2.imshow("test", frame)

        if cv2.waitKey(1) &  0xFF == ord('q'):
            reset()

if __name__ == '__main__':
    main()
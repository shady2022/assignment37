import cv2
import webbrowser
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(1)
detector = cv2.QRCodeDetector()
while True:
    ret, frame = cap.read()
    data, bbox, _ = detector.detectAndDecode(frame)
    
    if not ret:
        break
    
    if data:
        for i in data:
            cv2.putText(frame, i.data.decode("utf-8"), (i.rect[0], i.rect[1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 255, 0), 2, cv2.LINE_AA)

        if cv2.waitKey(1) == ord("e"):
            webbrowser.open(str(data))

    cv2.imshow("QR-Code-scanner", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
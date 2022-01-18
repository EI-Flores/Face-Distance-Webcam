import cv2
import cvzone

from cvzone.FaceMeshModule import FaceMeshDetector

captura = cv2.VideoCapture(1)
detector = FaceMeshDetector(maxFaces=1)

while True:
    sucess, img = captura.read()
    img, caras = detector.findFaceMesh(img, draw=False)

    if caras:
        cara = caras[0]
        pointLeft = cara[145]
        pointRight = cara[374]
        cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3

        # Encuentra la distancia focal
        #W = 6.3 # chk dist % iris (cm)
        #d = 68 # chk dist % ca y ojos (cm)
        #f = (w*d)/W
        # f dió 712
        #print(f)

        # Finding distance
        f = 712
        d = (W*f)/w
        print(d)

        #cvzone.putTextRect()
        cvzone.putTextRect(img, f'Distancia: {int(d)}cm',
                           (cara[10][0]-137, cara[10][1]-50),
                           scale = 2, thickness=2, offset=5)


    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) == ord('q'):
        break

import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

captura = cv2.VideoCapture(1)
detector = FaceMeshDetector(maxFaces=1)

textLista = ["Bienvenido a esta prueba.",
             "Este código se estudia",
             "visión por compuadora",
             "Prueba de texto 1"]

sensibilidad = 10 # mas valor menos sensibilidad

while True:
    sucess, img = captura.read()
    imgTexto = np.zeros_like(img)
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

        # Finding distance
        f = 712
        d = (W*f)/w
        print(d)

        #cvzone.putTextRect()
        cvzone.putTextRect(img, f'Distancia: {int(d)}cm',
                           (cara[10][0]-137, cara[10][1]-50),
                           scale = 2, thickness=2, offset=5)
        for i, text in enumerate(textLista):
            singleHeight = 20 + int((int(d/sensibilidad)*sensibilidad)/4)
            scale = 0.4 + (int(d/sensibilidad)*sensibilidad)/75
            cv2.putText(imgTexto, text, (50, 50 +(i * singleHeight)),
                        cv2.FONT_ITALIC, scale, (255, 255, 255), 2)

    imgStacked = cvzone.stackImages([img,imgTexto], 2, 1)
    cv2.imshow("Webcam", imgStacked)
    if cv2.waitKey(1) == ord('q'):
        break

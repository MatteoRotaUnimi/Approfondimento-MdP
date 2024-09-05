#importo le librerie OpenCV e Numpy
import cv2
import numpy as np

#leggo l'immagine sorgente
img = cv2.imread('Gioconda.jpg')

#creo l'identity kernel
k1 = np.array([[0, 0, 0],
               [0, 1, 0],
               [0, 0, 0]])

#applico la funzione filter2D()
identity = cv2.filter2D(src=img, ddepth=-1, kernel=k1)

#visualizzo l'immagine originale e quella filtrata
cv2.imshow('Originale', img)
cv2.imshow('Identity', identity)

#salvo l'immagine filtrata su disco
cv2.waitKey()
cv2.imwrite('identity.jpg', identity)
cv2.destroyAllWindows()


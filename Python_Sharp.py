#importo le librerie OpenCV e Numpy
import cv2
import numpy as np

#leggo l'immagine sorgente
img = cv2.imread('Gioconda.jpg')

#creo il kernel
k1 = np.array([[0, -1,  0],
               [-1,  5, -1],
               [0, -1,  0]])

#applico la funzione filter2D()
img2 = cv2.filter2D(src=img, ddepth=-1, kernel=k1)

#visualizzo l'immagine originale e quella filtrata
cv2.imshow('Originale', img)
cv2.imshow('Sharpened', img2)

#salvo l'immagine filtrata su disco
cv2.waitKey()
cv2.imwrite('sharp_image.jpg', img2)
cv2.destroyAllWindows()


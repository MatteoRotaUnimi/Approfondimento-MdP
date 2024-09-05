#importo le librerie OpenCV e Numpy
import cv2
import numpy as np

#leggo l'immagine sorgente
img = cv2.imread('Gioconda.jpg')

#applico la funzione bilateralFilter()
img2 = cv2.bilateralFilter(src=img, d=9, sigmaColor=75, sigmaSpace=75)

#visualizzo l'immagine originale e quella filtrata
cv2.imshow('Originale', img)
cv2.imshow('Bilateral Filtering', img2)

#salvo l'immagine filtrata su disco
cv2.waitKey(0)
cv2.imwrite('bilateral_filtering.jpg', img2)
cv2.destroyAllWindows()


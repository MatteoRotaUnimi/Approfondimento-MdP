#importo le librerie OpenCV e Numpy
import cv2
import numpy as np

#leggo l'immagine sorgente
img = cv2.imread('Gioconda.jpg')

#applico la funzione GaussianBlur()
img2 = cv2.GaussianBlur(src=img, ksize=(5,5), sigmaX=0, sigmaY=0)

#visualizzo l'immagine originale e quella filtrata
cv2.imshow('Originale', img)
cv2.imshow('Gaussian Blurred', img2)

#salvo l'immagine filtrata su disco
cv2.waitKey()
cv2.imwrite('gaussian_blur.jpg', img2)
cv2.destroyAllWindows()




#importo le librerie OpenCV e Numpy
import cv2
import numpy as np

#leggo l'immagine sorgente
img = cv2.imread('Gioconda.jpg')

#creo il kernel per la sfocatura
k2 = np.ones((5, 5), np.float32) / 25

#applico la funzione filter2D()
img2 = cv2.filter2D(src=img, ddepth=-1, kernel=k2)

#visualizzo l'immagine originale e quella filtrata
cv2.imshow('Originale', img)
cv2.imshow('Kernel Blur', img2)

#salvo l'immagine filtrata su disco
cv2.waitKey()
cv2.imwrite('blur_kernel.jpg', img2)
cv2.destroyAllWindows()


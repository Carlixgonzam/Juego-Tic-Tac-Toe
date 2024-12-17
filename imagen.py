import cv2
import numpy as np

imagen = cv2.imread('2.jpg')


kernel = np.array([[0, -1, 0], 
                   [-1, 5, -1], 
                   [0, -1, 0]])

imagen_nitida = cv2.filter2D(imagen, -1, kernel)
cv2.imwrite('imagen_mejorada.jpg', imagen_nitida)
cv2.imshow('Imagen Mejorada', imagen_nitida)
cv2.waitKey(0)
cv2.destroyAllWindows()
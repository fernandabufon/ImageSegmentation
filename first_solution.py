#Importando bibliotecas necessárias para a missão
import cv2
import numpy as np

#Carregando a imagem de teste
image = cv2.imread('test.JPG')

#Convertendo a imagem de BGR para HSV, para podermos isolar uma faixa específica de cores (verde) nas imagens
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#Definindo o lower_green e o upper_green, para criar um range de valores que serão considerados verde pelo algoritmo
lower_green = np.array([20, 5, 5])
upper_green = np.array([90, 255, 255])

#Criando uma máscara contendo apenas os pixels que possuem a cor verde, utilizando o range criado anteriormente.
green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

#Aplicando a máscara à imagem original, para obter uma nova imagem apenas com a parte verde.
plantation = cv2.bitwise_and(image, image, mask=green_mask)

#Redimensionando a imagem original e a imagem final para facilitar a visualização do resultado.
plantation_resized = cv2.resize(plantation, (203,608), interpolation=cv2.INTER_CUBIC)
image_resized = cv2.resize(image, (203,608), interpolation=cv2.INTER_CUBIC)

#Mostrando a imagem original e a imagem final
cv2.imshow('Imagem Teste', image_resized)
cv2.imshow('Imagem apenas Plantação', plantation_resized)

#Salvando a imagem obtida
cv2.imwrite('plantation.jpg', plantation)

cv2.waitKey(0)

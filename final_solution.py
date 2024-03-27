#Importando bibliotecas necessárias para a missão
import cv2
import numpy as np
import os

#Criando uma variável contendo o local em que as imagens estão alocadas.
#Nesse caso, a pasta das imagens está na mesma pasta que o app, então coloco apenas o nome da pasta.
pasta_imagens = 'Imagens'

#Criando uma variável com nome 'output'
output_folder = 'output'

#Caso não exista a pasta 'output', ela será criada
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#Definindo a lista de nomes das imagens contida na pasta.
nomes_arquivos = os.listdir(pasta_imagens)

#Definindo o lower_green e o upper_green, para criar um range de valores que serão considerados verde pelo algoritmo.
lower_green = np.array([20, 5, 5])
upper_green = np.array([90, 255, 255])

#Loop para que o algoritmo rode em todas as imagens da pasta.
for nome_arquivo in nomes_arquivos:

    #Definindo o caminho total da imagem utilizando os.path.join
    caminho_imagem = os.path.join(pasta_imagens, nome_arquivo)
    
    #Carregando a imagem
    image = cv2.imread(caminho_imagem)
    
    #IF para verificar se a imagem foi carregada com sucesso
    if image is not None:
        
        #Convertendo a imagem de BGR para HSV, para podermos isolar uma faixa específica de cores (verde) nas imagens
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        #Criando uma máscara contendo apenas os pixels que possuem a cor verde, utilizando o range criado anteriormente.
        green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

        #Aplicando a máscara à imagem original, para obter uma nova imagem apenas com a parte verde.
        plantation = cv2.bitwise_and(image, image, mask=green_mask)
        
        #Criando uma imagem composta combinando a imagem original e a imagem plantation
        combined_image = cv2.hconcat([image, plantation])

        #Redimensionando a imagem original e final combinadas para facilitar a visualização do resultado.
        combined_image_resized = cv2.resize(combined_image, (486,648), interpolation=cv2.INTER_CUBIC)

        #Mostrando o resultado
        cv2.imshow('Antes x Depois', combined_image_resized)
        cv2.waitKey(0)

        #Salvando a imagem gerada (combined_image) na pasta 'output'
        nome_saida = os.path.join(output_folder, "result_" + nome_arquivo)
        cv2.imwrite(nome_saida, combined_image)

#Fecha todas as janelas abertas
cv2.destroyAllWindows()

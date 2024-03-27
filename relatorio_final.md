# Relatório Final - Processo Seletivo CROMAI

**Autor(a):** Fernanda Bufon Farber
**Empresa responsável pelo case:** Cromai

## Resumo do Caso

O objetivo é desenvolver um algoritmo de segmentação de imagens para remover o solo em imagens aéreas de plantações de soja obtidas por drones. O algoritmo precisa ser robusto o suficiente para lidar com variações de iluminação e cenários adversos.

A abordagem sugerida envolve:

- Utilizar técnicas de visão computacional para garantir a precisão na remoção do solo.
- Utilizar técnicas de otimização computacional para acelerar o processamento e escalar o algoritmo.
- Treinar e testar o algoritmo nas imagens fornecidas no diretório "inputs".
- Validar os resultados comparando com exemplos fornecidos no diretório "exemplos".

Os principais desafios são lidar com variações nas condições de iluminação e cenário, além de garantir robustez, precisão, desempenho, e escalabilidade do algoritmo. O sucesso depende de encontrar a melhor combinação de técnicas de visão computacional e otimização computacional.

## Processo de Aprendizado

Primeiramente, foi escolhido o OpenCV como ferramenta principal. Para relembrar do básico e obter um melhor domínio da ferramenta, optei por assistir a um vídeo que explica do básico ao avançado. O vídeo foi responsável por trazer insights importantes e facilitar a resolução do problema. Além dele, acessei alguns sites para me aprofundar melhor e descobrir qual é o melhor método de resolver o problema. Alguns links importantes são:

- Como definir o range de uma cor.
- Como obter um recorte de um objeto de uma cor específica.
- Como utilizar o inRange.
- Utilizando o método os.path.join().

Com esses conteúdos, fui capaz de aprender melhor as funções e decidir qual era a melhor abordagem para o problema.

## Resolução do Problema

Para resolver o problema, decidi criar um roteiro teórico antes de fazer o algoritmo para que dessa forma eu consiga entender melhor os passos para atingir o objetivo e qual é a melhor forma de fazer cada parte do código. Dessa maneira, o roteiro criado inicialmente foi:

1. Carregar a imagem;
2. Converter o sistema de cores para HSV;
3. Definir um range de cores que serão considerados como plantação;
4. Criar uma máscara que será composta apenas pelos pixels que são da cor verde;
5. Aplicar a máscara à imagem real para ter uma imagem somente com a parte verde;
6. Mostrar a imagem sem solo, ou seja, apenas com a parte verde.

Assim, ao fim do processo de definição da solução e do processo de aprendizado, o código resultante que melhor atende o problema foi o seguinte:
![Arquivo first_solution](https://i.imgur.com/dQBNPiA.png "Arquivo first_solution")

Uma vez que o problema foi resolvido, passei a buscar uma forma de automatizar a solução, ou seja, uma forma de rodar todas as imagens da pasta de imagens de uma só vez para agilizar o processo. Utilizei o módulo os.path para conseguir a lista com os nomes das imagens da pasta e dessa maneira criar um for que modifique e mostre cada imagem da pasta. Esse foi o código resultante dessa abordagem:
![Arquivo final_solution](https://i.imgur.com/Ew1sILl.png "Arquivo final_solution")


É importante ressaltar que as variáveis foram nomeadas em inglês por escolha própria para seguir um padrão e melhorar a visualização e entendimento do código uma vez que as funções são em inglês.

## Resultado Final

Utilizando o código mostrado anteriormente, foram obtidas as imagens contendo apenas as plantações. Veja o antes e depois.
![Resultado Final](https://i.imgur.com/i7Zof7s.png "Resultado Final")

## Conclusão

O case do processo seletivo da CROMAI tinha como objetivo final a criação de um algoritmo de segmentação de imagens para remover o solo em imagens de plantações feita por drone. Esse objetivo foi alcançado utilizando técnicas de visão computacional com a ferramenta OpenCV, em Python. O processo de aprendizado permitiu adquirir o conhecimento necessário para criar o algoritmo, e o código resultante resolveu o problema proposto e foi automatizado para processar várias imagens de forma eficiente, economizando tempo e recursos. No resultado final, as imagens obtidas após a aplicação do algoritmo mostram a remoção total do solo e, consequentemente, o sucesso do algoritmo.

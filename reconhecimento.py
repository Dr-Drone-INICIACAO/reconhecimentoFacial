# Código por: https://projetobeachcleaner.blogspot.com/2020/04/visao-computacional-em-sistemas.html
# Xml treinado: https://github.com/opencv/opencv/tree/master/data/haarcascades

# importando a biblioteca OpenCV
import cv2

# Criando um classificador
classificador = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

# Definindo a fonte da letra que será imprimida na tela
fonte = cv2.FONT_HERSHEY_SIMPLEX

# Habilitando a WebCam conectada ao dispositivo
camera = cv2.VideoCapture(0)

# Loop para a detecção tempo real
while 1:
    # Fazendo a leitura da imagem
    conectado, imagem = camera.read()

    # Convertendo a imagem para a escala de cinza
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Atribuindo as classificações a variável facesDetectadas
    facesDetectadas = classificador.detectMultiScale(imagemCinza,
                                                     scaleFactor=1.5,
                                                     minSize=(50, 50))
    # Nas faces dectadas, desenhar um retângulo e escrever Humano
    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        cv2.putText(imagem, 'Humano', (x, y + (a + 30)), fonte, 1, (0, 255, 255))

    cv2.imshow("Face", imagem)
    cv2.waitKey(1)
camera.release()
cv2.destroyAllWindows

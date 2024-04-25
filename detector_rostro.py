import cv2 #importando opencv

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#variable con calor del haardcascade

cap = cv2.VideoCapture(0)#variable para obtener la webcam o nuestra camara en numero 0 pero puede ser otro numero segun N° de la camara

while True : #ciclo while infinito para reciclar la imagen y que se forme rectangulo
    retiro, marco = cap.read()#para leer fotograma del video tiene que ser una tupla
    #retiro es una variable para saber si se pudo leer el fotograma
    gris = cv2.cvtColor(marco, cv2.COLOR_BGR2GRAY ) #convertir a escala de gris para que lo tome mas arapido
    face = face_cascade.detectMultiScale(gris, 1.1, 4)#Variable que llamamos a 
    #variable face_cascade para detectar con .detectMultiScaleScale y parametro de la variable gris
    #y los 1.1, 4  son para ver la escala de gris que va a manejar
    for (x, y, w, h) in face: #(x, y, w, h) son los parametros de vertices para dibujar un rectangulo o cuadrado
        cv2.rectangle(marco, (x, y), (x+w, y+h), (0, 255, 0), 3)#para dibujar un rectangulo en la imagen
        #parametros (img, (x, y), (x+w, y+h), parametros de color(0, 255, 0), 2)
    cv2.imshow('img', marco)#para mostrar la imagen o fotograma con la cara dectectada para ver en webcam
    #detectar si estamos precionando la tecla escape para salir del programa
    esc = cv2.waitKey(30)#waitKey es un metodo que chequea que si cada (30milisec)se preciona la tecla esc
    #para salir del ciclo while puede variar el tiempo modificando el parametro entre ()
    if esc == 27:#si nos devuelve el valor asquit de la tecla esc(que es el valor de la tecla esc)
        #de ser otra tecla no va a salir.
        break   
cap.release()#para dejar de utilizar la webcam





















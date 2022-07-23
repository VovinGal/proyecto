from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import cv2
import matplotlib.pyplot as plt



def captImg():
    cameraObjet= cv2.VideoCapture(0)
          
    #Verifica objeto
    if cameraObjet is not None:
    #capturar fotografia
       retval, imagen = cameraObjet.read()
       if retval == True:
          img = Image.fromarray(imagen)
          img = img.resize((255,220))
          imgTk = ImageTk.PhotoImage(image = imgTk)
          lbl10.configure(image = imgTk)
          lbl10.image =imgTk

          plt.imshow(imagen)
          plt.title('Fotografía')
          plt.show()
    else:
      lbl10.image = ""
      cameraObjet.release()    
                
    cameraObjet.release()

def cerrarVentana():
    frame5.destroy
        
                
#Frame para Fotografía
frame5 = Frame(bg="red")
frame5.place(x=1045,y=0,height=255, width=220)  
lbl10 = Label(frame5)
lbl10.configure(bg="green")
lbl10.place(x=20,y=20, height=180, width=180)

#Botones de Cámara
btnGuardar=Button(frame5,text="Capturar Fotografia", command=captImg, bg="Silver", fg="Black")
btnGuardar.place(x=35,y=210,width=90, height=30)
btnCancelar=Button(frame5,text="Cerrar ventana", command=cerrarVentana, bg="Silver", fg="Black")
btnCancelar.place(x=130,y=210,width=60, height=30)     
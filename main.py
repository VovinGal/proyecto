
from tkinter import *
# from login_in import *
from ventana import *


def main():
    root = Tk()
    root.wm_title("Ingreso Visitantes")
    app = Ventana(root) 
    app.mainloop()



if __name__ == "__main__":
    main()


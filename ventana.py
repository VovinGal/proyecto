# ***************************************

from importlib.resources import path
from logging import root
from tkinter import *
from datos_datos import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from capturaImg import *

"""Creación de Ventana de Ingreso"""

path = 'Img\Logo_1.png'


class Ventana(Frame):

    datos_in = Datos()

    def __init__(self, master=None):
        super().__init__(master, width=1280, height=860, bg="light grey", border="1px")
        self.master = master
        self.pack()
        self.create_widgets()

        self.llenaDatos()
        self.habilitarCajas("disabled")
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")
        self.id = -1

    def habilitarCajas(self, estado):
        self.txtCedula.configure(state=estado)
        self.txtPrimerApell.configure(state=estado)
        self.txtSegundoApell.configure(state=estado)
        self.txtPrimerNom.configure(state=estado)
        self.txtSegundoNom.configure(state=estado)
        self.txtSexo.configure(state=estado)
        self.txtFechaNa.configure(state=estado)
        self.txtRH.configure(state=estado)
        # self.txtIngreso.configure(state=estado)

    def habilitarBtnOper(self, estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarBtnGuardar(self, estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def limpiarCajas(self):
        self.txtCedula.delete(0, END)
        self.txtPrimerNom.delete(0, END)
        self.txtSegundoNom.delete(0, END)
        self.txtPrimerApell.delete(0, END)
        self.txtSegundoApell.delete(0, END)
        self.txtSexo.delete(0, END)
        self.txtFechaNa.delete(0, END)
        self.txtRH.delete(0, END)
        # self.txtIngreso.delete(0,END)

    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def llenaDatos(self):
        datos = self.datos_in.consulta_datos()
        for row in datos:
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4],
                                                           row[5], row[6], row[7], row[8], row[9]))

        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    def fNuevo(self):
        self.habilitarCajas("normal")
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()
        self.txtCedula.focus()

    def fGuardar(self):
        if self.id == -1:
            self.datos_in.inserta_datos(self.txtCedula.get(), self.txtPrimerNom.get(),
                                        self.txtSegundoNom.get(), self.txtPrimerApell.get(),
                                        self.txtSegundoApell.get(), self.txtSexo.get(),
                                        self.txtFechaNa.get(), self.txtRH.get())
            messagebox.showinfo(
                "Insertar", 'Elemento insertado correctamente.')
        else:
            self.datos_in.modifica_datos(self.id, self.txtCedula.get(), self.txtPrimerNom.get(),
                                         self.txtSegundoNom.get(), self.txtPrimerApell.get(),
                                         self.txtSegundoApell.get(), self.txtSexo.get(),
                                         self.txtFechaNa.get(), self.txtRH.get())
            messagebox.showinfo(
                "Modificar", 'Elemento modificado correctamente.')
            self.id = -1
        self.limpiaGrid()
        self.llenaDatos()
        self.limpiarCajas()
        self.habilitarBtnGuardar("disabled")
        self.habilitarBtnOper("normal")
        self.habilitarCajas("disabled")

    def fModificar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')
        if clave == '':
            messagebox.showwarning(
                "Modificar", 'Debes seleccionar un elemento.')
        else:
            self.id = clave
            self.habilitarCajas("normal")
            valores = self.grid.item(selected, 'values')
            self.limpiarCajas()
            self.txtCedula.insert(0, valores[0])
            self.txtPrimerNom.insert(0, valores[1])
            self.txtSegundoNom.insert(0, valores[2])
            self.txtPrimerApell.insert(0, valores[3])
            self.txtSegundoApell.insert(0, valores[4])
            self.txtSexo.insert(0, valores[5])
            self.txtFechaNa.insert(0, valores[6])
            self.txtRH.insert(0, valores[7])
            # self.txtIngreso.insert(0,valores[8])
            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")
            self.txtCedula.focus()

    def fEliminar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')
        if clave == '':
            messagebox.showwarning(
                "Eliminar", 'Debes seleccionar un elemento.')
        else:
            valores = self.grid.item(selected, 'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion(
                "Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)
            if r == messagebox.YES:
                n = self.datos_in.elimina_datos(clave)
                if n == 1:
                    messagebox.showinfo(
                        "Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning(
                        "Eliminar", 'No fue posible eliminar el elemento.')

    def fCancelar(self):
        r = messagebox.askquestion(
            "Calcelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajas()
            self.habilitarBtnGuardar("disabled")
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disabled")

    def fActivarCam(self):
        pass

    def fCapturar(self):
        pass

    def create_widgets(self):

        # Frame para Botones
        frame1 = Frame(self, bg="light grey")
        frame1.place(x=470, y=500, width=280, height=120)
        self.btnNuevo = Button(frame1, text="Nuevo",
                               command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5, y=50, width=80, height=30)
        self.btnModificar = Button(
            frame1, text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=90, y=50, width=80, height=30)
        self.btnEliminar = Button(
            frame1, text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=175, y=50, width=80, height=30)

    # Frame para Cajas de Texto
        frame2 = Frame(self, bg="light grey")
        frame2.place(x=5, y=0, width=180, height=510)
        lbl1 = Label(frame2, text="Cedula: ")
        lbl1.configure(bg="light grey")
        lbl1.place(x=3, y=5)
        self.txtCedula = Entry(frame2)
        self.txtCedula.place(x=3, y=25, width=100, height=20)
        lbl2 = Label(frame2, text="Primer Apellido: ")
        lbl2.configure(bg="light grey")
        lbl2.place(x=3, y=55)
        self.txtPrimerApell = Entry(frame2)
        self.txtPrimerApell.place(x=3, y=75, width=100, height=20)
        lbl3 = Label(frame2, text="Segundo Apellido: ")
        lbl3.configure(bg="light grey")
        lbl3.place(x=3, y=105)
        self.txtSegundoApell = Entry(frame2)
        self.txtSegundoApell.place(x=3, y=125, width=100, height=20)
        lbl4 = Label(frame2, text="Primer Nombre: ")
        lbl4.place(x=3, y=155)
        lbl4.configure(bg="light grey")
        self.txtPrimerNom = Entry(frame2)
        self.txtPrimerNom.place(x=3, y=175, width=100, height=20)
        lbl5 = Label(frame2, text="Segundo Nombre: ")
        lbl5.configure(bg="light grey")
        lbl5.place(x=3, y=205)
        self.txtSegundoNom = Entry(frame2)
        self.txtSegundoNom.place(x=3, y=225, width=100, height=20)
        lbl6 = Label(frame2, text="Sexo: ")
        lbl6.configure(bg="light grey")
        lbl6.place(x=3, y=255)
        self.txtSexo = Entry(frame2)
        self.txtSexo.place(x=3, y=275, width=100, height=20)
        lbl7 = Label(frame2, text="Fecha Nacimiento: ")
        lbl7.configure(bg="light grey")
        lbl7.place(x=3, y=305)
        self.txtFechaNa = Entry(frame2)
        self.txtFechaNa.place(x=3, y=325, width=100, height=20)
        lbl8 = Label(frame2, text="RH: ")
        lbl8.configure(bg="light grey")
        lbl8.place(x=3, y=355)
        self.txtRH = Entry(frame2)
        self.txtRH.place(x=3, y=375, width=100, height=20)
        # lbl9 = Label(frame2,text="Ingreso: ")
        # lbl9.place(x=3,y=405)
        # lbl9.configure(bg="light grey")
        # self.txtIngreso=Entry(frame2)
        # self.txtIngreso.place(x=3,y=425,width=100, height=20)

        # Botones de Acción
        self.btnGuardar = Button(
            frame2, text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10, y=425, width=60, height=30)
        self.btnCancelar = Button(
            frame2, text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80, y=425, width=60, height=30)

        # Frame para Imagen
        frame3 = Frame(self, bg="light grey")
        frame3.place(x=480, y=600, height=80)
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.imgLabel = Label(frame3, image=self.img)
        self.panel = Label(frame3, image=self.img)
        self.panel.image = self.img
        self.panel.pack()

    # Frame para Treeview
        frame4 = Frame(self, bg="white")
        frame4.place(x=180, y=0, width=855, height=480)
        self.grid = ttk.Treeview(frame4, columns=(
            "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
        self.grid.column("#0", width=55, stretch=True)
        self.grid.column("col1", width=70, anchor=CENTER)
        self.grid.column("col2", width=90, anchor=CENTER)
        self.grid.column("col3", width=90, anchor=CENTER)
        self.grid.column("col4", width=90, anchor=CENTER)
        self.grid.column("col5", width=90, anchor=CENTER)
        self.grid.column("col6", width=90, anchor=CENTER)
        self.grid.column("col7", width=90, anchor=CENTER)
        self.grid.column("col8", width=60, anchor=CENTER)
        self.grid.column("col9", width=110, anchor=CENTER)
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Cedula", anchor=CENTER)
        self.grid.heading("col2", text="1er Apellido", anchor=CENTER)
        self.grid.heading("col3", text="2do Apellido", anchor=CENTER)
        self.grid.heading("col4", text="1er Nombre", anchor=CENTER)
        self.grid.heading("col5", text="2do Nombre", anchor=CENTER)
        self.grid.heading("col6", text="Sexo", anchor=CENTER)
        self.grid.heading("col7", text="Fecha Nacimiento", anchor=CENTER)
        self.grid.heading("col8", text="RH", anchor=CENTER)
        self.grid.heading("col9", text="Ingreso", anchor=CENTER)
        self.grid.pack(side=LEFT, fill=Y)
        sb = Scrollbar(frame4, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode'] = 'browse'

        # #Frame para Fotografía
        # frame5 = Frame(self,bg="red")
        # frame5.place(x=1045,y=0,height=255, width=220)
        # lbl1 = Label(frame5)
        # lbl1.configure(bg="green")
        # lbl1.place(x=20,y=20, height=180, width=180)

        # #Botones de Cámara
        # self.btnGuardar=Button(frame5,text="Activar Cámara", command=self.fActivarCam, bg="Silver", fg="Black")
        # self.btnGuardar.place(x=35,y=210,width=90, height=30)
        # self.btnCancelar=Button(frame5,text="Capturar", command=self.fCapturar, bg="Silver", fg="Black")
        # self.btnCancelar.place(x=130,y=210,width=60, height=30)

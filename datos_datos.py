import mysql.connector

class Datos:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="Lucy1217", database="ingresodb")
        print('Estoy conectado al Servidor SQL')

    def __str__(self):
        datos=self.consulta_datos()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_datos(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM visitantes")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_datos(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM visitantes WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_datos(self, Cedula, PrimerApell, SegundoApell, PrimerNom, SegundoNom, Sexo, FechaNa, RH):
        cur = self.cnn.cursor()
        sql='''INSERT INTO visitantes(Cedula, PrimerApell, SegundoApell, PrimerNom, SegundoNom, Sexo, FechaNa, RH) 
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}')'''.format(Cedula, PrimerApell, SegundoApell, PrimerNom, SegundoNom, Sexo, FechaNa, RH)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_datos(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM visitantes WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_datos(self, Id, Cedula, PrimerApell, SegundoApell, PrimerNom, SegundoNom, Sexo, FechaNa, RH):
        cur = self.cnn.cursor()
        sql='''UPDATE visitantes SET Cedula='{}', PrimerApell='{}', SegundoApell='{}', PrimerNom='{}',
        SegundoNom='{}', Sexo='{}', FechaNa='{}', RH='{}' WHERE Id= {}'''.format(Cedula, PrimerApell, SegundoApell, PrimerNom, SegundoNom, Sexo, FechaNa, RH, Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

class Login_datos():
        # self.conexion = mysql.connector.connect( host='localhost',
        #                                     database ='ingresodb', 
        #                                     user = 'root',
        #                                     password ='Lucy1217')

    def buscar_users(self, users):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM login WHERE Users = {}".format(users)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()     
        return usersx 

    def buscar_password(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM login WHERE Pass = {}".format(password) #
        cur.execute(sql)
        passwx = cur.fetchall()
        cur.close()     
        return passwx 
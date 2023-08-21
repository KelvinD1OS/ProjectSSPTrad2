#Creamos la clase
class analizador:

    #Inicializamos la estancia de la clase
    def __init__(self, e):
        
        self.entrada = str(e)
        #Separa la entrada por espacios en una lista
        self.splitEntrada = self.entrada.split(" ")
        #Declara el estado inicial en 0

    #Se devuelve el simbolo y el numero
    def returnTipo(self,estado):

        if estado == 0:

            return "Error"

        elif estado == 1:

            return "Entero", 1

        elif estado == 2:

            return "Error"

        elif estado == 3:

            return "Real", 2

        elif estado == 4:

            return "Identificador", 0

        elif estado == 5:

            return "+", 5

        elif estado == 6:

            return "-", 5

        elif estado == 7:

            return "*", 6
        elif estado == 8:

            return "/", 6
        elif estado == 9:

            return "OP. RELACIONAL", 7
        elif estado == 10:

            return "||", 8
        elif estado == 11:

            return "&&", 9
        elif estado == 12:

            return "!", 10
        elif estado == 13:

            return "OP. IGUALDAD", 11
        elif estado == 14:

            return ";", 12
        elif estado == 15:

            return "(", 14
        elif estado == 16:

            return ")", 15
        elif estado == 17:

            return "{", 16
        elif estado == 18:

            return "}", 17
        elif estado == 19:

            return "=", 18
        elif estado == 20:

            return "if", 19
        elif estado == 21:

            return "while", 20
        elif estado == 22:

            return "return", 21
        elif estado == 23:

            return "else", 22
        elif estado == 24:

            return "int", 4
        elif estado == 25:

            return "float", 4
        elif estado == 26:

            return "$", 23
        elif estado == 27:

            return "CADENA", 3
        elif estado == 28:

            return ",", 13
        elif estado == 29:

            return "void", 4
    
    #Toma una cadena y determina el elemento
    def evaluaElemento(self, cadena):

        estado = 0
    

        #PALABRAS RESERVADAS

        if cadena == "if" and estado==0:

            estado = 20
        elif cadena == "while" and estado==0:

            estado = 21
        elif cadena == "return" and estado==0:

                estado = 22
        elif cadena == "else" and estado==0:

            estado = 23
        elif cadena == "int" and estado==0:

            estado = 24
        elif cadena == "float" and estado==0:

            estado = 25
        elif cadena == "void" and estado==0:

            estado = 29
        elif cadena == "==" and estado==0:

            estado = 13

        else:
            
            for i in cadena:

                #Se mantiene en estado 1 es ENTERO
                if i.isnumeric() and estado==0:

                    estado = 1
                elif i.isnumeric() and estado==1:
                    
                    estado=1

                #Si tiene un punto y esta en el estado 1 pasa al segundo estado
                elif i == "." and estado==1:

                    estado = 2

                #Si esta en el estado 2 y tiene numero es REAL
                elif estado==2 and i.isnumeric:

                    estado = 3

                #Reconoce simbolos aritmeticos
                elif i == "+" and estado==0:

                    estado = 5

                elif i == "-" and estado==0:

                    estado = 6

                elif i == "*" and estado==0:

                    estado = 7

                elif i == "/" and estado==0:

                    estado = 8
                #Operadores Relacionales
                elif (i == "<" or i == ">") and estado==0:

                    estado = 9
                elif i == "=" and estado == 9:

                    estado = 9
                elif i == "|" and estado==0:

                    estado = 10
                elif i == "&" and estado==0:

                    estado = 11
                elif i == "!" and estado==0:

                    estado = 12
                elif i == "=" and (estado==12 or estado==19):

                    estado = 13
                elif i == ";" and estado==0:

                    estado = 14
                elif i == "(" and estado==0:

                    estado = 15
                elif i == ")" and estado==0:

                    estado = 16
                elif i == "{" and estado==0:

                    estado = 17
                elif i == "}" and estado==0:

                    estado = 18
                elif i == "}" and estado==0:

                    estado = 18
                elif i == "=" and estado==0:

                    estado = 19
                elif i == "$" and estado==0:

                    estado = 26
                elif i == "," and estado==0:

                    estado = 28
                elif (i == '"' or i == "'") and estado == 0:

                    estado = 27
                elif (i.isnumeric()==False or i == '"' or i == "'") and estado == 27:

                    estado = 27
                    
                #Si empieza con letra y esta en el estado 0 es IDENTIFICADOR
                elif i.isnumeric()==False and estado==0:
		    estado = 4

       		# Si contiene un punto y es numérico después de quitar el punto, es REAL
        	elif "." in cadena and cadena.replace(".", "", 1).isnumeric():
            	    estado = 3

        return estado

    #Se crean las columnas para el resultado
    def iniciarAnalizador(self):
        print("{:<15} {:<15} {:<15}".format("Entrada", "Simbolo", "Tipo"))
        for i in self.splitEntrada:
            tipo, tipo_numero = self.returnTipo(self.evaluaElemento(i))
            print("{:<15} {:<15} {:<15}".format(i, tipo, tipo_numero))

          

#Verifica si ya se ejecuto el script para pedirle al usuario una cadena e inicializar todo
if __name__ == "__main__":
    entrada_usuario = input("Ingrese una cadena de texto: ")
    analizador_instancia = analizador(entrada_usuario)
    analizador_instancia.iniciarAnalizador()

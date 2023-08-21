#Creamos la clase
class analizador:

    #Inicializamos la estancia de la clase	
    def __init__(self, e):
        self.entrada = str(e)
        self.splitEntrada = self.entrada.split(" ")

    #Se devuelve el simbolo y el numero
    def returnTipo(self, estado):
        if estado == 0:
            return "Error", 0
        elif estado == 2:
            return "Error", 0
        elif estado == 3:
            return "Real", 2
        elif estado == 4:
            return "Identificador", 0

    #Toma una cadena y determina el elemento
    def evaluaElemento(self, cadena):
        estado = 0

        # Si empieza con letra y esta en el estado 0, es IDENTIFICADOR
        if cadena.isnumeric() == False and estado == 0:
            estado = 4

        # Si contiene un punto y es numerico despues de quitar el punto, es REAL
        if "." in cadena and cadena.replace(".", "", 1).isnumeric():
            estado = 3

        return estado

    #Se crean las columnas para el resultado
    def iniciarAnalizador(self):
        print("{:<15} {:<15} {:<15}".format("Entrada", "Simbolo", "Tipo"))
        for i in self.splitEntrada:
            simbolo, tipo = self.returnTipo(self.evaluaElemento(i))
            print("{:<15} {:<15} {:<15}".format(i, simbolo, tipo))

#Verifica si ya se ejecuto el script para pedirle al usuario una cadena e inicializar todo
if __name__ == "__main__":
    entrada_usuario = input("Ingrese una cadena de texto: ")
    analizador_instancia = analizador(entrada_usuario)
    analizador_instancia.iniciarAnalizador()

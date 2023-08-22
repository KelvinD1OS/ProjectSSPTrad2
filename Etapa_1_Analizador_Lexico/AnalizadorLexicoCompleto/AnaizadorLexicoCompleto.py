#Definimos la clase token un objeto con 3 valores para la salida
class Token:
    def __init__(self, valor, tipo, tipo_num):
        self.valor = valor
        self.tipo = tipo
        self.tipo_num = tipo_num
#Definicion de la clase analizador e inicializacion de la misma
class AnalizadorLexico:
    def __init__(self, entrada):
        self.entrada = entrada
        self.posicion = 0
        self.palabras_reservadas = ["while", "return", "else", "if"]
#Una tabla con los simbolos para poder trabajar con ellos
        self.tabla_simbolos = {
            "IDENTIFICADOR": 0,
            "NUMERO_ENTERO": 1,
            "NUMERO_REAL": 2,
            "CADENA": 3,
            "TIPO": 4,
            "OPERADOR_Suma": 5,
            "OPERADOR_Mul": 6,
            "OPERADOR_Relac": 7,
            "OPERADOR_Or": 8,
            "OPERADOR_And": 9,
            "OPERADOR_Not": 10,
            "OPERADOR_IGUALDAD": 11,
            ";": 12,
            ",": 13,
            "(": 14,
            ")": 15,
            "{": 16,
            "}": 17,
            "=": 18,
            "if": 19,
            "while": 20,
            "return": 21,
            "else": 22,
            "$": 23
        }
#Funcion para reconocer los tokens
    def obtener_siguiente_token(self):
        while self.posicion < len(self.entrada):
            if self.entrada[self.posicion].isspace():
                self.posicion += 1
                continue
            
            if self.entrada[self.posicion].isalpha():
                inicio = self.posicion
                while self.posicion < len(self.entrada) and (self.entrada[self.posicion].isalpha() or self.entrada[self.posicion].isdigit()):
                    self.posicion += 1
                token_tipo = "IDENTIFICADOR"
                token_valor = self.entrada[inicio:self.posicion]
                token_tipo_num = self.tabla_simbolos[token_tipo]
            

            #---------------------------------------------------------------           
            
         # Verificar si el identificador es una palabra reservada
                if token_valor in self.palabras_reservadas:
                    token_tipo = token_valor.lower()  # Convertir a mayúsculas
                    token_tipo_num = self.tabla_simbolos[token_tipo]
                    return Token(token_valor, token_tipo, token_tipo_num)
                
         # Verificar si el identificador es un tipo ("int", "float", "void")
                tipos = ["int", "float", "void"]
                if token_valor in tipos:
                    token_tipo = "TIPO"
                    token_tipo_num = self.tabla_simbolos["TIPO"]
                    return Token(token_valor, token_tipo, token_tipo_num)
                
                # Si no es palabra reservada ni tipo, es un identificador
                return Token(token_valor, token_tipo, token_tipo_num)

                
        #NUMERO REAL Y ENTERO
            if self.entrada[self.posicion].isdigit():
                inicio = self.posicion
                while self.posicion < len(self.entrada) and (self.entrada[self.posicion].isdigit() or self.entrada[self.posicion] == "."):
                    self.posicion += 1
                token_valor = self.entrada[inicio:self.posicion]
                if "." in token_valor:
                    token_tipo = "NUMERO_REAL"
                    token_tipo_num = self.tabla_simbolos["NUMERO_REAL"]
                else:
                    token_tipo = "NUMERO_ENTERO"
                    token_tipo_num = self.tabla_simbolos["NUMERO_ENTERO"]
                return Token(token_valor, token_tipo, token_tipo_num)
        #*********************************************************
        
        #Op SUMA Y MUL
            if self.entrada[self.posicion] in "+-":
                token_tipo = "OPERADOR_Suma"
                token_valor = self.entrada[self.posicion]
                token_tipo_num = self.tabla_simbolos["OPERADOR_Suma"]
                self.posicion += 1
                return Token(token_valor, token_tipo, token_tipo_num)
                
            if self.entrada[self.posicion] in "*/":
                token_tipo = "OPERADOR_Mul"
                token_valor = self.entrada[self.posicion]
                token_tipo_num = self.tabla_simbolos["OPERADOR_Mul"]
                self.posicion += 1
                return Token(token_valor, token_tipo, token_tipo_num)
        #******************************************
        
        #Signos solos
            if self.entrada[self.posicion] in ";":
                token_tipo = ";"
                token_valor = self.entrada[self.posicion]
                token_tipo_num = self.tabla_simbolos[";"]
                self.posicion += 1
                return Token(token_valor, token_tipo, token_tipo_num)
                
            if self.entrada[self.posicion] in ",":
                token_tipo = ","
                token_valor = self.entrada[self.posicion]
                token_tipo_num = self.tabla_simbolos[","]
                self.posicion += 1
                return Token(token_valor, token_tipo, token_tipo_num)
            
            if self.entrada[self.posicion] in "(":
                token_tipo = "("
                token_valor = self.entrada[self.posicion]
                token_tipo_num = self.tabla_simbolos["("]
                self.posicion += 1
                return Token(token_valor, token_tipo, token_tipo_num)
                
            if self.entrada[self.posicion] in ")":
                token_tipo = ")"
                token_valor = self.entrada[self.posicion]
                token_tipo_num = self.tabla_simbolos[")"]
                self.posicion += 1
                return Token(token_valor, token_tipo, token_tipo_num)
            
            if self.entrada[self.posicion] in "{":
                token_tipo = "{"
                token_valor = self.entrada[self.posicion]
                token_tipo_num = self.tabla_simbolos["{"]
                self.posicion += 1
                return Token(token_valor, token_tipo, token_tipo_num)
                
            if self.entrada[self.posicion] in "}":
                token_tipo = "}"
                token_valor = self.entrada[self.posicion]
                token_tipo_num = self.tabla_simbolos["}"]
                self.posicion += 1
                return Token(token_valor, token_tipo, token_tipo_num)
                
        #*****************************************************************
           
        #Op Relacionales y de Igualdad 
        # Op Relacionales y de Igualdad
            operadores_relacionales = ["<=", ">=", "<", ">", "==", "!="]
            for operador in operadores_relacionales:
                if self.posicion + len(operador) <= len(self.entrada) and self.entrada[self.posicion:self.posicion + len(operador)] == operador:
                    token_tipo = "OPERADOR_Relac" if operador in ["<=", ">=", "<", ">"] else "OPERADOR_IGUALDAD"
                    token_valor = operador
                    token_tipo_num = self.tabla_simbolos[token_tipo]
                    self.posicion += len(operador)  # Avanzar la longitud del operador
                    return Token(token_valor, token_tipo, token_tipo_num)
        #*********************************************************************
        #Operador = 
            if self.entrada[self.posicion] in "=":
                token_tipo = "="
                token_valor = self.entrada[self.posicion]
                token_tipo_num = self.tabla_simbolos["="]
                self.posicion += 1
                return Token(token_valor, token_tipo, token_tipo_num)

        
           
        #************************************************************************
           
        #Op OR, AND Y NOT
            if self.entrada[self.posicion] in "!":
                token_tipo = "OPERADOR_Not"
                token_valor = self.entrada[self.posicion]
                token_tipo_num = self.tabla_simbolos["OPERADOR_Not"]
                self.posicion += 1
                return Token(token_valor, token_tipo, token_tipo_num)
            
            
            if self.entrada[self.posicion:self.posicion + 2] == "||":
                token_tipo = "OPERADOR_Or"
                token_valor = "||"
                token_tipo_num = self.tabla_simbolos["OPERADOR_Or"]
                self.posicion += 2
                return Token(token_valor, token_tipo, token_tipo_num)
            
            if self.entrada[self.posicion:self.posicion + 2] == "&&":
                token_tipo = "OPERADOR_And"
                token_valor = "&&"
                token_tipo_num = self.tabla_simbolos["OPERADOR_And"]
                self.posicion += 2
                return Token(token_valor, token_tipo, token_tipo_num)
        #**********************************************************
        
            tipos = ["int", "float", "void"]
            for tipo in tipos:
                if self.posicion + len(tipo) <= len(self.entrada) and self.entrada[self.posicion:self.posicion + len(tipo)].lower() == tipo:
                    token = Token(tipo, "TIPO", self.tabla_simbolos["TIPO"])
                    self.posicion += len(tipo)  # Avanzar la longitud del tipo
                    return Token(token_valor, token_tipo, token_tipo_num)
            
        # Identificar palabras reservadas (minúsculas)
            if self.posicion + 3 <= len(self.entrada) and self.entrada[self.posicion:self.posicion + 3].lower() in (palabra.lower() for palabra in self.palabras_reservadas):
                palabra_reservada = self.entrada[self.posicion:self.posicion + 3]
                token_tipo = palabra_reservada
                token_valor = palabra_reservada
                token_tipo_num = self.tabla_simbolos[token_tipo]
                self.posicion += 3
                return Token(token_valor, token_tipo, token_tipo_num)
        #**********************************************************************
                            
            if self.entrada[self.posicion] in "$":
                token_tipo = "$"
                token_valor = self.entrada[self.posicion]
                token_tipo_num = self.tabla_simbolos["$"]
                self.posicion += 1
                return Token(token_valor, token_tipo, token_tipo_num)
           

            tipos = ["int", "float", "void"]
            for tipo in tipos:
                if self.posicion + len(tipo) < len(self.entrada) and self.entrada[self.posicion:self.posicion + len(tipo)] == tipo:
                    token = Token(tipo, "TIPO", self.tabla_simbolos["TIPO"])
                    self.posicion += len(tipo)  # Avanzar la longitud del tipo
                    return token
        #CADENAS
            if self.entrada[self.posicion] == '"':
                inicio = self.posicion
                self.posicion += 1
                while self.posicion < len(self.entrada) and self.entrada[self.posicion] != '"':
                    self.posicion += 1
                if self.posicion < len(self.entrada) and self.entrada[self.posicion] == '"':
                    self.posicion += 1
                    return Token(self.entrada[inicio:self.posicion], "CADENA", self.tabla_simbolos["CADENA"])
        #**************************************************

            self.posicion += 1
        
        return None
#Verifica si ya se ejecuto el script para pedirle al usuario una cadena e inicializar todo
if __name__ == "__main__":
    entrada_usuario = input("Ingrese una cadena de texto: ")
    analizador = AnalizadorLexico(entrada_usuario)
    
    print("=" * 66)
    print("{:<18} {:<24} {:<10}".format("Entrada", "Simbolo", "Tipo de numero"))
    print("=" * 66)
    
    token = analizador.obtener_siguiente_token()
    while token:
        print("{:<18} {:<24} {:<10}".format(token.valor, token.tipo, token.tipo_num))
        token = analizador.obtener_siguiente_token()

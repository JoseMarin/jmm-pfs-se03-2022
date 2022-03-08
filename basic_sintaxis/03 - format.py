# Múltiples líneas

# En algunas situaciones se puede dar el caso de que queramos tener una sola instrucción en varias línea de código. Uno
# de los motivos principales podría ser que fuera demasiado larga, y de hecho en la especificación PEP8 se recomienda
# que las líneas no excedan los 79 caracteres.

# main method
if __name__ == '__main__':

    a = 1 + 2 + 3 + 4 + \
        5 + 6 + 7 + 8

    print('Valor de a: ' + str(a))

    x = (1 + 2 + 3 + 4 +
         5 + 6 + 7 + 8)

    def suma(a, b, c):
        return a + b + c

    d = suma(10,
            23,
            3)
    
    print('Valor de d: ' + str(d))

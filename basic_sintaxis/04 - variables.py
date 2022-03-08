# main method
if __name__ == '__main__':
    if True:
        print("True")

    x = y = z = 10
    print('valor de x:' + str(x) + '; valor de y: ' + str(y) + '; valor de z: ' + str(z))
    x, y = 4, 2
    print('valor de x:' + str(x) + '; valor de y: ' + str(y) + '; valor de z: ' + str(z))
    x, y, z = 1, 2, 3
    print('valor de x=>', x, '; valor de y=>', y, '; valor de z=>', z)

    # Nombrando variables ---------------------------------------------------------------------------------------------
    # Válido
    _variable = 10
    vari_able = 20
    variable10 = 30
    variable = 60
    variaBle = 10

    # No válido
    # 2 variable = 10
    # var-iable = 10
    # var iable = 10

    # palabras reservadas utilizadas por Python internamente ----------------------------------------------------------
    import keyword

    print(keyword.kwlist)

    # Uso de paréntesis -----------------------------------------------------------------------------------------------
    x = 10
    y = x * 3 - 3 ** 10 - 2 + 3
    x = 10
    y = (x * 3 - 3) ** (10 - 2) + 3

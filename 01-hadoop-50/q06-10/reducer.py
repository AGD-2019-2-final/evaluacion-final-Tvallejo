import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    clave_actual = None
    minimo = 0; maximo = 0
    for line in sys.stdin:
        clave, valor = line.split("\t")
        valor = float(valor)
        if clave_actual == clave:
            minimo = valor if valor < minimo else minimo
            maximo = valor if valor > maximo else maximo
        else:
            if clave_actual is not None:
                print("{}\t{}\t{}".format(clave_actual, maximo, minimo))
            clave_actual = clave
            minimo = valor
            maximo = valor
    print("{}\t{}\t{}".format(clave_actual, maximo, minimo))
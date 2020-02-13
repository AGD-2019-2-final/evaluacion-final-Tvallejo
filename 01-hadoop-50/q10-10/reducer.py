import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    clave_actual = None
    numero_actual = ""
    for line in sys.stdin:
        tmp, clave, valor = line.split("\t")
        valor = valor.strip()
        if clave_actual == clave:
            numero_actual = "{},{}".format(numero_actual, valor)
        else:
            if clave_actual is not None:
                print("{}\t{}".format(clave_actual, numero_actual))
            clave_actual = clave
            numero_actual = valor
    print("{}\t{}".format(clave_actual, numero_actual))
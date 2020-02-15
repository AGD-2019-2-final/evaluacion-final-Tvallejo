import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == "__main__":
    clave_actual = None
    total = 0
    for line in sys.stdin:
        Clave, valor = line.split("\t")
        valor = int(valor)
        if Clave == clave_actual:
            total += valor
        else:
            if clave_actual is not None:
                print("{}\t{}".format(clave_actual, total))
            clave_actual = Clave
            total = valor
    print("{}\t{}".format(clave_actual, total))
        
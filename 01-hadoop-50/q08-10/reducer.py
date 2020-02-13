import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    clave_actual = None
    total = 0; count = 0
    for line in sys.stdin:
        clave, valor = line.split("\t")
        valor = float(valor)
        if clave_actual == clave:
            total += valor; count += 1
        else:
            if clave_actual is not None:
                print("{}\t{}\t{}".format(clave_actual, total, (total/count)))
            clave_actual = clave
            total = valor; count = 1
    print("{}\t{}\t{}".format(clave_actual, total, (total/count)))
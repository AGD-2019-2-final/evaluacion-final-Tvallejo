import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    for line in sys.stdin:
        line_split = line.split("   ")
        numero = line_split[2].strip(); number_int = int(numero)
        numero = ("0" + numero) if number_int < 100 else numero
        numero = ("0" + numero) if number_int < 10 else numero
        print("{}{}\t{}\t{}\t{}".format(
            line_split[0],numero, line_split[0],line_split[1],str(number_int)))
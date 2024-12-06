conjuntoA = input("Conjunto A: ").split(",")
conjuntoB = input("Conjunto B: ").split(",")



def pares(conjuntoA, conjuntoB):

    resultado = []
    for a in conjuntoA:
        for b in conjuntoB:
                resultado.append((a, b))
    return resultado

rr = pares(conjuntoA, conjuntoB)


qnt = len(rr)
print("quantidade de pares: ", qnt)

for p in rr:
    print(p)

    
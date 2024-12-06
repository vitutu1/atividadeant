conjuntoA = input("Conjunto A: ").split(",")
conjuntoB = input("Conjunto B: ").split(",")



def pares(conjuntoA, conjuntoB):

    po = []
    for a in conjuntoA:
        for b in conjuntoB:
                po.append((a, b))
    return po

rr = pares(conjuntoA, conjuntoB)


qnt = len(rr)
print("quantidade de pares: ", qnt)

for p in rr:
    print(p)

    

def metade(p = 0, format = False):
    res = p / 2
    return res if format is False else moeda(res)

def dobro(p = 0, format = False):
    res = p * 2
    return res if format is False else moeda(res)

def aumentar(p = 0, x = 0, format = False):
    res = p + (x/100 * p)
    return res if format is False else moeda(res)
 
    
def diminuir(p = 0, x = 0, format = False):
     res = p - (x/100 * p)
     return res if format is False else moeda(res)

def moeda(p = 0, moeda = 'R$'):
    return f"{moeda}{p:.2f}".replace(".",",")

def resumo(p = 0, taxa = 10, taxar = 13):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(p)}")
    print(f"Dobro do preço: \t{dobro(p, True)}")
    print(f"Metade do preço: \t{metade(p, True)}")
    print(f"{taxa}% de aumento: \t{aumentar(p, taxa, True)}")
    print(f"{taxar}% de redução: \t{diminuir(p, taxar, True)}")
    print("-" * 30)
    
    
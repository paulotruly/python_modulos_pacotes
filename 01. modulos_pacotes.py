from modulos_pacotes_uteis import numeros

num = int(input("Digite o valor: "))
fat = numeros.fatorial(num)

print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {numeros.dobro(num)}")

qtd=0
soma=0
media=0

valor=float(input("insira uma nota: "))

while (qtd<3):
    qtd=qtd+1
    soma=soma + valor
    valor=float(input("insira uma nota: "))

media=soma/qtd
print("\n total soma: ", soma)
print("\n bimestres: ", qtd+1)
print("\n a media é de: ", media)


if media<=7:
    print("Reprovado")



else:
    print("Aprovado")
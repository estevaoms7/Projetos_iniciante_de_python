MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
IDADE_ESPECIAL2 = 16

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar a CHN.")

elif idade == IDADE_ESPECIAL2:
    print("Você nâo tem idade para tirar a CNH")
    print("Mas já pode fazer aulas teóricas")

elif idade == IDADE_ESPECIAL:
    print("Você não tem idade para às aulas práticas")
    print("Mas já pode fazer os exames")
else:
    print("Você não tem idade para tirar a CNH.")
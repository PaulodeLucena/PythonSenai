totalpessoas = int(input("qual o número de pessoas que vão votar: "))

voto1 = 0
voto2 = 0
voto3 = 0

pessoasvotos = 0

while pessoasvotos < totalpessoas:
    voto = int(input("Vote no participante (1, 2 ou 3): "))
    
    if voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
    elif voto == 3:
        voto3 += 1
    else:
        print("esse número não está na lista de votos. Vote em 1, 2 ou 3.")

    pessoasvotos += 1

print(f"O participante 1 teve {voto1} votos")
print(f"O Participante 2 teve {voto2} votos")
print(f"O Participante 3 teve {voto3} votos")


nota = int(input('Digite um numero de 0 a 100: '))

if nota >= 90:
    print(f'A nota do aluno tirou {nota} Aluno recebeu a nota A')
elif nota >= 80 and nota < 90:
    print(f'A nota do aluno tirou {nota} Aluno recebeu a nota B')
elif nota >= 70 and nota < 80:
    print(f'A nota do aluno tirou {nota} Aluno recebeu a nota C')
elif nota >= 60 and nota < 70:
    print(f'A nota do aluno tirou {nota} Aluno recebeu a nota D')
else:
    print('A nota do aluno recebeu a nota F')

    
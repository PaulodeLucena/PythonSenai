salario = float(input('Digite o salário do colaborador: R$'))

if salario <= 280.00:
    novosalario = salario * 1.20
    print(f'O salário antes do reajuste era {salario:.2f}, o percentual de aumento aplicado foi 20%, o valor do aumento foi de {salario * 0.20:.2f} e o novo salário é R${novosalario:.2f}')
elif salario > 280.00 and salario <= 700.00:
    novosalario = salario * 1.15
    print(f'O salário antes do reajuste era {salario:.2f}, o percentual de aumento aplicado foi 15%, o valor do aumento foi de {salario * 0.15:.2f} e o novo salário é R${novosalario:.2f}')
elif salario > 700.00 and salario <= 1500.00:
    novosalario = salario * 1.10
    print(f'O salário antes do reajuste era {salario:.2f}, o percentual de aumento aplicado foi 10%, o valor do aumento foi de {salario * 0.10:.2f} e o novo salário é R${novosalario:.2f}')
else:
    novosalario = salario * 1.05
    print(f'O salário antes do reajuste era {salario:.2f}, o percentual de aumento aplicado foi 05%, o valor do aumento foi de {salario * 0.05:.2f} e o novo salário é R${novosalario:.2f}')
        

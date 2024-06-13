valor_hora = float(input("Informe o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

desconto_ir = salario_bruto * 0.05
desconto_inss = salario_bruto * 0.10

fgts = salario_bruto * 0.11

total_descontos = desconto_ir + desconto_inss
salario_liquido = salario_bruto - total_descontos

print(f"\nSalário Bruto:\t\t\t ({valor_hora} * {horas_trabalhadas}) R$ {salario_bruto:.2f}")
print(f"(-) IR (5%)\t\t\t R$ {desconto_ir:.2f}")
print(f"(-) INSS (10%)\t\t\t R$ {desconto_inss:.2f}")
print(f"FGTS (11%)\t\t\t R$ {fgts:.2f}")
print(f"Desconto Total\t\t\t R$ {total_descontos:.2f}")
print(f"Salário Líquido\t\t\t R$ {salario_liquido:.2f}")

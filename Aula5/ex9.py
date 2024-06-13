contador = 0
impar = 0
par = 0 
somaimpar = 0
somapar = 0

while contador <= 9:
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        somapar += n
        par += 1 
    else:
        somaimpar += n
        impar += 1 
    contador += 1 

print(f'A Quantidade de números impares foi {impar} e a soma deu {somaimpar} \n de números pares a quantidade foi {par} e a soma foi {somapar}')
##1
##Função
def amplitude():
    listagem = []
    for x in range(1,5):
        print('-----------')
        x = input('Valor:')
        listagem.append(x)
    maior = max(listagem)
    menor = min(listagem)
    resultado = int(maior) - int(menor)

    print('A diferença entre os valores digitados é: ' + str(resultado))

##Teste

print('Insira os valors para verificar a diferença entre eles!')
amplitude()

##2
def nome(x):
    x = input('Por favor escreva seu nome: ')
    for y in x:
        print(y)

nome('Rafael')

##3

carga = input('Insira o valor da carga: ')

if int(carga) < 10:
    print('Valor da Carga é R$50,00')
if (int(carga) > 11 and int(carga) < 20):
    print('Valor da Carga é R$80,00')
if int(carga) > 20:
    print('Transporte não aceito')
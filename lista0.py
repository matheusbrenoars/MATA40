import random
#Funções
def ord_listDEC(tamanho, x1, x2):
    l2 = []
    for c in range(0, tamanho):
        n = random.randint(x1, x2)
        if c == 0 or n < l2[len(l2) - 1]:#mudei
            l2.append(n)
        else:
            p = 0
            while p < len(l2):
                if n >= l2[p]:#mudei
                    l2.insert(p, n)
                    break
                p += 1
    return l2

def ord_listCres(tamanho, x1, x2):
    l2 = []
    for c in range(0, tamanho):
        n = random.randint(x1, x2)
        if c == 0 or n > l2[len(l2) - 1]:
            l2.append(n)
        else:
            p = 0
            while p < len(l2):
                if n <= l2[p]:
                    l2.insert(p, n)
                    break
                p += 1
    return l2

def media_ar(lista):
    soma = 0
    for c in range(len(lista)):
        soma += lista[c]
    return soma / len(lista)

def var(lista):
    soma = 0
    for c in range(len(lista)):
        soma = soma +((lista[c]-media_ar(lista))**2)/len(lista)
    return soma

def d_pad(lista):
    import math
    return math.sqrt(var(lista))

def soma_salto(salto, lista):
  soma = 0
  controle = 0
  while controle < len(lista):
    soma+= lista[0+controle]
    controle+=salto +1
  return soma

def list_invertida(lista):
    n = len(lista)
    for i in range(n//2):
        temp = lista[i]
        lista[i] = lista[n-i-1]
        lista[n-i-1] = temp
    return lista

def troca(lista):
  for c in range(len(lista)):
    if c % 2==0 and lista[c] % 2 == 0:
      lista[c]= -1
    elif c % 2 ==1 and lista[c] % 2 ==1:
      lista[c] = 1
  return lista

#entradas
x, a, b = map(int, input(' quantidade de numeros, começo do intervalo, fim do intervalo ').split())
ord = input('Qual a ordem? Crescente= C / Decrescente = D: ')
z = int(input(' O que deseja calcular? Aperte: (1)Media (2)Variancia (3)Desvio padrão: '))
list_cresc = ord_listCres(x, a, b)
list_dec = ord_listDEC(x , a, b)

#ordenação
if x<=0:
    print('Entrada Inválida: o número de elemnetos não pode ser negativo ou nulo')

elif ord == 'C':
    print(list_cresc)
    if z ==1:
        print('Média:',media_ar(list_cresc))
    elif z ==2:
        print('Variancia:', var(list_cresc))
    elif z == 3:
        print('Desvio padrão:', d_pad(list_cresc))
    else:
        print('Comando inválido')


elif ord == 'D':
    print(list_dec)

    if z == 1:
        print('Média:', media_ar(list_dec))
    elif z == 2:
        print('Variancia:', var(list_dec))
    elif z == 3:
        print('Desvio padraão:', d_pad(list_dec))
    else:
        print('Comando inválido')

else:
    print('Inválido, digite C para ordem crescente ou D para ordem decrescente')

m = int(input('(1)Soma com um salto (2)Inverter os elemntos ou (3)Elemento e índice par = -1 ou elemento e indice impar = 1 :'))


if m == 1:
    salt = int(input('Qual o salto? Lembre-se que o salto deve ser menor que o tamanho da lista: '))

    if ord == 'C':
        print('Soma = ', soma_salto(salt, list_cresc))
        if salt >=x:
            print('Inválido')

    elif ord == 'D':
        print('Soma = ', soma_salto(salt, list_dec))
        if salt >=x:
            print('Inválido')
    else:
        print('inválido')

elif m ==2:
    if ord == 'C':
        print(list_invertida(list_cresc))

    elif ord == 'D':
        print( list_invertida(list_dec))

    else:
        print('invalido')

elif m ==3:
    if ord == 'C':
        print(troca(list_cresc))
    elif ord == 'D':
        print(troca(list_dec))
    else:
        print('inválido')

else:
    print('Operação não existente')









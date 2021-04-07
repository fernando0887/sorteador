import random
import os

print('-----Sorteomêtro-----')

menu = int(input('''Escolha a modalidade para a geração aleatória:
1 - Mega sena 
2 - Lotomania 
3 - Lotofácil  
4 - Sorteio por nome (5 participantes)
5 - Sorteio por nome (10 participantes) 
0 - Sair
Insira a opção desejada:   '''))


if  menu == 1:
    mega_sena = random.sample(range(0, 61), 6)
    print('Números gerados: ', mega_sena)

elif menu == 2:
    lotomania = random.sample(range(0, 101), 20)
    print('Números gerados: ', lotomania)

elif menu == 3:
    lotofacil = random.sample(range(0, 26), 15)
    print('Números gerados: ', lotofacil)

elif menu == 4:
    nomes = {}
    nomes_2 = {}
    nomes_3 = {}
    nomes_4 = {}
    nome_5 = {}


    p_1 = str(input('Insira o nome dos participante 1:'))
    p_2 = str(input('Insira o nome do participante 2: '))
    p_3 = str(input('Insira o nome do participante 3: '))
    p_4 = str(input('Insira o nome do participante 4: '))
    p_5 = str(input('Insira o nome do participante 5: '))

    nomes.update({len(nomes): p_1})
    nomes_2.update({len(nomes_2): p_2})
    nomes_3.update({len(nomes_3): p_3})
    nomes_4. update({len(nomes_4): p_4})
    nome_5.update({len(nome_5): p_5})

    lista = [nomes,nomes_2,nomes_3,nomes_4,nome_5]

    n = random.choice(lista)

    print('O nome sorteado foi: ', n)

elif menu == 5:
    nomes = {}
    nomes_2 = {}
    nomes_3 = {}
    nomes_4 = {}
    nome_5 = {}
    nomes_6 = {}
    nomes_7 = {}
    nomes_8 = {}
    nomes_9 = {}
    nome_10 = {}

    p_1 = str(input('Insira o nome dos participante 1:'))
    p_2 = str(input('Insira o nome do participante 2: '))
    p_3 = str(input('Insira o nome do participante 3: '))
    p_4 = str(input('Insira o nome do participante 4: '))
    p_5 = str(input('Insira o nome do participante 5: '))
    p_6 = str(input('Insira o nome dos participante 6:'))
    p_7 = str(input('Insira o nome do participante 7: '))
    p_8 = str(input('Insira o nome do participante 8: '))
    p_9 = str(input('Insira o nome do participante 9: '))
    p_10 = str(input('Insira o nome do participante 10: '))

    nomes.update({len(nomes): p_1})
    nomes_2.update({len(nomes_2): p_2})
    nomes_3.update({len(nomes_3): p_3})
    nomes_4.update({len(nomes_4): p_4})
    nome_5.update({len(nome_5): p_5})
    nomes_6.update({len(nomes): p_6})
    nomes_7.update({len(nomes_2): p_7})
    nomes_8.update({len(nomes_3): p_8})
    nomes_9.update({len(nomes_4): p_9})
    nome_10.update({len(nome_5): p_10})

    lista = [nomes, nomes_2, nomes_3, nomes_4, nome_5, nomes_6, nomes_7, nomes_8, nomes_9, nome_10]

    n = random.choice(lista)
    print('O nome sorteado foi: ', n)



elif menu == 0:
    os.system('cls')


else:
    print('opção inválida')

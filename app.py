#criando a lista de coisas
listaDeCoisas = []
item = input("Digite um item da lista: ")
listaDeCoisas.append(item)
while item != '0':
  item = input("Digite um item da lista (Digite 0 para sair): ")
  listaDeCoisas.append(item)
listaDeCoisas.remove('0')

#criação das listas de pontuação e controle
pontuacao = []
controle = []

#inserindo valor 0 para todos os itens da lista de coisas
for i in listaDeCoisas:
  pontuacao.append(int(0))

for indice, i in enumerate(listaDeCoisas):
  for index, j in enumerate(listaDeCoisas):
    if i == j or j in controle: #controle de duplicatas e itens já avaliados
      continue
    else:
      print(f"Você prefere {i} (Aperte 1) ou {j} (Aperte 2)?")
      k = int(input())
      if k not in (1,2):
        k = int(input("Digite 1 ou 2"))
      else:
        if k == 1:
          pontuacao[indice] += 3
          pontuacao[index] += 1
        else:
          pontuacao[index] += 3
          pontuacao[indice] += 1
  controle.append(i)

# juntando as duas listas
lista_combinada = list(zip(pontuacao, listaDeCoisas))

lista_combinada.sort(reverse=True)

#imprimindo a lista ordenada
for linha in lista_combinada:
  for elemento in linha:
    print(elemento, end=" ")
  print()

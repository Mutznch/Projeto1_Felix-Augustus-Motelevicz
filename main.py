#TRABALHO 1 - CONJUNTOS, Félix Augustus Motelevicz

#Abre e lê arquivos de texto, criando uma lista onde cada linha é um elemento tipo string.
with open("teste.txt") as f:
  texto = f.readlines()

numeroOperacoes = int(texto[0]) #Define o número de operações baseado na primeira linha do texto.
linha = 1 #Variável que identifica a linha à ser lida.
#Variáveis para ajudar na formatação.
L = "{"
R = "}"
# Função que lê uma linha e transforma os elementos em uma lista, removendo vírgulas, espaços e "\n".
def lista():
  numero = ""
  x = []
  for i in texto[linha]:
    if i != "," and i != "\n" and i != " ":
      numero += i
    else:
      if numero != "":
        x.append(numero)
        numero = ""
  return x
#Laço de repetição que realiza as operações.
for i in range(numeroOperacoes):
  operacao = texto[linha][0] #Identifica qual operação será realizada.
#Cria uma lista com os elementos do primeiro conjunto.
  linha += 1
  A = lista()
#Cria uma lista com os elementos do segundo conjunto.
  linha += 1
  B = lista()
  
  soma = A + B #Junta os conjuntos em um (utilizado em algumas operações).
#Transforma os conjuntos em uma string separando os elementos com vírgula.
  conjunto1 = ",".join(A)
  conjunto2 = ",".join(B)
  
  resultado = [] #Utilizado em algumas operações.
#Realiza a operação União.
  if operacao == "U":
    resultado = ",".join(list(dict.fromkeys(soma))) #Retira elementos repetidos e transforma tudo em uma string separando os elementos com vírgula.
    operacao = "União" #Variável para ajudar na formatação.
#Realiza a operação Interseção.
  elif operacao == "I":
#Laço que adiciona elementos iguais dos conjuntos em uma lista.
    for j in soma:
      if soma.count(j) > 1:
        resultado.append(j)

    resultado = ",".join(list(dict.fromkeys(resultado))) #Transforma tudo em uma string separando os elementos com vírgula.
    operacao = "Interseção" #Variável para ajudar na formatação.
#Realiza a operação Diferença.
  elif operacao == "D":
#Retira elementos do conjunto 1 que também estão no conjunto 2.
    for j in range(len(A)):
      if soma.count(A[j]) > 1:
        del A[j]
        A.insert(j,"")
    resultado = list(dict.fromkeys(A))
    resultado.remove("")

    resultado = ",".join(resultado) #Transforma tudo em uma string separando os elementos com vírgula.
    operacao = "Diferença" #Variável para ajudar na formatação.
#Realiza a operação Produto Cartesiano.
  else:
#Cria pares dos os elementos do conjunto 1 com o 2.
    for k in B:
      for j in A:
        resultado.append("("+j+","+k+")")

    resultado = ",".join(resultado)#Transforma tudo em uma string separando os elementos com vírgula.
    operacao = "Produto Cartesiano" #Variável para ajudar na formatação.
#Imprime as operações, conjuntos e o resultado no terminal.
  print(f"{operacao}: conjunto 1 {L+conjunto1+R}, conjunto 2 {L+conjunto2+R}. Resultado: {L+resultado+R}")
  linha += 1 #Variável que identifica a próxima linha à ser lida.
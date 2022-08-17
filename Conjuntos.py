#Joao Pedro Aires de Siqueira
#Basicamente, ele pega o arquivo txt, transforma ele em um vetor, apos isso, separa os conjuntos  em um subvetores, transformando em uma matriz, pois assim é mais facil de trabalhar, apos isso faz as operaçoes de acordo com a letra encontrada no arquivo txt, depois disso, printa elemento por elemento, para que ele fique na formataçao correta(entre chaves) 
with open("file2.txt", "r") as arquivos:
    linhas = arquivos.readlines()
vet = []
for linha in linhas:
    formatador = linha.strip()
    vet.append(formatador)
vet.pop(0)
def transformar(a):
    lis = []
    char = ""
    for x in a:
        if not x == ",":
            char += x
        else:
            lis.append(char)
            char = ""
    lis.append(char)
    return lis

#Transformar - Transform sets in lists

for i in range(1, len(vet), 3):
    vet[i] = transformar(vet[i])
    vet[i + 1] = transformar(vet[i + 1])


def uniao(a, b):
    resposta = []
    for i in a:
        if not i in resposta:
            resposta.append(i)
    for i in b:
        if not i in resposta:
            resposta.append(i)
    return resposta

def intercecao(a, b):
    resposta = []
    for i in a:
        for j in b:
            if i == j:
                resposta.append(i)
    return resposta


def dif(a, b):
    resposta = []
    for i in a:
        if not i in b:
            resposta.append(i)
    for i in b:
        if not i in a:
            resposta.append(i)
    return resposta


def Cartesian(a, b):
    resposta = []
    banana = []
    for i in a:
        for j in b:
            banana.append(i)
            banana.append(j)
            resposta.append(banana)
            banana = []
    return resposta

def summary(res, nome):
    print(f"{nome}: Conjunto 1","{ ", end="")
    for i in range(0, len(vet[x + 1]) - 1):
        print(f"{vet[x + 1][i]},", end="")
    print(vet[x + 1][len(vet[x + 1]) - 1],"}", end=" ")
    print("Conjunto 2: {", end=" ")
    for i in range(0, len(vet[x + 2]) - 1):
        print(f"{vet[x + 2][i]},", end="")
    print(vet[x + 2][len(vet[x + 2]) - 1], "}", end=" ")
    print("Resposta: { ", end="")
    for i in range(0, len(res) - 1):
        print(f"{res[i]},", end="")
    print(res[len(res) - 1], "}")

for x in range(0, len(vet), 3):
    if vet[x] == "U":
        resposta = uniao(vet[x + 1], vet[x + 2])
        summary(resposta, "União")
    elif vet[x] == "I":
        resposta = intercecao(vet[x + 1], vet[x + 2])
        summary(resposta, "Interceção")
    elif vet[x] == "D":
        resposta = dif(vet[x + 1], vet[x + 2])
        summary(resposta, "Diferença")
    elif vet[x] == "C":
        resposta = Cartesian(vet[x + 1], vet[x + 2])
        print("Cartesiano: Conjunto 1: { ", end=" ")
        for i in range(0, len(vet[x + 1]) - 1):
            print(f"{vet[x + 1][i]}, ", end="")
        print(vet[x + 1][len(vet[x + 1]) - 1], "}", end=" ")
        print("Conjunto 2: { ", end=" ")
        for i in range(0, len(vet[x + 2]) - 1):
            print(f"{vet[x + 2][i]}, ", end="")
        print(vet[x + 2][len(vet[x + 2]) - 1], "}", end=" ")
        print("Resposta: {(", end="")
        for i in range(0, len(resposta) - 1):
            print(resposta[i][0], end=",")
            print(resposta[i][1], end="), (")
        print(resposta[len(resposta) - 1][len(resposta[len(resposta) - 1]) - 2], end=",")
        print(resposta[len(resposta) - 1][len(resposta[len(resposta) - 1]) - 1], end=")}")

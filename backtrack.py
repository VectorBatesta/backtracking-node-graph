def BUSCA_RETROCESSO(G, inicial, objetivo):
    LE = [inicial]
    LNE = [inicial]
    BSS = [] #Inicialização

    EC = inicial #Estado corrente

    while LNE != None: #não está vazio, LNE != [ ]
        if EC == objetivo: #objetivo = nó do objetivo indicado
            return LE #Se houver sucesso, retorna a lista de estados no caminho

        if not G[EC]: #se nao tem filhos
            while LE != None and EC == LE[0]: # != None quer dizer não vazio
                BSS.append(EC)
                LE.pop(0) #remove primeiro de LE
                LNE.pop(0) #remove primeiro de LNE
                EC = LNE[0]
            LE.append(EC)
        else:
            #linha abaixo pego do google
            filhos = [child for child in G[EC] if child not in BSS + LE + LNE]
            LNE = filhos + LNE
            #/\ Exceto os já em BSS, LE ou LNE

            EC = LNE[0] #primeiro elemento da LNE
            LNE.pop(0)
            LE.append(EC) #acrescenta EC a LE;
    return "FALHA"

#grafo mostrado no pdf da aula
G = {
    'A': {'B': 100, 'C': 125, 'D': 100, 'E': 75},
    'B': {'A': 100, 'E': 125, 'D': 75, 'C': 50},
    'C': {'B': 50, 'A': 125, 'E': 125, 'D': 100},
    'D': {'E': 50, 'A': 100, 'B': 75, 'C': 100},
    'E': {'A': 75, 'B': 125, 'C': 125, 'D': 50}
}

print("Caminho final:", BUSCA_RETROCESSO(G, 'A', 'D'))
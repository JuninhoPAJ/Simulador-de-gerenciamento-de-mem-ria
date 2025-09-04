def encontrar_espacos_livres(memoria):
    livres = []
    inicio = None
    for i, bloco in enumerate(memoria):
        if bloco is None:
            if inicio is None:
                inicio = i
        else:
            if inicio is not None:
                livres.append((inicio, i - inicio))
                inicio = None
    if inicio is not None:
        livres.append((inicio, len(memoria) - inicio))
    return livres

def first_fit(memoria, blocos_necessarios):
    espacos = encontrar_espacos_livres(memoria)
    for inicio, tamanho in espacos:
        if tamanho >= blocos_necessarios:
            return inicio
    return None

def best_fit(memoria, blocos_necessarios):
    espacos = encontrar_espacos_livres(memoria)
    melhor = None
    for inicio, tamanho in espacos:
        if tamanho >= blocos_necessarios:
            if melhor is None or tamanho < melhor[1]:
                melhor = (inicio, tamanho)
    return melhor[0] if melhor else None

def worst_fit(memoria, blocos_necessarios):
    espacos = encontrar_espacos_livres(memoria)
    pior = None
    for inicio, tamanho in espacos:
        if tamanho >= blocos_necessarios:
            if pior is None or tamanho > pior[1]:
                pior = (inicio, tamanho)
    return pior[0] if pior else None

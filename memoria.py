class Memoria:
    def __init__(self):
        self.tamanho_total = 128  # em KB
        self.bloco_tamanho = 2    # em KB
        self.num_blocos = self.tamanho_total // self.bloco_tamanho
        self.blocos = [None] * self.num_blocos  # memória inicial vazia
        self.processos_ativos = []  # Lista FIFO: [(nome, tamanho)]

    def alocar(self, processo, algoritmo):
        blocos_necessarios = processo.tamanho // self.bloco_tamanho
        posicao = algoritmo(self.blocos, blocos_necessarios)

        if posicao is not None:
            for i in range(posicao, posicao + blocos_necessarios):
                self.blocos[i] = processo.nome
            self.processos_ativos.append((processo.nome, processo.tamanho))
            print(
                f"Processo {processo.nome} alocado com sucesso "
                f"nos blocos {posicao + 1} até {posicao + blocos_necessarios }."
            )
            return True
        else:
            return False

    def desalocar(self, nome_processo):
        desalocados = 0
        for i in range(len(self.blocos)):
            if self.blocos[i] == nome_processo:
                self.blocos[i] = None
                desalocados += 1

        self.processos_ativos = [
            (nome, tamanho) for nome, tamanho in self.processos_ativos if nome != nome_processo
        ]

        print(f"Desalocados {desalocados} blocos do processo {nome_processo}.")

    def remover_processo_mais_antigo(self):
        if self.processos_ativos:
            nome, _ = self.processos_ativos.pop(0)
            self.desalocar(nome)
        else:
            print("Nenhum processo para remover.")

    def tem_processos_ativos(self):
        return len(self.processos_ativos) > 0

    def mostrar_processos_ativos(self):
        print("\n Processos ativos na memória:")
        if self.processos_ativos:
            for idx, (nome, tamanho) in enumerate(self.processos_ativos, start=1):
                print(f"{idx}. {nome} ({tamanho} KB)")
        else:
            print("Nenhum processo alocado.")

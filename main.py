from memoria import Memoria
from processo import Processo
from algoritmos import first_fit, best_fit, worst_fit

def menu():
    print("\n=== Simulador de Gerenciamento de Memória ===")
    print("1. Adicionar processo")
    print("2. Remover processo")
    print("3. Mostrar processos ativos")
    print("4. Sair")
    return input("Escolha uma opção: ")

def escolher_algoritmo():
    print("\nAlgoritmos disponíveis:")
    print("1. First Fit")
    print("2. Best Fit")
    print("3. Worst Fit")
    escolha = input("Escolha o algoritmo de alocação: ")
    if escolha == "1":
        return first_fit
    elif escolha == "2":
        return best_fit
    elif escolha == "3":
        return worst_fit
    else:
        print("Algoritmo inválido.")
        return escolher_algoritmo()

def main():
    memoria = Memoria()
    algoritmo = escolher_algoritmo()

    while True:
        opcao = menu()

        if opcao == "1":
            nome = input("Nome do processo: ")
            tamanho = int(input("Tamanho do processo (em KB): "))
            processo = Processo(nome, tamanho)

            # Tenta alocar, e força remoções até conseguir
            sucesso = memoria.alocar(processo, algoritmo)
            while not sucesso and memoria.tem_processos_ativos():
                print("Memória cheia. Removendo processo mais antigo (FIFO)...")
                memoria.remover_processo_mais_antigo()
                sucesso = memoria.alocar(processo, algoritmo)

            if not sucesso:
                print("Erro: processo grande demais para ser alocado mesmo com memória limpa.")

            memoria.mostrar_processos_ativos()

        elif opcao == "2":
            nome = input("Nome do processo a remover: ")
            memoria.desalocar(nome)
            memoria.mostrar_processos_ativos()

        elif opcao == "3":
            memoria.mostrar_processos_ativos()

        elif opcao == "4":
            print("Encerrando simulador...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

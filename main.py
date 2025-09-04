from memoria import Memoria
from processo import Processo
from algoritmos import first_fit, best_fit, worst_fit

from memoria import Memoria
from processo import Processo
from algoritmos import first_fit, best_fit, worst_fit

# Dicionário para exibir o nome do algoritmo
NOMES_ALGORITMOS = {
    first_fit: "First Fit",
    best_fit: "Best Fit",
    worst_fit: "Worst Fit"
}

def menu(algoritmo_atual):
    print("\n=== Simulador de Gerenciamento de Memória ===")
    print(f"Algoritmo atual: {NOMES_ALGORITMOS[algoritmo_atual]}")
    print("1. Adicionar processo")
    print("2. Remover processo")
    print("3. Mostrar processos ativos")
    print("4. Trocar algoritmo de alocação")
    print("5. Sair")
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
        opcao = menu(algoritmo)

        if opcao == "1":
            nome = input("Nome do processo: ")
            tamanho = int(input("Tamanho do processo (em KB): "))
            processo = Processo(nome, tamanho)

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
            algoritmo = escolher_algoritmo()
            print("Algoritmo trocado com sucesso.")

        elif opcao == "5":
            print("Encerrando simulador...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()

Introdução

Simulador de Gerenciamento de memória, desenvolvido em Python, que tem o objetivo de demonstrar o comportamento desses 3 algoritmos escolhidos, First Fit, Best Fit e Worst Fit. Esse projeto permite alocar e desalocar processos de acordo com as necessidades do usuário. 
Caso a memória atinja sua capacidade máxima, usa o algoritmo FIFO(First In, First Out).
Objetivo

O objetivo do projeto foi a alocação de processos na memória, em blocos fixos de 2 KB cada, onde o total da memória foi de 128 KB, aplicando os três algoritmos:


First Fit: Nesse algoritmo, ele se aloca no primeiro espaço da memória livre suficiente.

Vantagens: Ele é rápido, pois para na primeira opção adequada.
Desvantagens: Pode deixar espaços pequenos não utilizados.

Best Fit: Nesse algoritmo, procura o menor espaço possível na memória, que seja suficiente para o processo.

Vantagens: Pode usar a memória de forma mais eficiente.
Desvantagens: Ele é mais lento, pois precisa percorrer a lista inteira, podendo deixar muitos espaços muito pequenos.

Worst Fit: Nesse algoritmo, aloca o processo no maior espaço livre disponível. 

Vantagens: Tende a deixar espaços razoáveis para futuros processos.
Desvantagens: Pode-se desperdiçar espaços grandes com processos pequenos.

FIFO(First in, First Out): É um algoritmo que descreve um método de processamento ou armazenamento, onde o primeiro item a ser processado é o primeiro a ser removido. Esse algoritmo faz a substituição, em que o primeiro processo que entrou na memória, é o primeiro a ser removido quando a memória estiver cheia.


Modo de Execução do Projeto

O Projeto tem quatro arquivos: algoritmos.py, memoria.py, processo.py, e o main.py, sendo esse o principal arquivo para a execução dos arquivos.


VS Code: Com todos os arquivos abertos no VS Code, abre um novo terminal e executa o comando python main.py

PyCharm: Com o arquivo main.py, deve clicar com o botão direito no arquivo e selecionar Run ‘app’, ouclicar no icone verde no canto superior direito

O projeto possui um menu que permite ao usuário:

Adicionar processo.


Remover processo.


Mostrar processos ativos.


Trocar o algoritmo de alocação.

Sair.

Regras de Alocação
Tamanho dos blocos: Cada processo deve ser alocado em blocos de 2 KB. Se um processo precisar de 10KB, ele usará 5 blocos. 

Política de substituição: Quando não há espaço suficiente, o processo mais antigo é removido. Isso simula uma fila FIFO de processos.

Exemplos de como o algoritmo funciona:
	

Para iniciar outro exemplo, certifique-se que a memória esteja sempre vazia!


First Fit:


1. Adiciona processo A com 10 KB, que vai ficar nos blocos 1 ao 5


2. Adiciona processo B com 20 KB, que vai ficar nos blocos 6 ao 15


3. Remove processo A, liberando os blocos 1 ao 5


4. Adiciona processo C com 5 KB, que vai ficar nos blocos 1 ao 2


5. Adiciona processo D com 10 KB, que vai ficar nos blocos 16 ao 20


6. Adiciona processo E com 2 KB, que vai ficar no bloco 3







Best Fit: 

1. Adiciona processo A com 60 KB, que vai ficar nos blocos 1 ao 30


2. Adiciona processo B com 66 KB, que vai ficar nos blocos 31 ao 63


- Sobra apenas o bloco 64 livre (2 KB) → espaço pequeno no fim da memória


3. Remove processo A, liberando os blocos 1 ao 30


4. Adiciona processo C com 2 KB, que vai ficar no bloco 64 (menor espaço livre disponível)

Worst Fit: 

1. Adiciona processo A com 10 KB, que vai ficar nos blocos 1 ao 5


2. Adiciona processo B com 20 KB, que vai ficar nos blocos 6 ao 15


3. Adiciona processo C com 12 KB, que vai ficar nos blocos 16 ao 21


4. Remove processo A, liberando os blocos 1 ao 5


5. Adiciona processo D com 8 KB, que vai ficar nos blocos 22 ao 25 (pior espaço livre é o final da memória)

FIFO: 

1. Adiciona processo A com 60 KB, que vai ficar nos blocos 1 ao 30


2. Adiciona processo B com 60 KB, que vai ficar nos blocos 31 ao 60


- Tenta adicionar processo C com 60 KB, mas não há espaço suficiente (apenas blocos 61 ao 64 livres)


- Remove processo A, liberando os blocos 1 ao 30 (FIFO)


3. Adiciona processo C com 60 KB, que vai ficar nos blocos 1 ao 30

# Sistema Bancário Simples

Este projeto implementa um sistema bancário simples em Python que permite ao usuário realizar as seguintes operações:

- Depósitos
- Saques (com limite de saques e valor)
- Visualização de extrato
- Sair do programa

## Funcionalidades

O sistema oferece um menu interativo com quatro opções principais:

1. **Depósito:** O usuário pode inserir um valor positivo, que será adicionado ao saldo.
2. **Saque:** O usuário pode sacar um valor, desde que tenha saldo disponível, respeitando o limite por saque e o número máximo de saques diários.
3. **Extrato:** Mostra um histórico das movimentações realizadas (depósitos e saques) e o saldo atual.
4. **Sair:** Encerra o programa.

### Regras de Negócio

- O **saldo** é atualizado após cada depósito ou saque.
- O **limite** de saque por transação é de R$ 500,00.
- O número de saques diários é limitado a **3**.
- O extrato exibe as transações realizadas e o saldo atualizado.

## Aprendizado

Aprender com este projeto foi uma experiência rica, pois ele aborda alguns conceitos essenciais da programação, como:

- **Manipulação de variáveis:** Através do controle do saldo, limite, e extrato.
- **Controle de fluxo:** Utilizando estruturas de repetição (`while`) e seleção (`if-elif-else`), aprendi como direcionar o fluxo do programa com base nas escolhas do usuário.
- **Manipulação de strings:** O uso da variável `extrato` para armazenar as transações em formato de texto me ensinou a concatenar strings de maneira eficiente e apresentar dados de forma legível.
- **Interação com o usuário:** Trabalhar com entradas (`input`) e validar dados (como valores negativos) reforçou a importância da experiência do usuário e da robustez do código.

## Como usar

Para executar o sistema bancário, basta rodar o script em um ambiente Python. O menu será exibido e você poderá interagir com o sistema realizando as operações bancárias disponíveis.

### Exemplo de uso:

```bash
========MENU========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> 1
Informe o valor do depósito: R$ 1000

========MENU========
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> 3

========== EXTRATO ==========
Depósito: R$ 1000.00

Saldo atual: R$ 1000.00
=============================

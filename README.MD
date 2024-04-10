# Documentação do Código da Biblioteca

Este documento oferece uma visão geral e documentação detalhada do código Python que implementa um sistema de biblioteca simples, incluindo a estrutura de dados para armazenar o acervo, classes para operações de empréstimo e devolução, bem como um menu interativo para interação do usuário.

## Estrutura do Código

O código consiste em várias classes e métodos para gerenciar o acervo da biblioteca, realizar operações de empréstimo e devolução, e fornecer uma interface de usuário para interação com o sistema. As principais classes incluem:

1. `NoArvore`: Representa um nó na árvore binária de busca que armazena informações sobre um livro, como título, autor e número de exemplares.

2. `ArvoreBinaria`: Implementa uma árvore binária de busca para armazenar o acervo da biblioteca. Fornece métodos para inserir e buscar livros na árvore.

3. `FilaEmprestimo`: Implementa uma fila para gerenciar solicitações de empréstimo de livros.

4. `PilhaDevolucao`: Implementa uma pilha para gerenciar devoluções de livros.

5. `Biblioteca`: Representa a biblioteca como um todo e oferece métodos para cadastrar livros, consultar o acervo, solicitar empréstimos, processar empréstimos, devolver livros e processar devoluções.

6. `menu`: Um método que fornece um menu interativo para o usuário interagir com o sistema.

## Funcionalidades Principais

### Cadastrar Livro

-   Permite cadastrar novos livros no acervo da biblioteca, incluindo título, autor e número de exemplares.

### Consultar Acervo

-   Permite buscar livros no acervo da biblioteca por título e exibe informações sobre o livro, como autor e disponibilidade de exemplares.

### Solicitar Empréstimo

-   Permite solicitar o empréstimo de um livro do acervo. Se o livro estiver disponível, reduz o número de exemplares disponíveis e adiciona o título à fila de empréstimo.

### Processar Empréstimo

-   Realiza o empréstimo de um livro da fila de empréstimo, se houver solicitações pendentes.

### Devolver Livro

-   Permite ao usuário devolver um livro emprestado. Aumenta o número de exemplares disponíveis para o livro devolvido.

### Processar Devolução

-   Processa todas as devoluções pendentes na pilha de devolução, aumentando o número de exemplares disponíveis para cada livro devolvido.

### Menu Interativo

-   Fornece uma interface de usuário simples com um menu de opções para interagir com as funcionalidades da biblioteca.

## Uso do Código

Para utilizar o código, basta executar o script Python `biblioteca.py`. Isso iniciará o programa e exibirá o menu interativo. O usuário pode então selecionar as opções desejadas para interagir com o sistema de biblioteca.

## Considerações Finais

Este código fornece uma implementação básica de um sistema de biblioteca em Python, demonstrando o uso de estruturas de dados como árvores binárias e filas, bem como a construção de uma interface de usuário simples. Ele pode ser estendido e aprimorado para adicionar mais funcionalidades e recursos, conforme necessário.

# Biblioteca

Este é um sistema simples de biblioteca implementado em Python. Ele permite cadastrar livros, consultar o acervo, solicitar empréstimos, processar empréstimos e devolver livros.

## Classes

### `NoArvore`

Representa um nó de uma árvore binária. Cada nó possui informações sobre um livro, incluindo título, autor e quantidade de exemplares, bem como referências para os nós filhos esquerdo e direito.

-   **Métodos:**
    -   `__init__(self, titulo, autor, exemplares)`: Inicializa um nó com o título, autor e quantidade de exemplares especificados.

### `ArvoreBinaria`

Implementa uma árvore binária de busca para armazenar os livros do acervo da biblioteca.

-   **Métodos:**
    -   `__init__(self)`: Inicializa a árvore binária.
    -   `inserir(self, titulo, autor, exemplares)`: Insere um novo livro na árvore.
    -   `_inserir_recursivo(self, novo_no, no_atual)`: Método auxiliar para inserção recursiva de um novo nó na árvore.
    -   `buscar(self, titulo)`: Busca por um livro na árvore.
    -   `_buscar_recursivo(self, titulo, no_atual)`: Método auxiliar para busca recursiva de um livro na árvore.

### `FilaEmprestimo`

Implementa uma fila para gerenciar os pedidos de empréstimo de livros.

-   **Métodos:**
    -   `__init__(self)`: Inicializa a fila.
    -   `adicionar(self, titulo)`: Adiciona um título à fila.
    -   `remover(self)`: Remove e retorna o título na frente da fila.
    -   `esta_vazia(self)`: Verifica se a fila está vazia.

### `PilhaDevolucao`

Implementa uma pilha para gerenciar os livros devolvidos.

-   **Métodos:**
    -   `__init__(self)`: Inicializa a pilha.
    -   `adicionar(self, titulo)`: Adiciona um título à pilha.
    -   `remover(self)`: Remove e retorna o título no topo da pilha.
    -   `esta_vazia(self)`: Verifica se a pilha está vazia.

### `Biblioteca`

Representa a biblioteca como um todo, incluindo o acervo de livros, a fila de empréstimos e a pilha de devoluções.

-   **Métodos:**
    -   `__init__(self)`: Inicializa a biblioteca com uma árvore binária vazia, uma fila de empréstimos vazia e uma pilha de devoluções vazia.
    -   `cadastrar_livro(self, titulo, autor, exemplares)`: Registra um novo livro no acervo.
    -   `consultar_acervo(self, titulo)`: Consulta o acervo em busca de um livro específico.
    -   `solicitar_emprestimo(self, titulo)`: Solicita o empréstimo de um livro do acervo.
    -   `processar_emprestimo(self)`: Processa um empréstimo da fila de empréstimos.
    -   `devolver_livro(self, titulo)`: Registra a devolução de um livro e o retorna ao acervo.
    -   `menu(self)`: Exibe um menu interativo para interação com o sistema.

## Uso

Para usar o sistema, execute o arquivo e siga as instruções exibidas no menu.

Exemplo de uso:

```python
if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.menu()
```

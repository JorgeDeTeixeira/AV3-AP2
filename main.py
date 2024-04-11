from collections import deque


class NoArvore:
    def __init__(self, titulo, autor, exemplares):
        self.titulo = titulo
        self.autor = autor
        self.exemplares = exemplares
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, titulo, autor, exemplares):
        if exemplares < 1:
            raise ValueError("O número de exemplares deve ser um inteiro positivo.")
        novo_no = NoArvore(titulo, autor, exemplares)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(novo_no, self.raiz)

    def _inserir_recursivo(self, novo_no, no_atual):
        if novo_no.titulo == no_atual.titulo:
            raise ValueError("Livro com título duplicado.")
        elif novo_no.titulo < no_atual.titulo:
            if no_atual.esquerda is None:
                no_atual.esquerda = novo_no
            else:
                self._inserir_recursivo(novo_no, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = novo_no
            else:
                self._inserir_recursivo(novo_no, no_atual.direita)

    def buscar(self, titulo):
        return self._buscar_recursivo(titulo, self.raiz)

    def _buscar_recursivo(self, titulo, no_atual):
        if no_atual is None:
            return None
        elif titulo == no_atual.titulo:
            return no_atual
        elif titulo < no_atual.titulo:
            return self._buscar_recursivo(titulo, no_atual.esquerda)
        else:
            return self._buscar_recursivo(titulo, no_atual.direita)


class FilaEmprestimo:
    def __init__(self):
        self.fila = deque()

    def adicionar(self, titulo):
        self.fila.append(titulo)

    def remover(self):
        return self.fila.popleft()

    def esta_vazia(self):
        return len(self.fila) == 0


class PilhaDevolucao:
    def __init__(self):
        self.pilha = []

    def adicionar(self, titulo):
        self.pilha.append(titulo)

    def remover(self):
        return self.pilha.pop()

    def esta_vazia(self):
        return len(self.pilha) == 0


class Biblioteca:
    def __init__(self):
        self.acervo = ArvoreBinaria()
        self.fila_emprestimo = FilaEmprestimo()
        self.pilha_devolucao = PilhaDevolucao()

    def cadastrar_livro(self, titulo, autor, exemplares):
        self.acervo.inserir(titulo, autor, exemplares)
        print(f"O livro '{titulo}' foi cadastrado no acervo.")

    def consultar_acervo(self, titulo):
        livro = self.acervo.buscar(titulo)
        if livro is None:
            return f"Livro '{titulo}' não encontrado no acervo."
        else:
            disponibilidade = "disponível" if livro.exemplares > 0 else "indisponível"
            return f"Livro '{titulo}':\n- Autor: {livro.autor}\n- Exemplares disponíveis: {livro.exemplares} ({disponibilidade})"

    def solicitar_emprestimo(self, titulo):
        livro = self.acervo.buscar(titulo)
        if livro is None:
            print(f"Livro '{titulo}' não encontrado.")
        elif livro.exemplares == 0:
            print(f"Livro '{titulo}' não disponível para empréstimo.")
        else:
            livro.exemplares -= 1
            self.fila_emprestimo.adicionar(titulo)
            print(f"Empréstimo do livro '{titulo}' solicitado.")

    def processar_emprestimo(self):
        if not self.fila_emprestimo.esta_vazia():
            titulo = self.fila_emprestimo.remover()
            print(f"Empréstimo do livro '{titulo}' realizado.")
        else:
            print("Fila de empréstimos vazia.")

    def devolver_livro(self, titulo):
        if titulo not in self.fila_emprestimo.fila:
            print(f"Livro '{titulo}' não foi emprestado anteriormente.")
        else:
            self.fila_emprestimo.fila.remove(titulo)
            livro = self.acervo.buscar(titulo)
            if livro is not None:
                livro.exemplares += 1
                print(
                    f"Devolução do livro '{titulo}' processada. Exemplares disponíveis: {livro.exemplares}"
                )
            else:
                print(f"Erro: Livro '{titulo}' não encontrado no acervo.")

    def menu(self):
        while True:
            print("\nMenu da Biblioteca:")
            print("1. Cadastrar Livro")
            print("2. Consultar Acervo")
            print("3. Solicitar Empréstimo")
            print("4. Processar Empréstimo")
            print("5. Devolver Livro")
            print("6. Sair")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                titulo = input("Título do livro: ")
                autor = input("Autor do livro: ")
                exemplares = int(input("Quantidade de exemplares: "))
                self.cadastrar_livro(titulo, autor, exemplares)
            elif opcao == "2":
                titulo = input("Título do livro: ")
                print(self.consultar_acervo(titulo))
            elif opcao == "3":
                titulo = input("Título do livro para empréstimo: ")
                self.solicitar_emprestimo(titulo)
            elif opcao == "4":
                self.processar_emprestimo()
            elif opcao == "5":
                titulo = input("Título do livro a ser devolvido: ")
                self.devolver_livro(titulo)
            elif opcao == "6":
                print("OBRIGADO POR USAR NOSSO SISTEMA!")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.menu()

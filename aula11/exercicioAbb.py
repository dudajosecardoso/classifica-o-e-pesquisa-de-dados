class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.esquerda = None
        self.direita = None
        
class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, id, nome, descricao, preco):
        novo_produto = Produto(id, nome, descricao, preco)
        if self.raiz is None:
            self.raiz = novo_produto
        else:
            self._inserir_recursivo(self.raiz, novo_produto)

    def _inserir_recursivo(self, nodo, novo_produto):
        if novo_produto.id < nodo.id:
            if nodo.esquerda is None:
                nodo.esquerda = novo_produto
            else:
                self._inserir_recursivo(nodo.esquerda, novo_produto)
        else:
            if nodo.direita is None:
                nodo.direita = novo_produto
            else:
                self._inserir_recursivo(nodo.direita, novo_produto)

    def buscar(self, id):
        return self._buscar_recursivo(self.raiz, id)

    def _buscar_recursivo(self, nodo, id):
        if nodo is None or nodo.id == id:
            return nodo
        if id < nodo.id:
            return self._buscar_recursivo(nodo.esquerda, id)
        return self._buscar_recursivo(nodo.direita, id)

    def remover(self, id):
        self.raiz = self._remover_recursivo(self.raiz, id)

    def _remover_recursivo(self, nodo, id):
        if nodo is None:
            return nodo
        if id < nodo.id:
            nodo.esquerda = self._remover_recursivo(nodo.esquerda, id)
        elif id > nodo.id:
            nodo.direita = self._remover_recursivo(nodo.direita, id)
        else:
            if nodo.esquerda is None:
                return nodo.direita
            elif nodo.direita is None:
                return nodo.esquerda
            temp = self._minimo(nodo.direita)
            nodo.id = temp.id
            nodo.nome = temp.nome
            nodo.descricao = temp.descricao
            nodo.preco = temp.preco
            nodo.direita = self._remover_recursivo(nodo.direita, temp.id)
        return nodo

    def _minimo(self, nodo):
        atual = nodo
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def listar_em_ordem(self):
        return self._listar_em_ordem_recursivo(self.raiz)

    def _listar_em_ordem_recursivo(self, nodo):
        produtos = []
        if nodo:
            produtos += self._listar_em_ordem_recursivo(nodo.esquerda)
            produtos.append((nodo.id, nodo.nome, nodo.descricao, nodo.preco))
            produtos += self._listar_em_ordem_recursivo(nodo.direita)
        return produtos
        
arvore = ArvoreBinariaBusca()

arvore.inserir(30, "Produto A", "Descrição A", 100.0)
arvore.inserir(20, "Produto B", "Descrição B", 50.0)
arvore.inserir(40, "Produto C", "Descrição C", 150.0)

produto_buscado = arvore.buscar(20)
if produto_buscado:
    print(f"Produto encontrado: {produto_buscado.nome}, Preço: {produto_buscado.preco}")
else:
    print("Produto não encontrado.")

arvore.remover(20)
produtos_listados = arvore.listar_em_ordem()
print("Produtos em ordem crescente de ID:")
for produto in produtos_listados:
    print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[3]}")

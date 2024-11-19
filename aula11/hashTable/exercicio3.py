class Arquivo:
    def __init__(self, nome, caminho, tamanho):
        self.nome = nome
        self.caminho = caminho
        self.tamanho = tamanho
        self.proximo = None

class TabelaHash:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [None] * self.tamanho

    def funcao_hash(self, nome):
        return sum(ord(char) for char in nome) % self.tamanho

    def adicionar_arquivo(self, nome, caminho, tamanho):
        indice = self.funcao_hash(nome)
        novo_arquivo = Arquivo(nome, caminho, tamanho)

        if self.tabela[indice] is None:
            self.tabela[indice] = novo_arquivo
        else:
            atual = self.tabela[indice]
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_arquivo

    def buscar_arquivo(self, nome):
        indice = self.funcao_hash(nome)
        atual = self.tabela[indice]

        while atual is not None:
            if atual.nome == nome:
                return (atual.nome, atual.caminho, atual.tamanho)
            atual = atual.proximo
        return None

    def remover_arquivo(self, nome):
        indice = self.funcao_hash(nome)
        atual = self.tabela[indice]
        anterior = None

        while atual is not None:
            if atual.nome == nome:
                if anterior is None:
                    self.tabela[indice] = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def listar_arquivos(self):
        arquivos = []
        for lista in self.tabela:
            atual = lista
            while atual is not None:
                arquivos.append((atual.nome, atual.caminho, atual.tamanho))
                atual = atual.proximo
        return arquivos

tabela_hash = TabelaHash()

tabela_hash.adicionar_arquivo("relatorio.pdf", "/documentos/relatorio.pdf", 1024)
tabela_hash.adicionar_arquivo("foto.jpg", "/imagens/foto.jpg", 2048)
tabela_hash.adicionar_arquivo("dados.csv", "/planilhas/dados.csv", 512)
tabela_hash.adicionar_arquivo("backup.zip", "/backup/backup.zip", 4096)

info_dados = tabela_hash.buscar_arquivo("dados.csv")
print("Informações do arquivo 'dados.csv':", info_dados)

tabela_hash.remover_arquivo("foto.jpg")

arquivos_restantes = tabela_hash.listar_arquivos()
print("Arquivos restantes na tabela hash:", arquivos_restantes)

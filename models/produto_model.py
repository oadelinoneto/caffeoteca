listaProdutos = []


class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco


def listar_produtos():
    return listaProdutos


def obter_produto_por_id(produto_id):
    for produto in listaProdutos:
        if produto.id == produto_id:
            return produto
    return None


def adicionar_produto(id, nome, descricao, preco):
    for produto in listaProdutos:
        if produto.id == id:
            produto.nome = nome
            produto.descricao = descricao
            produto.preco = preco
            return

    listaProdutos.append(Produto(id, nome, descricao, preco))

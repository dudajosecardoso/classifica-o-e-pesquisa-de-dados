#Crie um TAD (Tipo Abstrato de Dados) de ABB, com, no mínimo, funções para:
#criação;
#inserção;
#impressão (percurso em pré-ordem, pós-ordem, ordem simétrica);
#remoção;
#busca.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

def print_node(node):
    print(node, end=" ")

def arvore_vazia(arv):
    return arv is None

def pre_ordem(arv):
    if not arvore_vazia(arv):
        print_node(arv)
        pre_ordem(arv.left)
        pre_ordem(arv.right)

def em_ordem(arv):
    if not arvore_vazia(arv):
        em_ordem(arv.left)
        print_node(arv)
        em_ordem(arv.right)

def pos_ordem(arv):
    if not arvore_vazia(arv):
        pos_ordem(arv.left)
        pos_ordem(arv.right)
        print_node(arv)

def insere(arv, key):
    if arvore_vazia(arv):
        return Node(key)
    if key < arv.val: 
        arv.left = insere(arv.left, key)
    else:  
        arv.right = insere(arv.right, key)
    return arv

def remove(root, key):
    if root is None:
        return root

    if key < root.val:  
        root.left = remove(root.left, key)
    elif key > root.val:  
        root.right = remove(root.right, key)
        
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        else:
            min_larger_node = root.right
            while min_larger_node.left is not None:
                min_larger_node = min_larger_node.left
            root.val = min_larger_node.val
            root.right = remove(root.right, min_larger_node.val)

    return root

def search(root, value):
    if root is None:
        return None
    if value < root.val:
        return search(root.left, value)
    elif value > root.val:
        return search(root.right, value)
    return root


arvore = None
arvore = insere(arvore, "A")
arvore = insere(arvore, "C")
arvore = insere(arvore, "D")
arvore = insere(arvore, "Z")
arvore = insere(arvore, "F")
arvore = insere(arvore, "G")
arvore = insere(arvore, "B")
arvore = insere(arvore, "M")
arvore = insere(arvore, "P")

print("\nEm ordem:")
em_ordem(arvore)
print("\nPré-ordem:")
pre_ordem(arvore)
print("\nPós-ordem:")
pos_ordem(arvore)
print("\n\n")


search_result = search(arvore, "A")
if search_result:
    print(f"Valor encontrado: {search_result.val}")
else:
    print("Valor não encontrado.")


arvore = remove(arvore, "C")

print("\nApós remover 'C':")
print("\nEm ordem:")
em_ordem(arvore)
print("\nPré-ordem:")
pre_ordem(arvore)
print("\nPós-ordem:")
pos_ordem(arvore)

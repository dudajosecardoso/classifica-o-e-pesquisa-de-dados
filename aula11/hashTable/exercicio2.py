class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  

class HashTableLinkedList:
    def __init__(self):
        self.table = [None] * 10  

    def _hash(self, key):
        return hash(key) % 10

    def insert(self, key, value):
        hash_key = self._hash(key)  
        new_node = Node(key, value)  

        if self.table[hash_key] is None:
            self.table[hash_key] = new_node  
        else:
            current = self.table[hash_key]
            while current:
                if current.key == key:
                    current.value = value  
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node  

    def get(self, key):
        hash_key = self._hash(key)  
        current = self.table[hash_key]
        while current:
            if current.key == key:
                return current.value  
            current = current.next
        return None  


hash_table_ll = HashTableLinkedList()
hash_table_ll.insert("chave1", "Azul")
hash_table_ll.insert("chave2", "Amarelo")
hash_table_ll.insert("chave3", "Vermelho")
print(hash_table_ll.get("chave1"))  
print(hash_table_ll.get("chave2"))  
print(hash_table_ll.get("chave3"))  

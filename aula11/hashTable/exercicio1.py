class HashTableSimple:
    def __init__(self):
        self.table = {}

    def _hash(self, key):
        return hash(key) % 10  

    def insert(self, key, value):
        hash_key = self._hash(key)  
        if hash_key not in self.table:
            self.table[hash_key] = []  
        self.table[hash_key].append((key, value))  

    def get(self, key):
        hash_key = self._hash(key) 
        if hash_key in self.table:
            for k, v in self.table[hash_key]:
                if k == key:
                    return v  
        return None  


hash_table = HashTableSimple()
hash_table.insert("chave1", "Rosa")
hash_table.insert("chave2", "Preto")
hash_table.insert("chave2", "Branco")
print(hash_table.get("chave1"))  
print(hash_table.get("chave2"))  
print(hash_table.get("chave3"))  

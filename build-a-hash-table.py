class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, input_str):
        hash_value = 0
        for letter in input_str:
            hash_value += ord(letter)
        return hash_value

    def add(self, key, value):
        hash_key = self.hash(key)
        self.collection.setdefault(hash_key, {})[key] = value
    
    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            return
        self.collection[hash_key].pop(key, None)
    
    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            return None
        return self.collection[hash_key].get(key)
    
hash_test = HashTable()


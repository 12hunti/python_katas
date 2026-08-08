class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, input_str):
        hash_value = 0
        for letter in list(input_str):
            hash_value += ord(letter)
        return hash_value

    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            self.collection[hash_key][key] = value
        else:
            self.collection[hash_key] = {key: value}
    
    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                del self.collection[hash_key][key]
    
    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                return self.collection[hash_key][key]
        return None
    
hash_test = HashTable()


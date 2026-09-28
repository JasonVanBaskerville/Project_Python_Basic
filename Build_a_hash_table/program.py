class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string: str) -> int:
        characters = list(string)
        ascii_code = [ord(character) for character in characters]
        return sum(ascii_code)

    def add(self, key: str, value):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        self.collection[hash_key][key] = value

    def remove(self, key: str):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            return

        if key not in self.collection[hash_key]:
            return

        del self.collection[hash_key][key]

    def lookup(self, key: str):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            return

        if key not in self.collection[hash_key]:
            return

        return self.collection[hash_key][key]



table1 = HashTable()
print(table1.collection)

print(table1.hash('golf'))
table1.add('golf', 'sport')
print(table1.collection)

print(table1.hash('dear'))
print(table1.hash('read'))
table1.add('dear', 'friend')
table1.add('read', 'book')
print(table1.collection)

print(table1.lookup('golf'))

table1.remove('golf')
print(table1.collection)


print(table1.lookup('golf'))
print(table1.lookup('cfc'))

table1.add('rose', 'flower')
print(table1.collection)
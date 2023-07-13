
class Table:

    def __init__(self, TABLE_SIZE = 100):
        self.table_size = TABLE_SIZE
        self.table = [[] for _ in range(TABLE_SIZE)]

    #Calculates the has of the key
    def calculate_hash(self, key):
        tot = 0
        for char in key:
            tot += ord(char)

        return tot % self.table_size


    def add_item(self, key, data):

        h = self.calculate_hash(key)
        self.table[h].append((key, data))

    def delete_item(self, key):
        
        h = self.calculate_hash(key)

        for element in self.table[h]:
            if element[1] == key:
                self.table.remove(element)

    def print(self):
        for element in self.table:
            print(element)



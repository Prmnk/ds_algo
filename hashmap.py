class hashmap:

    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size
        pass

    def hashfucntion(self,key):
        sum = 0
        for i in range(len(key)):
            sum += ord(key[i])

        return sum%self.size

    def put(self,key, data):
        index = self.hashfucntion(key)

        while self.keys[index] is not None:
            # in case same key exist at the index , update the value
            if self.keys[index]== key:
                self.values[index] == data
                return
            #linear probing in case key
            index = (index+1)%self.size

        self.keys[index] = key
        self.values[index] = data

    
    def get(self,key):
        index = self.hashfucntion(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index+1)%self.size

        return None

table = hashmap()

table.put('apple',10)
table.put("orange", 20)
table.put("car",30)
table.put("table", 40)

print(table.get("kev"))
print(table.get("car"))
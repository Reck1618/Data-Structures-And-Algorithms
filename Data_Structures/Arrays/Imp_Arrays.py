# Implement an Array in python.
# Build methods such as get, push, pop, delete.

class Array:

    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):                            # Represents the class object as a string
        return str(self.__dict__)
    
    def get(self,index):
        return self.data[index]

    def push(self,item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item
    
    def delete(self, index):
        deleted_item = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

        del self.data[self.length - 1]
        self.length -= 1
        return deleted_item

arr = Array()
arr.push("hello")
arr.push("my fellow")
arr.push("human")
arr.delete(1)
print(arr)
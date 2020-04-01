
class Caretaker:
    def __init__(self):
        self.storage = []

    def show_storage(self):
        for i, copy in enumerate(self.storage):
            print(i, copy.name)

    def restore_copy(self, index):
        return self.storage[index]

    def store_copy(self, copy):
        self.storage.append(copy)
        return len(self.storage)  - 1
        


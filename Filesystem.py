class MyFileSystemObject:
    def __init__(self, name, date):
        self.name = name
        self.creation_date = date


class MyFile(MyFileSystemObject):
    def __init__(self, name, date):
        MyFileSystemObject.__init__(self, name, date)
        self.content = '' #хранит текст
    

    def show_contents(self, i):
        print('\t' * i, self.name)

    def clone(self):
        """ Метод clone: для каждого класса; копирует свойства и возвращает новый объект"""
        clone = MyFile(self.name, self.creation_date)
        clone.content = self.content
        return clone
        


class MyFolder(MyFileSystemObject):
    def __init__(self, name, date):
        MyFileSystemObject.__init__(self, name, date)
        self.contents= []

    def add_element(self, element):
        self.contents.append(element)

    def remove_element(self, element):
        self.contents.remove(element)

    def show_contents(self, i):
        print('\t' * i, self.name + '/')
        for element in self.contents:
            element.show_contents(i + 1)
        print('\t')

    def clone(self):
        """ Метод clone: для каждого класса; копирует свойства и возвращает новый объект"""
        clone = MyFolder(self.name, self.creation_date)
        for element in self.contents:
            clone.contents.append(element.clone())

        return clone



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
        



        







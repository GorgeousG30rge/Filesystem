from Caretaker import Caretaker

Storage = Caretaker()

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
    
    def __apply__(self, copy):
        self.content = copy.content
        self.date = copy.creation_date
        self.name = copy.name

    def store_copy(self):
        return Storage.store_copy(self.clone())
		
    def restore_copy(self, index):
        copy = Storage.restore_copy(index)
        self.__apply__(copy)
        


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

    def __apply__(self, copy):
        self.name = copy.name
        self.creation_date = copy.creation_date
        self.contents = 0 # Здесь должно быть скопированное содержание списка

    def store_copy(self):
        return Storage.store_copy(self.clone())

    def restore_copy(self, index):
        copy = Storage.restore_copy(index)
        self.name = copy.name
        self.creation_date = copy.creation_date 
        self.contents = copy.contents
        self.__apply__(copy)

Storage.show_storage()



        


        




        



        







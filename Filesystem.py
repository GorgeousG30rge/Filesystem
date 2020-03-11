class MyFileSystemObject:
    def __init__(self, name):
        self.name = name


class MyFile(MyFileSystemObject):
    def __init__(self, name, date):
        MyFileSystemObject.__init__(self, name)
        self.creation_date = date
        self.content = '' #хранит текст
    

    def show_contents(self, i):
        print('\t' * i, self.name)

    def clone(self, obj):
        clone = obj
        return clone
        


class MyFolder(MyFileSystemObject):
    def __init__(self, name):
        MyFileSystemObject.__init__(self, name)
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

    def clone(self, obj):
        clone = obj
        return clone


""" Метод clone:
для каждого класса;
копирует свойства
и возвращает новый объект"""
        







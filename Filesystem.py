class MyFileSystemObject:
    def __init__(self, name):
        self.name = name


class MyFile(MyFileSystemObject):
    def __init__(self, name, date):
        MyFileSystemObject.__init__(self, name)
        self.creation_date = date

class MyFolder(MyFileSystemObject):
    def __init__(self, name):
        MyFileSystemObject.__init__(self, name)
        self.data = []
        







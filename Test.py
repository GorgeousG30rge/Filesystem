from Filesystem import MyFile
from Filesystem import MyFolder
from Filesystem import Caretaker

DATE = '16.03.2020'

Storage = Caretaker()
root = MyFolder('root', DATE)
dir1 = MyFolder('dir1', DATE)
dir2 = MyFolder('dir2', DATE)
root.add_element(dir1)
root.add_element(dir2)
file1 = MyFile('file1.txt', DATE)
file2 = MyFile('file2.txt', DATE)
dir1.add_element(file1)
dir1.add_element(file2)
file3 = MyFile('file3.txt', DATE)
file4 = MyFile('file4.txt', DATE)
dir2.add_element(file3)
dir2.add_element(file4)
data = MyFolder('data', DATE)
part1 = MyFile('part1.bin', DATE)
part2 = MyFile('part2.bin', DATE)
system = MyFolder('system', DATE)
sysinfo = MyFile('sys.info', DATE)
system.add_element(sysinfo)
dir2.add_element(system)
dir2.add_element(data)
data.add_element(part1)
data.add_element(part2)
root_backup1 = root.clone()
Storage.store_copy(root_backup1)
test_dir = MyFolder('test_dir', DATE)
test_file = MyFile('test_file', DATE)
test_dir.add_element(test_file)
root.add_element(test_dir)
print(root.show_contents(0))
root = Storage.restore_copy(0)
Storage.show_storage()
print(root.show_contents(0))










from Filesystem import MyFile
from Filesystem import MyFolder
from Filesystem import Caretaker

DATE = '16.03.2020'

root = MyFolder('root', DATE)
dir1 = MyFolder('dir1', DATE)
dir2 = MyFolder('dir2', DATE)
file1 = MyFile('file1.txt', DATE)
file2 = MyFile('file2.txt', DATE)
file3 = MyFile('file3.txt', DATE)
file4 = MyFile('file4.txt', DATE)
data = MyFolder('data', DATE)
part1 = MyFile('part1.bin', DATE)
part2 = MyFile('part2.bin', DATE)
system = MyFolder('system', DATE)
sysinfo = MyFile('sys.info', DATE)
test_dir = MyFolder('test_dir', DATE)
test_file = MyFile('test_file', DATE)
root.add_element(dir1)
root.add_element(dir2)
dir1.add_element(file1)
dir1.add_element(file2)
dir2.add_element(file3)
dir2.add_element(file4)
dir2.add_element(data)
data.add_element(part1)
data.add_element(part2)
system.add_element(sysinfo)
data.add_element(system)
root.show_contents(0)
root.store_copy()
test_file = MyFile('test_file', DATE)
test_dir = MyFolder('test_folder', DATE)
data.add_element(test_file)
data.add_element(test_dir)
test_file.store_copy()
root.show_contents(0)
root.restore_copy()











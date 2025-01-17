from pathlib import Path

path = Path('example.txt')
print(path.exists())  # Output: True or False

path = Path('/home/rdflex/Desktop/vpa_RdFlex/vpa_day-1')
print(path.is_dir())

p = Path('/home/rdflex/Desktop/vpa_RdFlex/vpa_day-12-Extra')
for dir in p.iterdir():
    if dir.is_dir():
        print(dir)
 
py_files = p.rglob('*.py')
print(list(py_files))
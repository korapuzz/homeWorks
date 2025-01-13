import os
import time

directory = "."
#print(list(os.walk(directory)))

print(os.path.join("c:\\", "python\\", "projects\\"))

file = "module_07_02.py"

print(os.path.getmtime(file))
print(time.ctime(os.path.getmtime(file)))

print(os.path.getsize(file))
print(os.getcwd())
print(os.path.dirname(os.getcwd()))
#print(os.name(os.getcwd()))

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.getcwd()
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.getcwd()
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

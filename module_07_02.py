def custom_write(file_name, strings):
    file = open (file_name, "w", encoding='utf-8')
    strings_positions = {}
    number = 0
    for line in strings:
        number += 1
        pos = file.tell()
        strings_positions[(number, pos)] = line
        file.write(line+"\n")
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

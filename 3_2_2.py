'''Задание: составные сообщения об ошибках и поиск подстроки
Вам дан шаблон для функции test_substring, которая принимает два значения: full_string и substring.

Функция должна проверить вхождение строки substring в строку full_string с помощью оператора assert и, в случае
несовпадения, предоставить исчерпывающее сообщение об ошибке.'''

'''s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')'''

def test_substring(full_string, substring):
    assert substring in full_string, "expected '{}' to be substring of '{}'".format(substring, full_string)

def test_substring(full_string, substring):
    assert substring in full_string, f"expected {substring!r} to be substring of {full_string!r}"

def test_substring(full_string, substring):
    assert substring in full_string,\
    f"expected '{substring}' to be substring of '{full_string}'"










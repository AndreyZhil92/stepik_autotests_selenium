'''Задание: составные сообщения об ошибках
Для закрепления материала реализуйте проверку самостоятельно.

Вам дана функция test_input_text,  которая принимает два значения: expected_result — ожидаемый результат,
и actual_result — фактический результат. Обратите внимание, input использовать не нужно!

Функция должна проверить совпадение значений с помощью оператора assert и, в случае несовпадения,
предоставить исчерпывающее сообщение об ошибкe'''


#по старинке решил
'''def test_input_text(expected_result, actual_result):
    if expected_result != actual_result:
        print(f"expected {expected_result}, got {actual_result}")
    else:
        print('')'''

#требуемое решение

def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'

def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, "expected {}, got {}".format(expected_result, actual_result)

def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
        "expected " + expected_result + ", got " + actual_result

def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, \
        f"expected {expected_result}, got {actual_result}"



#===================================================================
'''a,b = input().split()
print("" if a == b  else f'expected {a}, got {b}')'''

#print("expected {}, goes {}".format("one", "two") if )

'''actual_result = "abrakadabra"
print("Wrong text, got", actual_result, "something wrong"'''
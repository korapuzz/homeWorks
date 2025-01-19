def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for n in numbers:
            if isinstance(n, int) or isinstance(n, float):
                result += n
            else:
                print(f"Некорректный тип данных для подсчёта суммы - {n}")
                incorrect_data += 1
        return result, len(numbers) - incorrect_data
    except TypeError as ex:
        print("В numbers записан некорректный тип данных")
        return None

def calculate_average(*numbers):
    try:
        summ, count = personal_sum(*numbers)
        return summ / count
    except ZeroDivisionError as ex:
        return 0
    except TypeError as ex:
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

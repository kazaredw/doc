# doc
spisok[]
spisok.append(23} добавить значение в конец списка
spisok.extend([5,6,7,]) добавить список в конец списка
spisok.insert(1,'ewewe') вставляет в список но номеру индекса
spisok.remove('wewew') удаляет в списке по имени элемента
spisok.pop(0) удаляет по номеру элемента
spisok.index('sdsds') возвращает индекс элемента 
spisok.sort() сортирует список
cars.sort(reverse=True) сортирует в обратном алфовитному порядику
casrs.sorted() сортирует элементы, но не меняет список
spisok.reverse() переворачивает список
spisok.clear() очишает весь список
len(cars) определение длинный списка

Перебор элементов списка
for i in spisok:
  print (i)

Заполнить список числовыми значениями
numbers = list(range(1,6))
print(numbers)

Можно узнать минимальное, максимальное сумму списка
min(spisok), max(spisok), sum(spisok)

Генератор списка
squares = [value**2 for value in range(1,11)]

# Проект Homework_2

## Описание

## Установка

Клонируйте репозиторий:

```
git clone git@github.com:AlexandrKulikov1803/Course_work_1.git
```

## Использование

### Модуль classes.py

Класс ***Product*** содержит основную информацию о продукте:

+ Название продукта(str)
+ Описание(str)
+ Стоимость(float)
+ Количество(int)

Класс ***Category*** содержит основную информацию о категории:

+ Название категории(str)
+ Описание(str)
+ Список продуктов в данной категории(list)

А также имеются переменные ***category_count*** и ***product_count*** для учёта количества категорий и продуктов.

### Модуль utils.py

Модуль ***utils.py*** содержит две функции: ***read_json***, ***create_objects_from_json***.

Функция ***read_json*** считывает данные json-файла и преобразует их в список словарей.

```
# вызов функции
print(read_json("путь к файлу/файл.xlsx"))

# выход функции
[{'name': 'Смартфоны', 'description': 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни', 'products': [{'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0, 'quantity': 5}, {'name': 'Iphone 15', 'description': '512GB, Gray space', 'price': 210000.0, 'quantity': 8}, {'name': 'Xiaomi Redmi Note 11', 'description': '1024GB, Синий', 'price': 31000.0, 'quantity': 14}]}, {'name': 'Телевизоры', 'description': 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником', 'products': [{'name': '55" QLED 4K', 'description': 'Фоновая подсветка', 'price': 123000.0, 'quantity': 7}]}]
```

+ Тестирование считывания данных json-файла и преобразования в список словарей.
+ Проверка работы функции при получении пути к несуществующему файлу.
+ Проверка работы функции при получении пути к файлу с некорректными данными.

Функция ***create_objects_from_json*** пробегает по списку словарей и создаёт список экземпляров классов и подклассов
внутри них.

```
# вызов функции
categories_data = create_objects_from_json(список словарей)
print(categories_data)
print(categories_data[0].name)
print(categories_data[0].description)
print(categories_data[0].products)
print(categories_data[0].products[0].name)


# выход функции
[<src.classes.Category object at 0x0000015E97786900>, <src.classes.Category object at 0x0000015E97725090>]
Смартфоны
Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни
[<src.classes.Product object at 0x0000020FF4B367B0>, <src.classes.Product object at 0x0000020FF4AD7750>, <src.classes.Product object at 0x0000020FF4AD79D0>]
Samsung Galaxy C23 Ultra
```

+ Тестирование преобразования списка словарей в список экземпляров класса.

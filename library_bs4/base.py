# Импортируем необходимые модули
from bs4 import BeautifulSoup  # BeautifulSoup используется для парсинга HTML
import re  # Модуль re нужен для работы с регулярными выражениями

# Открываем и читаем HTML-файл
with open('blank/index.html') as file:  # Открываем файл 'index.html' в папке 'blank'
    src = file.read()  # Читаем содержимое файла в переменную src

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(src, 'lxml')  # Используем парсер 'lxml' для обработки HTML-кода

# Эти строки закомментированы, они показывают, как получить заголовок документа (<title>)
# title = soup.title  # Находит тег <title>
# print(title)  # Печатает тег <title> целиком
# print(title.text)  # Печатает текст внутри тега <title>
# print(title.string)  # То же, что и .text, возвращает текстовое содержимое

# Работа с методами .find() и .find_all()
# Находим первый тег <h1> в документе
page_h1 = soup.find('h1')  # .find() возвращает первый найденный элемент
print(page_h1)  # Печатаем тег <h1> целиком

# Находим все теги <h1> в документе
page_all_h1 = soup.find_all('h1')  # .find_all() возвращает список всех найденных элементов
print(page_all_h1)  # Печатаем список всех тегов <h1>

# Проходим по списку всех <h1> и печатаем их текстовое содержимое
for item in page_all_h1:
    print(item.text)  # .text извлекает текст внутри тега

# Закомментированный пример поиска имени пользователя
# user_name = soup.find('div', class_='user__name')  # Находит <div> с классом 'user__name'
# print(user_name.text.strip())  # Печатает текст внутри, убирая лишние пробелы

# Находим текст внутри тега <span>, который находится внутри <div> с классом 'user__name'
user_name = soup.find('div', class_='user__name').find('span').text  # Цепочка методов для вложенного поиска
print(user_name)  # Печатаем текст из <span>

# Находим все теги <span> внутри элемента с классом 'user__info'
find_all_span_in_user_info = soup.find(class_='user__info').find_all('span')  # Ищем все <span> внутри 'user__info'
# print(find_all_span_in_user_info)  # Закомментировано: печать списка всех <span>

# Закомментированные примеры обработки списка <span>
# for item in find_all_span_in_user_info:  # Цикл по списку <span>
#     print(item.text)  # Печать текста каждого <span>
# print(find_all_span_in_user_info[2].text)  # Печать текста третьего <span> по индексу

# Находим все ссылки <a> внутри <ul>, который находится в элементе с классом 'social__networks'
social_links = soup.find(class_='social__networks').find('ul').find_all('a')  # Цепочка поиска вложенных элементов
print(social_links)  # Печатаем список всех ссылок <a>

# Проходим по списку ссылок и печатаем их текст и атрибут 'href'
for item in social_links:
    item_text = item.text  # Извлекаем текст ссылки
    item_url = item.get('href')  # .get('href') извлекает значение атрибута 'href'
    print(f"{item_text} : {item_url}")  # Печатаем текст и URL в формате "текст : URL"

# Работа с методами .find_parent() и .find_parents()
# Находим ближайший родительский <div> с классом 'user__post' для элемента с классом 'post__text'
post_div = soup.find(class_='post__text').find_parent('div', class_='user__post')  # Исправлено: указываем класс правильно
print(post_div)  # Печатаем найденный родительский элемент

# Находим все родительские <div> с классом 'user__post' для элемента с классом 'post__text'
post_divs = soup.find(class_='post__text').find_parents('div', class_='user__post')  # Исправлено:一致性 в имени класса
print(post_divs)  # Печатаем список всех родительских элементов

# Работа с навигацией .next_element
# Переходим к следующему элементу дважды от элемента с классом 'post__title' и печатаем его текст
next_el = soup.find(class_='post__title').next_element.next_element.text  # .next_element идет по дереву парсинга
print(next_el)  # Печатаем текст второго следующего элемента

# Находим следующий элемент после 'post__title' и печатаем его текст
next_el = soup.find(class_='post__title').find_next().text  # .find_next() ищет следующий элемент в документе
print(next_el)  # Печатаем текст следующего элемента

# Работа с методами .find_next_sibling() и .find_previous_sibling()
# Находим следующий соседний элемент для 'post__title'
next_sib = soup.find(class_='post__title').find_next_sibling()  # Ищет следующий элемент на том же уровне
print(next_sib)  # Печатаем следующий соседний элемент

# Находим предыдущий соседний элемент для 'post__date'
prev_sib = soup.find(class_='post__date').find_previous_sibling()  # Ищет предыдущий элемент на том же уровне
print(prev_sib)  # Печатаем предыдущий соседний элемент

# Цепочка навигации: от 'post__date' к предыдущему, затем к следующему элементу, и печатаем текст
post_title = soup.find(class_='post__date').find_previous_sibling().find_next().text  # Комбинируем методы
print(post_title)  # Печатаем текст результата

# Находим все ссылки <a> внутри элемента с классом 'some__links'
links = soup.find(class_='some__links').find_all('a')  # Ищем все теги <a>
print(links)  # Печатаем список ссылок

# Проходим по списку ссылок и печатаем их атрибуты 'href' и 'data-attr'
for link in links:
    link_href_attr = link.get('href')  # Извлекаем атрибут 'href'
    link_data_attr = link.get('data-attr')  # Извлекаем атрибут 'data-attr'
    print(f"href: {link_href_attr}, data-attr: {link_data_attr}")  # Исправлено: печатаем оба атрибута

# Находим первую ссылку <a>, текст которой содержит 'Одежда', с помощью регулярного выражения
find_a_by_text = soup.find('a', text=re.compile('Одежда'))  # Ищем тег <a> по тексту
print(find_a_by_text)  # Печатаем найденную ссылку

# Находим все элементы, текст которых содержит 'Одежда' или 'одежда' (с учетом регистра)
find_all_clothers = soup.find_all(text=re.compile("([Оо]дежда)"))  # Используем регулярное выражение для поиска
print(find_all_clothers)  # Печатаем список всех совпадений
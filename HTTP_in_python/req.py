import requests
import config

# 📤 Простой GET-запрос
response = requests.get('https://42.uz/')
print(response.status_code)     # 200
# print(response.text)        # HTML-код страницы 

"""
📌 response.text содержит HTML-код страницы — то, 
что ты увидишь в браузере при просмотре кода.
"""


# 📥 Передача параметров
# Часто данные передаются в URL, например ?page=2. Это можно сделать так:

params = {'page':2}
response = requests.get('https://www.sulpak.kg/f/noutbuki', params=params)
# 📎 Преимущество: тебе не нужно вручную формировать URL — requests сделает это за тебя.
print(response.status_code)


# 🧢 Заголовки (headers)
"""
Иногда сайты проверяют, кто делает запрос. 
Если ты не укажешь User-Agent, сайт может 
вернуть пустой ответ или заблокировать тебя.
"""
params = {'page':2}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
response = requests.get('https://www.sulpak.kg/f/noutbuki', params=params, headers=headers)
print(response.status_code)


# 🍪 Работа с cookies
"""
Если сайт использует куки (например, для входа в аккаунт), 
ты можешь передать их вручную:
"""

# Создаём объект сессии
session = requests.Session()

# Добавляем заголовок, чтобы сайт думал, что мы браузер
session.headers.update({'User-Agent': 'Mozilla/5.0'})

# Данные для входа
login_data = {'username': config.instaram_username , 'password': config.instagram_password}

# Отправляем запрос для логина
session.post('https://www.instagram.com/accounts/login/', data=login_data)

# Теперь можем зайти на защищённую страницу
response = session.get('https://www.instagram.com/mr__hikmatulloh/')
print(response.status_code)
print(response.text)  # Смотрим содержимое страницы профиля
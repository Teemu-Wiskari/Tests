import requests


def create_folder(path, ya_token):
    """Функция для создания папки на яндекс диске"""
    headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {ya_token}'
        }
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    response = requests.put(f'{url}?path={path}', headers=headers)
    result = response.status_code

    if result == 201:
        print(f'Папка "{path}" успешно создана!')

    elif result == 409:
        print(f'Папка "{path}" уже существует!')

    elif result == 401:
        print('Отсутствует токен доступа к яндекс диску. Проверьте введенный токен.')

    else:
        print(f'Ошибка при создании папки "{path}": {result}')

    return result
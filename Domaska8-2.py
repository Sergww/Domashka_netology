import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл по пути file_path на яндекс диск"""
        self.file_path = file_path

        folder_yadisk = ''
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth ' + self.token
            }
        params = {"path": folder_yadisk + self.file_path, "overwrite": "true"}

        response = requests.get(upload_url, headers=headers, params=params).json()
        #pprint(response)
        href = response['href']  # получили ссылку для загрузки
        #print(href)
        response = requests.put(href, data=open(self.file_path, 'rb'))

        return response

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file ='myfile.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)

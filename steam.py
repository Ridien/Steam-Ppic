

import requests


def updatePicture():
    url = 'https://steamcommunity.com/actions/FileUploader'
    i = '76561198246664798' # enter ID64
    cookies = {
        'steamLoginSecure': '76561198252244294%7C%7CEE7EF021946D4DD74298F3A2063D02A37099A215',
        'sessionid': 'cbad38a970afa6b2920bc053',
    }
    data = {
        "MAX_FILE_SIZE": "1048576",
        "type": "player_avatar_image",
        "sId": "76561198252244294",
        "sessionid": "cbad38a970afa6b2920bc053",
        "doSub": "1",

    }

    picture = open('picture.jpg', 'rb')
    r = requests.post(url=url, params={'type': 'player_avatar_image', 'sId':i}, files={'avatar': picture}, data=data, cookies=cookies)
    if r:
        print(r)

updatePicture()
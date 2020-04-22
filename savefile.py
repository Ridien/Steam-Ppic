import requests 
import urllib.request
import os
from steam import updatePicture
import time


# api-endpoint 
URL = "https://danbooru.donmai.us/posts/"

def downloadImage(id):
    fetchURL = URL + id + '.json'
    r = requests.get(url = fetchURL, params = "") 
    if r:
        try:
            data = r.json() 
            saveImage(data)
        except:
            print('this is not a valid file')
            



def saveImage(data):
    file_url = ''
    characters = data['tag_string_character']
    anime = ''
    name= ''
    extension = ''
    try:
        
        if 'large_file_url' in data:
            file_url = data['large_file_url']
            extension = data['large_file_url'].rsplit('.', 1)[1]
        elif 'large_file_url' in data:
            file_url = data['file_url'] 
            extension = data['file_url'].rsplit('.', 1)[1]
        else:
            print('No links for given image')
        name=str(data['id'])+'.' +extension
         
        if data['tag_string_copyright'] == '':
            anime = 'original'
        else:
            anime = data['tag_string_copyright']

        folder = anime.split(' ', 1)[0]
        folder = folder.split('/', 1)[0]
        path = 'picture.jpg'
        urllib.request.urlretrieve(data['large_file_url'], path)
        createLog(file_url, name, characters, anime, path)
        print('here')

    except:
        print('an exception occurred, perhaps you are trying to load a premium image')
        print('The image in question was ' + name)


def createLog(file_url, image_id, characters, anime, filePath):
    print("________________________________________________________________________________________")
    print("Starting the log for image with id " + image_id + "...")
    print("______________")
    print("Anime:" + anime)
    print("Characters:" + characters)
    print("______________")
    print("Actions:")

    print("Downloading file from " + file_url + "...")
    print("Image downloaded, you can find it at: " + filePath)
    print("________________________________________________________________________________________")
    print()
    print()
    print()

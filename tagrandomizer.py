# importing the requests library 
import requests 
import urllib.request
import os
from savefile import saveImage
import random

# api-endpoint 
URL = "https://danbooru.donmai.us/posts.json"
relatedTagsURL = "https://danbooru.donmai.us/related_tag.json"


# sending get request and saving the response as response object 


def getRandomImage(tag):
    print("tag: " +tag)
    data = {"tags":tag, "limit":100}
    relatedParams = {"query":tag}
    r = requests.get(url = URL, params = data) 
    if r:	
        # extracting data in json format 
        picList = r.json()
        if len(picList) > 0:
            post = random.randint(0, len(picList)-1)
            print('Received images for the given tag, downloading the ' + str(post) + ' result')
            saveImage(picList[post])
        else:
            related = requests.get(url = relatedTagsURL, params = relatedParams)
            related = related.json()
            
            if len(related['wiki_page_tags']) > 0:
                print('No images found for the given tag, assuming you meant ' + related['wiki_page_tags'][0][0])
                data = {"tags":related['wiki_page_tags'][0][0], "limit":100}
                r = requests.get(url = URL, params = data) 
                if r:	
                    # extracting data in json format 
                    picList = r.json()
                    if len(picList) > 0:
                        post = random.randint(0, len(picList)-1)
                        print('Received images for the given tag, downloading the ' + str(post) + ' result')
                        saveImage(picList[post])
            else:
                print("Sorry, i did not find any images for this tag...")    
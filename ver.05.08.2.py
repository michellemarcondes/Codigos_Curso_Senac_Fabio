#tread's
import threading
import requests

class Download(treading.Thread):
    def __init__(self, url):
        super().__init__()
        self._url = url
        
    def rum(self):
        response = requests.get(self._url)

        filename = self._url.split('//')[1].replace('/','_') + '.html'
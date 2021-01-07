import requests
from requests_oauthlib import OAuth1
import os


class IconGetter:
    def __init__(self, save_dir="tmp"):
        key = os.environ["KEY"]
        secret = os.environ["SECRET"]
        self.auth = OAuth1(key, secret)
        self.endpoint = "http://api.thenounproject.com/icon"
        self.save_dir = save_dir

    def get_and_save_icon(self, id):
        response = requests.get(f"{self.endpoint}/{id}", auth=self.auth)
        res_json = response.json()
        print(res_json["icon"])
        if type(id) == str:
            ID = f"{id}.png"
            icon_url = res_json["icon"]["preview_url"]
        elif type(id) == int:
            ID = f"{id}.svg"
            icon_url = res_json["icon"]["icon_url"]
        img = requests.get(icon_url)
        with open(os.path.join(self.save_dir, ID), "wb") as file:
            file.write(img.content)


icon_getter = IconGetter()
icon_getter.get_and_save_icon("forest")
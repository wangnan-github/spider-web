# -*- coding: gb2312 -*-
import requests


class HtmlDownLoader(object):
    def __init__(self):
        pass

    def download(self, url):
        if url is None:
            return None

        resp = requests.get(url)
        resp.encoding = resp.apparent_encoding
        if resp.status_code != 200:
            return None

        return resp.text

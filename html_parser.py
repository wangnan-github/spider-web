# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    def __init__(self):
        pass

    # 从网页中提取链接
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/html/article/'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    # 获取网页中内容
    def _get_new_data(self, page_url, soup):
        res_data = {}

        page_title = soup.find('div', class_='content').find('h1')
        res_data['title'] = page_title.get_text()
        print res_data['title']

        urls = []
        links = soup.find_all('img', src=re.compile(r'^https://.*jpg$'))
        for link in links:
            urls.append(link['src'])
        res_data['urls'] = urls

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

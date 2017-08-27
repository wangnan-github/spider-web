# -*- coding: UTF-8 -*-
import os
import urllib2


class HtmlOutputer(object):
    def __init__(self):
        pass

    def collect_data(self, data):
        if data is None:
            return

        dir_name = r'resource/picture/{}'.format(str(data['title'].encode('utf-8')))
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        urls = data['urls']
        for i in range(len(urls)):
            print urls[i]
            file_name = '{}/{}{}'.format(dir_name, i, '.jpg')
            if os.path.exists(file_name):
                continue
            content = urllib2.urlopen(urls[i]).read()
            with open(file_name, 'wb') as f:
                f.write(content)

        self.output_md(data)

    def output_md(self, data):
        md = open('resource/picture.md', 'a+')
        md.writelines('# {}'.format(str(data['title'].encode('utf-8'))))
        for url in data['urls']:
            md.writelines(' * {}'.format(str(url.encode('utf-8'))))
        md.writelines()
        md.close()

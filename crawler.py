# coding: utf-8

from bs4 import BeautifulSoup
import requests
import os

class yuanzun():

    def __init__(self):
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}


    def request(self, url): # 通过url获取html
        content = requests.get(url, headers = self.headers)
        return content


    def all_url(self, url): # 获取全部的小说章节名和地址列表
        start_html = self.request(url)
        Soup = BeautifulSoup(start_html.text, 'lxml')

        dd_list = Soup.find_all('a')
        head_url = dd_list[0]['href']

        book = '/book/3137'
        url_lists = []
        title_lists = []
        for i in dd_list:
            try:
                if book in i['href']:
                    title_lists.append(i.text)
                    url_lists.append(head_url + i['href'])
            except:
                print("Get Error！")
        return title_lists, url_lists


    def get_all_content(self, start, url): # 下载全部整本小说

        titles, urls = self.all_url(url)
        for u in range(start, len(urls)):
            name = titles[u]
            content = self.get_conten-t(urls[u]) # 获取每章章节文本
            self.local_load(name, content)


    def local_load(self, name, content):   # 下载函数

        try:
            f = open(name + '.txt', 'w', encoding='utf-8')
            f.write(content)
            f.close()
            print(name + ' Loaded success!')
        except:
            print(name + " False!")


    def get_content(self, url): # 获取当前章节文本

        content = self.request(url)
        novel_Soup = BeautifulSoup(content.text, 'lxml')
        novel_content = novel_Soup.find('div', id='content').text

        return novel_content


    def updata(self, updata_num, url): # 更新而不必重新爬取
        titles, urls = self.all_url(url)
        names, contents = [], []
        for u in range(1, updata_num):
            name = titles[(-1) * u]
            names.append(name)
            content = self.get_content(urls[(-1)*u])
            contents.append(content)
        return names, contents


if __name__ == '__main__':

    Yuanzun = yuanzun()
    #Yuanzun.get_all_content(0, "https://www.qu.la/book/3137/")
    names, contents = Yuanzun.updata(3, "https://www.qu.la/book/3137/")
    print(names, contents)




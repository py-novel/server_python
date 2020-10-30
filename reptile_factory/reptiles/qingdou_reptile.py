from bs4 import BeautifulSoup

from reptile_factory.utils.gene_id import gene_id
from reptile_factory.utils.request import post, get
from reptile_factory.utils.get_url_prefix import get_url_prefix

class Qingdou(object):
    def __init__(self, target_url):
        if target_url is None:
            target_url = 'https://www.qingdou.net'
        self.url_prefix = get_url_prefix(target_url)
        self.target_url = target_url

    def get_novel_list(self, keyword):
        # 获取 html 
        target_url = 'https://www.qingdou.net/search.html'
        html = post(target_url, { 'searchkey': keyword })
        
        # 解析 html
        soup = BeautifulSoup(html, 'lxml')
        novel_list = []
        for item in soup.find_all('div', attrs={ 'id': 'alistbox' }):
            book_name = item.find('div', attrs={'class': 'title'}).h2.a.string
            author_name = item.find('div', attrs={'class': 'title'}).span.a.string
            book_url = item.find('div', attrs={'class': 'title'}).h2.a.get('href')
            novel_list.append({
                'authorName': author_name,
                'bookName': book_name,
                'bookUrl': f'{self.url_prefix}{book_url}',
            })
        return novel_list

    def get_novel_intro(self): 
        # 获取 html 
        html = get(self.target_url)
        
        # 解析 html
        soup = BeautifulSoup(html, 'lxml')
        author_name = soup.find('h1', { 'class': 'f20h' }).em.string.split('：')[1]                 # 作者名
        book_name = soup.find('h1', { 'class': 'f20h' }).contents[0]                                # 书名
        last_update_time = soup.find('div', { 'class': 'top' }).find_all('span')[3].contents[1]     # 最后更新时间
        book_intro = soup.find('div', { 'class': 'intro' }).contents[0]                             # 小说简介
        book_cover_url = soup.find('div', { 'class': 'pic' }).img.get('src')                        # 小说封面地址
        first_chapter_url = soup.dl.dd.a.get('href')                                                # 第一章地址
        classify_name = soup.find('ul', { 'class': 'bread-crumbs' }).find_all('li')[1].a.string     # 分类名称
        
        return {
            'authorName': author_name,
            'bookName': book_name,
            'lastUpdateTime': last_update_time,
            'bookIntro': book_intro,
            'bookCoverUrl': book_cover_url,
            'firstChapterUrl': f'{self.url_prefix}{first_chapter_url}',
            'classifyName': classify_name,
        }

    def get_chapter_list(self):
        # 获取 html 
        html = get(self.target_url)

        # 解析 html
        soup = BeautifulSoup(html, 'lxml')
        dd_list = soup.find_all('dd')
        chapter_list = []
        for dd in dd_list:
            chapter_name = dd.a.string
            chapter_url = dd.a.get('href')
            chapter_list.append({
                'id': gene_id(),
                'chapterName': chapter_name,
                'chapterUrl': f'{self.url_prefix}{chapter_url}',
            })     

        return chapter_list                           

    def get_chapter_content(self):
        # 获取 html 
        html = get(self.target_url)

        # 解析 html
        soup = BeautifulSoup(html, 'lxml')
        # 章节标题
        chapter_title = soup.find('div', { 'class': 'kfyd' }).h2.string     
        # 章节内容
        p_list = soup.find('div', { 'id': 'content' }).contents             
        chapter_content = ''
        for p in p_list:
            chapter_content += p.string
        # 上一章节url地址
        prev_chapter_url = soup.find('div', { 'id': 'thumb' }).find_all('a')[0].get('href')     
        if '.html' not in prev_chapter_url:
            prev_chapter_url = None
        else:
            prev_chapter_url = self.url_prefix + prev_chapter_url
        # 下一章节url地址
        next_chapter_url = soup.find('div', { 'id': 'thumb' }).find_all('a')[2].get('href')     
        if '.html' not in next_chapter_url:
            next_chapter_url = None
        else:
            next_chapter_url = self.url_prefix + next_chapter_url
        
        return {
            'chapterTitle': chapter_title,
            'chapterContent': chapter_content,
            'prevChapterUrl': prev_chapter_url,
            'nextChapterUrl': next_chapter_url,
        }
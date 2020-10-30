from bs4 import BeautifulSoup

from reptile_factory.utils.gene_id import gene_id
from reptile_factory.utils.request import post, get
from reptile_factory.utils.get_url_prefix import get_url_prefix

class Biquge5200(object):
    def __init__(self, target_url):
        if target_url is None:
            target_url = 'https://www.biquge5200.cc'
        self.url_prefix = get_url_prefix(target_url)
        self.target_url = target_url

    def get_novel_list(self, keyword):
        # 获取 html 
        target_url = 'https://www.biquge5200.cc/modules/article/search.php?searchkey=' + keyword
        html = get(target_url)
        
        # 解析 html
        soup = BeautifulSoup(html, 'lxml')
        tr_list = soup.table.find_all('tr')[1:]
        novel_list = []
        for tr in tr_list:
            author_name = tr.find_all('td')[2].string       # 作者名
            book_name = tr.find('td').a.string              # 书名
            book_url = tr.find('td').a.get('href')          # 书url地址
            novel_list.append({
                'authorName': author_name,
                'bookName': book_name,
                'bookUrl': book_url,
            })
        return novel_list

    def get_novel_intro(self): 
        # 获取 html 
        html = get(self.target_url)
        
        # 解析 html
        soup = BeautifulSoup(html, 'lxml')
        author_name = soup.find('div', { 'id': 'info' }).p.string.split('：')[1]                        # 作者名
        book_name = soup.find('div', { 'id': 'info' }).h1.string                                        # 书名
        last_update_time = soup.find('div', { 'id': 'info' }).find_all('p')[2].string.split('：')[1]    # 最后更新时间
        book_intro = soup.find('div', { 'id': 'intro' }).find_all('p')[1].string                        # 小说简介
        book_cover_url = soup.find('div', { 'id': 'fmimg' }).img.get('src')                             # 小说封面地址
        first_chapter_url = soup.find('div', {'id': 'list'}).find_all('dd')[9].a.get('href')            # 第一章地址
        classify_name = soup.find('div', { 'class': 'con_top' }).find_all('a')[2].string                # 分类名称
        
        return {
            'authorName': author_name,
            'bookName': book_name,
            'lastUpdateTime': last_update_time,
            'bookIntro': book_intro,
            'bookCoverUrl': book_cover_url,
            'firstChapterUrl': first_chapter_url,
            'classifyName': classify_name,
        }

    def get_chapter_list(self):
        # 获取 html 
        html = get(self.target_url)

        # 解析 html
        soup = BeautifulSoup(html, 'lxml')
        dd_list = soup.find('div', {'id': 'list'}).find_all('dd')[9:]
        chapter_list = []
        for dd in dd_list:
            chapter_name = dd.a.string          # 章节名称
            chapter_url = dd.a.get('href')      # 章节url地址
            chapter_list.append({
                'id': gene_id(),
                'chapterName': chapter_name,
                'chapterUrl': chapter_url,
            })     

        return chapter_list                           

    def get_chapter_content(self):
        # 获取 html 
        html = get(self.target_url)

        # 解析 html
        soup = BeautifulSoup(html, 'lxml')
        # 章节标题
        chapter_title = soup.find('div', { 'class': 'bookname' }).h1.string   
        # 章节内容      
        p_list = soup.find('div', { 'id': 'content' }).contents                     
        chapter_content = ''
        for p in p_list:
            chapter_content += p.string
        # 上一章节url地址
        prev_chapter_url = soup.find('div', { 'class': 'bottem1' }).find_all('a')[1].get('href')        
        if '.html' not in prev_chapter_url:
            prev_chapter_url = None
        # 下一章节url地址
        next_chapter_url = soup.find('div', { 'class': 'bottem1' }).find_all('a')[3].get('href')        
        if '.html' not in next_chapter_url:
            next_chapter_url = None
        
        return {
            'chapterTitle': chapter_title,
            'chapterContent': chapter_content,
            'prevChapterUrl': prev_chapter_url,
            'nextChapterUrl': next_chapter_url,
        }
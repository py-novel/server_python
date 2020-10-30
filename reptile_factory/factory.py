from urllib.parse import urlparse

from reptile_factory.reptiles.qingdou_reptile import Qingdou
from reptile_factory.reptiles.biquge5200_reptile import Biquge5200

class ReptileFactory(object):
    def __init__(self, target_url = None):
        self.target_url = target_url
        self.domains = {
            'www.biquge5200.cc': Biquge5200(target_url),
            'www.qingdou.net': Qingdou(target_url),  
        }

    def get_reptile(self):
        parsed_result = urlparse(self.target_url)
        domain = parsed_result.hostname
        return self.domains[domain]

    def get_novels_by_keyword(self, keyword):
        for reptile in self.domains.values():
            novel_list = reptile.get_novel_list(keyword)
            if len(novel_list) > 0:
                break
        return novel_list

    # 阅读小说切换源时调用该方法
    def get_novel_by_author_and_bookname(self, **kw):
        author_name = kw['author_name']
        book_name = kw['book_name']
        if self.target_url is None:
            self.target_url = kw['origin']
        reptile = self.get_reptile()
        novel_list = reptile.get_novel_list(book_name)

        novel = None
        for n in novel_list:
            if n['authorName'] == author_name:
                novel = n
                break
        return novel



        

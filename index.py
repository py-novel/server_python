from reptile_factory.factory import ReptileFactory

# 根据关键词查询小说列表
reptile_factory = ReptileFactory()
novel_list = reptile_factory.get_novels_by_keyword('九灯和善')
print(novel_list)

# 查询小说详情
# target_url = 'https://www.biquge5200.cc/75_75847/'
# reptile_factory = ReptileFactory(target_url)
# reptile = reptile_factory.get_reptile()
# novel_intro = reptile.get_novel_intro()
# print(novel_intro)

# 查询小说章节列表
# target_url = 'https://www.biquge5200.cc/75_75847/'
# reptile_factory = ReptileFactory(target_url)
# reptile = reptile_factory.get_reptile()
# chapter_list = reptile.get_chapter_list()
# print(len(chapter_list))
# print(chapter_list[:10])

# 查询小说章节内容
# target_url = 'https://www.biquge5200.cc/75_75847/146728646.html'
# reptile_factory = ReptileFactory(target_url)
# reptile = reptile_factory.get_reptile()
# chapter_content = reptile.get_chapter_content()
# print(chapter_content)

# 切换源
# target_url = 'https://www.biquge5200.cc/'
# reptile_factory = ReptileFactory()
# reptile_factory.get_novel_by_author_and_bookname(author_name='月半云遮', book_name='余年不庆', origin=target_url)
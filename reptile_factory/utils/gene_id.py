import random

# 测试生成30位时间在0-1毫秒
def gene_id(length = 10):
    capital_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_letter = 'abcdefghijklmnopqrstuvwxyz'
    figure = '0123456789'
    char_list = list(capital_letter) + list(small_letter) + list(figure)
    random.shuffle(char_list)   # 打乱顺序

    id = ''
    while length > 0:
        id += random.choice(char_list)
        length = length - 1

    return id
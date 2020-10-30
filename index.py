#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, abort, request, jsonify

from reptile_factory.factory import ReptileFactory

app = Flask(__name__)

# 根据关键字查询小说列表
# @param keyword {string} 关键词
@app.route('/novels', methods=['GET'])
def get_novel_list():
    if not request.args or 'keyword' not in request.args:
        return jsonify({ 'code': '9999', 'message': '查询关键字不能为空', 'data': None })
    
    reptile_factory = ReptileFactory()
    novel_list = reptile_factory.get_novels_by_keyword(request.args['keyword'])
    return jsonify({ 'code': '0000', 'message': '查询小说列表成功', 'data': novel_list })

# 查询小说详情，包括作者名、书名、封面url地址、更新时间、简介、第一章url地址、分类名称
# @param url {string} 小说url地址
@app.route('/novel', methods=['GET'])
def get_novel():
    if not request.args or 'url' not in request.args:
        return jsonify({ 'code': '9999', 'message': '小说url地址不能为空', 'data': None })

    reptile_factory = ReptileFactory(request.args['url'])
    reptile = reptile_factory.get_reptile()
    novel = reptile.get_novel_intro()
    return jsonify({ 'code': '0000', 'message': '查询小说介绍成功', 'data': novel })

# 查询小说章节列表
# @param url {string} 小说url地址
@app.route('/chapters', methods=['GET'])
def get_chapter_list():
    if not request.args or 'url' not in request.args:
        return jsonify({ 'code': '9999', 'message': '小说url地址不能为空', 'data': None })

    reptile_factory = ReptileFactory(request.args['url'])
    reptile = reptile_factory.get_reptile()
    chapter_list = reptile.get_chapter_list()
    return jsonify({ 'code': '0000', 'message': '查询小说章节列表成功', 'data': chapter_list })

# 查询小说章节内容，包括章节标题、章节内容、上一章节url地址、下一章节url地址
# @param url {string} 章节url地址
@app.route('/chapter', methods=['GET'])
def get_chapter():
    if not request.args or 'url' not in request.args:
        return jsonify({ 'code': '9999', 'message': '小说章节url地址不能为空', 'data': None })

    reptile_factory = ReptileFactory(request.args['url'])
    reptile = reptile_factory.get_reptile()
    chapter = reptile.get_chapter_content()
    return jsonify({ 'code': '0000', 'message': '查询小说章节内容成功', 'data': chapter })

if __name__ == "__main__":
    app.run(debug=True)
# -*- coding: utf-8 -*-
# 需要 exts 目錄下的 sphinx.search.py
from sphinx.search import SearchLanguage
# 使用結巴套件執行中文分詞, 使用前必須先安裝結巴分詞套件
# https://github.com/fxsjy/jieba
import jieba

class SearchChinese(SearchLanguage):
    lang = 'zh'

    def init(self, options):
        print ("Start to execute zh.py")

    def split(self, input):
        return jieba.cut(input.encode("utf8"),cut_all=True) 

    def word_filter(self, stemmed_word):
        return len(stemmed_word) > 1
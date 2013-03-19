# -*- coding: utf-8 -*- 

def setup(app):
    # 本程式在 Sphinx conf.py 中, 以延伸程式導入, 需要位於 exts 目錄下的 sphinx.search.py 與 zh.py
    import sphinx.search as search
    import zh
    search.languages["zh_TW"] = zh.SearchChinese
#coding: utf-8

from googlesearch import GoogleSearch

class ExpandSearch:
    def __init__(self):
        pass
    
    def get_expand(self, word='keyword'):
        gs = GoogleSearch()
        gs.search(word)
        return gs.get_articles()




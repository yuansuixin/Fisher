# -*- coding: utf-8 -*-

def is_isbn_or_key(word):
    # isbn  isbn13  13个0到9的数字组成
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_q = word.replace('-','')
    if '-' in word and len(short_q)==10 and short_q.isdigit():
        isbn_or_key = 'isbn'
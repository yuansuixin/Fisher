# -*- coding: utf-8 -*-


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.isbn = book['isbn']
        self.pages = book['pages']

    @property
    def intro(self):
        '''
        过滤掉作者，出版社，价格为null的情况
        :return:
        '''
        intros = filter(lambda x:True if x else False,
                        [self.author, self.publisher, self.price])
        return ' / '.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]



class _BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword':keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'price': data['price'],
            'summary': data['summary'],
            'image': data['image'] or '',
            'author': '、'.join(data['author'])
        }
        return book
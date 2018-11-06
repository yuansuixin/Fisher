from app.models.gift import Gift
from app.view_models.book import BookViewModel
from . import web


__author__ = '七月'


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return 'hello'


@web.route('/personal')
def personal_center():
    pass

from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('genre', ['Фантастика','Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_successfully(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Приключения Шерлока Холмса')
        collector.set_book_genre('Приключения Шерлока Холмса', genre)

        assert collector.get_book_genre('Приключения Шерлока Холмса') == genre

    def test_get_books_with_specific_genre_successfully(self):
        collector = BooksCollector()

        collector.add_new_book('Семь смертей Эвелины Хардкасл')
        collector.add_new_book('Чужак')
        collector.add_new_book('Лисьи броды')

        collector.set_book_genre('Семь смертей Эвелины Хардкасл', 'Фантастика')
        collector.set_book_genre('Чужак', 'Ужасы')
        collector.set_book_genre('Лисьи Броды', 'Детективы')

        books_by_genre = collector.get_books_with_specific_genre('Фантастика')

        assert books_by_genre == ['Семь смертей Эвелины Хардкасл']

    def test_get_books_genre_successfully(self):
        collector = BooksCollector()

        collector.add_new_book('Рыцарь семи королевств')
        collector.set_book_genre('Рыцарь семи королевств', 'Фантастика')

        books_genre = collector.get_books_genre()

        assert books_genre == {'Рыцарь семи королевств': 'Фантастика'}

    def test_get_books_for_children_return_successfully(self):
        collector = BooksCollector()

        collector.add_new_book('Губка Боб')
        collector.add_new_book('Шрек')
        collector.add_new_book('Синистер')
        collector.add_new_book('Дюна')

        collector.set_book_genre('Губка Боб', 'Комедии')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.set_book_genre('Синистер', 'Ужасы')
        collector.set_book_genre('Дюна', 'Роман')

        children_books = collector.get_books_for_children()

        assert children_books == ['Губка Боб', 'Шрек']

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')

        assert collector.get_list_of_favorites_books() == ['Шерлок Холмс']

    def test_delete_book_from_favorits_successfully(self):
        collector = BooksCollector()

        collector.add_new_book('Граница')
        collector.add_book_in_favorites('Граница')

        collector.delete_book_from_favorites('Граница')

        assert collector.get_list_of_favorites_books() == []

    def test_add_new_book_with_41_char_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('ХолмсХолмсХолмсХолмсХолмсХолмсХолмсХолмсс')

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_with_0_char_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('')

        assert len(collector.get_books_genre()) == 0

    def test_add_book_in_favorites_cannot_add_exist_book(self):

        collector = BooksCollector()


        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')

        assert len(collector.get_list_of_favorites_books()) == 1
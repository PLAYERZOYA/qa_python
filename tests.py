import pytest

from main import BooksCollector

books = [
    ["Гордость и предубеждение и зомби", "Комедии"],
    ["Оно", "Ужасы"],
    ["Зов Ктулху", "Ужасы"],
    ["Собака Баскервилей", "Детективы"],
    ["shrek", "Мультфильмы"],
    ["Мы", "Фантастика"],
]


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
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_get_book_genre_output_book_genre(self):

        collector = BooksCollector()
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Комедии")
        assert collector.get_book_genre("Гордость и предубеждение и зомби") == "Комедии"

    def test_set_books_genre_add_genre(self):

        collector = BooksCollector()

        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Комедии")
        assert collector.books_genre["Гордость и предубеждение и зомби"] == "Комедии"

    @pytest.mark.parametrize("name,book_genre", books)
    def test_get_books_with_specific_genre_output_books_with_specific_genre(self, name, book_genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, book_genre)
        assert collector.get_books_with_specific_genre(book_genre) == [name]

    def test_get_books_genre_output_books_genre(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    @pytest.mark.parametrize("name,book_genre", books)
    def test_get_books_for_children_output_books_without_age_rating(self, name):

        collector = BooksCollector()

        collector.add_new_book(name)
        assert collector.get_books_for_children() == [
            "Гордость и предубеждение и зомби",
            "Ходячий замок",
            "Мы",
        ]

    @pytest.mark.parametrize("name,book_genre", books)
    def test_get_books_for_children_output_books_without_genre_age_rating_books(self, name, book_genre):

        collector = BooksCollector()

        collector.add_new_book(name)

        assert "Оно" not in collector.get_books_for_children()


    def test_add_book_in_favorites_add_one_book_from_books_genre(self):

        collector = BooksCollector()
        collector.add_new_book("1984")
        collector.add_book_in_favorites("1984")

        assert collector.favorites == ["1984"]

    def test_delete_book_from_favorites_delete_book_from_favorites(self):

        collector = BooksCollector()

        collector.add_new_book("1984")
        collector.add_book_in_favorites("1984")
        collector.delete_book_from_favorites("1984")
        assert collector.favorites == []

    def test_get_list_of_favorites_books_get_favorites(self):

        collector = BooksCollector()
        collector.get_list_of_favorites_books()
        assert collector.favorites == []

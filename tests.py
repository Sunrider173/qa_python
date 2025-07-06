from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        """Проверка добавления двух книг."""
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_name_too_long_not_added(self):
        """Проверка, что книга с именем длиннее 40 символов не добавляется."""
        collector = BooksCollector()
        collector.add_new_book('Очень длинное название книги, которое точно больше 40 символов')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_duplicate_not_added(self):
        """Проверка, что дубликат книги не добавляется."""
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')  
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid_genre_added(self):
        """Проверка установки допустимого жанра для книги."""
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_set_book_genre_invalid_genre_not_added(self):
        """Проверка, что несуществующий жанр не устанавливается."""
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Роман')  
        assert collector.get_book_genre('1984') == ''

    def test_get_books_with_specific_genre_correct_list_returned(self):
        """Проверка получения книг по указанному жанру."""
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('Шерлок')
        collector.set_book_genre('1984', 'Фантастика')
        collector.set_book_genre('Шерлок', 'Детективы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['1984']

    def test_get_books_for_children_no_age_rating_returned(self):
        """Проверка, что возвращаются только книги без возрастного рейтинга."""
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('Шерлок')
        collector.add_new_book('Ну, погоди!')
        collector.set_book_genre('1984', 'Фантастика')
        collector.set_book_genre('Шерлок', 'Детективы')
        collector.set_book_genre('Ну, погоди!', 'Мультфильмы')
        assert collector.get_books_for_children() == ['1984', 'Ну, погоди!']

    def test_add_book_in_favorites_added_once(self):
        """Проверка добавления книги в избранное (без дублирования)."""
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('1984')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_removed(self):
        """Проверка удаления книги из избранного."""
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert '1984' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_correct_list_returned(self):
        """Проверка получения списка избранных книг."""
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('Шерлок')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('Шерлок')
        assert collector.get_list_of_favorites_books() == ['1984', 'Шерлок']
    
    def test_add_book_in_favorites_if_book_not_in_books_genre_not_added(self):
        """Проверка, что нельзя добавить в избранное книгу, которой нет в books_genre."""
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0    
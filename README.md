# qa_python
1.  test_get_book_genre_output_book_genre проверяет, что жанр книги установлен
2. test_set_books_genre_add_genre проверяет соответствие книги ее жанру 
3. test_get_books_with_specific_genre_output_books_with_specific_genre проверяет, что выводится книга с конкретным жанром
4. test_get_books_genre_output_books_genre проверяет, что выводится словарь books_genre
5. test_get_books_for_children_output_books_without_age_rating проверяет, что книги для детей выводятся без рейтинга
6. test_get_books_for_children_output_books_without_genre_age_rating_books проверяет, что в книгах для детей не выводятся книги с возрастным рейтингом
7. test_add_book_in_favorites_add_one_book_from_books_genre проверяет, что книги добавляются в список избранных книг
8. test_delete_book_from_favorites_delete_book_from_favorites проверяет, что книги удаляются из списка избранных книг
9. test_get_list_of_favorites_books_get_favorites проверяет, что список избранных книг выводится корректно
10. test_add_new_book_add_empty_string проверяет, что пустая строка не добавляется в books_genre
11. test_add_new_book_add_lenght_1 проверяет, что книга из 1 символа добавляется в books_genre
12. test_add_new_book_add_lenght_39 проверяет, что книга из 39 символов добавляется в books_genre
13. test_add_new_book_add_lenght_40 проверяет, что книга из 40 символов добавляется в books_genre
14. test_add_new_book_add_lenght_41 проверяет, что книга из 41 символа НЕ добавляется в books_genre
15. test_add_new_book_add_repeat_adding_book проверяет, что книга не добавляется повторно в books_genre
16. test_add_book_in_favorites_add_one_book_not_from_books_genre проверяет, что книга не добавляется в список избранных, если ее нет в books_genre
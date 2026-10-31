# qa_python
В проекте были написаны автотесты для приложения BooksCollector
# автотесты
1. test_add_new_book_add_two_books — Успешное добавление двух разных книг в коллекцию.
2. test_set_book_genre_successfully —  Успешное проставление всех 5 валидных жанров для книги.
3. test_get_books_with_specific_genre_successfully — Успешное получение списка книг, отфильтрованных по конкретному жанру.
4. test_get_books_genre_successfully — Успешное получение всего словаря с книгами и их жанрами.
5. test_get_books_for_children_return_successfully — Проверка фильтрации книг для детей (отсекаются жанры с возрастным ограничением и несуществующие жанры).
6. test_add_book_in_favorites_add_one_book — Успешное добавление книги в список Избранного.
7. test_delete_book_from_favorites_successfully — Успешное удаление книги из списка Избранного.
8. test_add_new_book_with_41_characters_not_added —  Книга с длиной названия 41 символ не добавляется в коллекцию.
9. test_add_new_book_with_0_char_not_added —  Книга с пустой строкой вместо названия (0 символов) не добавляется в коллекцию.
10. test_add_book_in_favorites_cannot_add_exist_book — Повторное добавление одной и той же книги в Избранное не создает дубликат
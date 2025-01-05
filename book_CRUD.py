def create_book(redis_client, book_id, title, author, year, price):
    book_key = f"book:{book_id}" 
    redis_client.hset(book_key, mapping={
        "title": title,
        "author": author,
        "year": year,
        "price": price
    })
    return f"Book '{title}' has been added to the library."


def read_book(redis_client, book_id=None):
    if book_id:
        book_key = f"book:{book_id}"
        if redis_client.exists(book_key):
            book = redis_client.hgetall(book_key)
            return f"Book details (ID: {book_id}): {book}"
        else:
            return f"No book found with ID: {book_id}"
    else:
        keys = redis_client.keys("book:*")
        if keys:
            books = []
            for key in keys:
                book = redis_client.hgetall(key)
                books.append(book)
            return f"List of books in the library:\n" + "\n".join(str(book) for book in books)
        else:
            return "The library currently has no books."


def update_book(redis_client, book_id, field, new_value):
    book_key = f"book:{book_id}"
    if redis_client.exists(book_key):
        redis_client.hset(book_key, field, new_value)
        return f"Updated '{field}' of book ID {book_id} to '{new_value}'."
    else:
        return f"No book found with ID: {book_id} to update."


def delete_book(redis_client, book_id):
    book_key = f"book:{book_id}"
    if redis_client.exists(book_key):
        redis_client.delete(book_key)
        return f"Book ID {book_id} has been deleted from the library."
    else:
        return f"No book found with ID: {book_id} to delete."

from save_all_books import save_all_books

def remove_book(all_books):
    isbn = int(input("Enter the ISBN of the book to remove: "))
    for i, book in enumerate(all_books):
        if book['isbn'] == isbn:
            del all_books[i]
            save_all_books(all_books)
            print("Book removed successfully.")
            return all_books

    print("Book with the given ISBN not found.")
    return all_books

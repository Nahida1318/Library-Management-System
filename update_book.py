from save_all_books import save_all_books

def update_book(all_books):
    isbn = int(input("Enter the ISBN of the book to update: "))
    for book in all_books:
        if book['isbn'] == isbn:
            print("Book found. Enter new details:")
            book['title'] = input("Enter new title: ") or book['title']
            book['author'] = input("Enter new author: ") or book['author']
            book['year'] = int(input("Enter new publishing year: ") or book['year'])
            book['price'] = int(input("Enter new price: ") or book['price'])
            book['quantity'] = int(input("Enter new quantity: ") or book['quantity'])

            save_all_books(all_books)
            print("Book updated successfully.")
            return all_books

    print("Book with the given ISBN not found.")
    return all_books

from save_all_books import save_all_books


def add_books(all_books):
    title=input("Enter book title:")
    author=input("Enter author name:")
    isbn=int(input("Enter ISBN number:"))
    year=int(input("Enter publishing year number:"))
    price=int(input("Enter book price:"))
    quantity=int(input("Enter quantity number:"))

    book={
        "title":title,
        "author":author,
        "isbn":isbn,
        "year":year,
        "price":price,
        "quantity":quantity,
    }

    all_books.append(book)
    save_all_books(all_books)

    print("Books added successfully.")

    return all_books

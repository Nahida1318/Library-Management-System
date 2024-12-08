def view_all_books(all_books):
    if all_books !=[]:
        print("\nBook list :")
        for book in all_books:
            print(f"Title:{book['title']}|Author:{book['author']}|ISBN:{book['isbn']}|Year:{book['year']}|Price:{book['price']}|Quantity:{book['quantity']}")
    else:
        print("no book found in All Books file.")
    print("\n")

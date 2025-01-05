import tkinter as tk
from tkinter import messagebox
from connect_redis import get_redis_connection
from book_CRUD import create_book, read_book, update_book, delete_book

# Initialize Redis connection
redis_client = get_redis_connection()

if not redis_client:
    print("Failed to connect to Redis. Exiting...")
    exit()


# GUI Wrappers for CRUD Operations
def create_book_gui():
    def submit():
        book_id = entry_id.get()
        title = entry_title.get()
        author = entry_author.get()
        year = entry_year.get()
        price = entry_price.get()
        result = create_book(redis_client, book_id, title, author, year, price)
        messagebox.showinfo("Result", f"{result}")
        create_window.destroy()

    create_window = tk.Toplevel(root)
    create_window.title("Create a New Book")

    tk.Label(create_window, text="Book ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(create_window)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(create_window, text="Title:").grid(row=1, column=0, padx=10, pady=5)
    entry_title = tk.Entry(create_window)
    entry_title.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(create_window, text="Author:").grid(row=2, column=0, padx=10, pady=5)
    entry_author = tk.Entry(create_window)
    entry_author.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(create_window, text="Year:").grid(row=3, column=0, padx=10, pady=5)
    entry_year = tk.Entry(create_window)
    entry_year.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(create_window, text="Price:").grid(row=4, column=0, padx=10, pady=5)
    entry_price = tk.Entry(create_window)
    entry_price.grid(row=4, column=1, padx=10, pady=5)

    tk.Button(create_window, text="Submit", command=submit).grid(row=5, column=0, columnspan=2, pady=10)


def read_book_gui():
    def submit():
        book_id = entry_id.get()
        result = read_book(redis_client, book_id)
        messagebox.showinfo("Books", result)
        read_window.destroy()

    read_window = tk.Toplevel(root)
    read_window.title("Read Book Information")

    tk.Label(read_window, text="Book ID (leave blank for all books):").grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(read_window)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(read_window, text="Submit", command=submit).grid(row=1, column=0, columnspan=2, pady=10)


def update_book_gui():
    def submit():
        book_id = entry_id.get()
        field = entry_field.get()
        new_value = entry_value.get()
        result = update_book(redis_client, book_id, field, new_value)
        messagebox.showinfo("Result", result)
        update_window.destroy()

    update_window = tk.Toplevel(root)
    update_window.title("Update Book")

    tk.Label(update_window, text="Book ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(update_window)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(update_window, text="Field (title/author/year/price):").grid(row=1, column=0, padx=10, pady=5)
    entry_field = tk.Entry(update_window)
    entry_field.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(update_window, text="New Value:").grid(row=2, column=0, padx=10, pady=5)
    entry_value = tk.Entry(update_window)
    entry_value.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(update_window, text="Submit", command=submit).grid(row=3, column=0, columnspan=2, pady=10)


def delete_book_gui():
    def submit():
        book_id = entry_id.get()
        result = delete_book(redis_client, book_id)
        messagebox.showinfo("Result", result)
        delete_window.destroy()

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Book")

    tk.Label(delete_window, text="Book ID:").grid(row=0, column=0, padx=10, pady=5)
    entry_id = tk.Entry(delete_window)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(delete_window, text="Submit", command=submit).grid(row=1, column=0, columnspan=2, pady=10)


# Main GUI
root = tk.Tk()
root.title("Redis Library Management")
root.geometry("400x400")

tk.Label(root, text="Redis Library Management", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Create a New Book", command=create_book_gui, width=30).pack(pady=5)
tk.Button(root, text="Read Book Information", command=read_book_gui, width=30).pack(pady=5)
tk.Button(root, text="Update a Book", command=update_book_gui, width=30).pack(pady=5)
tk.Button(root, text="Delete a Book", command=delete_book_gui, width=30).pack(pady=5)
tk.Button(root, text="Exit", command=root.quit, width=30).pack(pady=10)

root.mainloop()

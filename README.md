## python_library_collection_management_system
Library Collection Management System Program using Python

# Python CRUD Application for Library Collection Management

A Python application for managing the data of a library's book collection, as well as any book borrowing system that library has, using Create, Read, Update, and Delete (CRUD) operations. 

**Target Users:**

This application is designed for both librarians and guests within a library to facilitate the library's book borrowing system (both by allowing any guest to view the library's book collection in advance, and by allowing a librarian to edit the library's borrow list with ease), as well as to assist librarians in managing the library's book collection.

## Features

* **Book Collection Management: Manage a library's book collection using CRUD functions**
    * **Create:**
        * Add new books to the collection, by inputing book data such as Book ID, Name, Author, Category, Genre, ISBN, Publication Year, Available Copies, and Rented Copies 
        * Checks if the inputed book name is identical to another book from within the collection.
    * **Read:**
        * Display book collection.
    * **Update:**
        * Change any data within book collection (except for Book ID).
    * **Delete:**
        * Remove books from within book collection.
* **Borrow System Management: Manage a library's book borrowing system using CRUD functions**
    * **Create:**
        * Add new borrow transactions to borrow list, by inputing book data such as Borrow ID, Customer Name, Book ID, Book Name, Copies Rented, and Due Date (by Days)
    * **Read:**
        * Display borrow lis.
    * **Update:**
        * Change any data within the borrow list (except for Borrow ID).
        * Ensure that changes within Book ID will also cause changes to Book Name and vice-versa.
    * **Delete:**
        * Remove borrow transactions from borrow list.
* **Security:**
    * Implement user authentication in the form of a login page and a username-password system to control access to different CRUD operations.
    * Create, Update, and Delete functions are available only for librarians, while the Read function is also available for guests

## Installation

1. **Prerequisites:**
    * Python (at least version 3.12.3)

2. **Installation:**
   Clone this repository using this code: 
    ```bash
    git clone https://github.com/faishalhanan/python_library_collection_management_system.git
    ```
   then, switch your active directory to this project's directory using this code:
    ```bash
    cd python_library_collection_management_system
    ```
   then, run this application using this code:
    ```bash
    python main.py
    ```

## Contributing
Feel free to submit an issue whenever you encounter any errors or problems while using this application, or if you feel like there is any room for improvement. If you wish to open a pull request, feel free to send it to faishalhanan@gmail.com.

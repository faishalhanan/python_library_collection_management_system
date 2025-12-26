# Capstone Project #1
# Faishal Hananta Aji
# JCDSBSDAM-31

##############################################################################################################################################################

# Book data:
# | Book ID | Name | Author | Category | Genre | ISBN | Publication Year | Available Copies | Rented | 

book_data_regular = [
    {'book_id': '001', 'book_name': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'category': 'Novel', 'genre': 'Southern Gothic', 
     'isbn': '9780061120084', 'year': '1960', 'copies_avail': '3', 'copies_rented': '0'}, 

    {'book_id': '002', 'book_name': 'Crime and Punishment', 'author': 'Fyodor Dostoevsky', 'category': 'Novel', 'genre': 'Psychological Thriller', 
     'isbn': '9780140449136', 'year': '1866', 'copies_avail': '2', 'copies_rented': '0'}, 

    {'book_id': '003', 'book_name': 'The C Programming Language', 'author': 'Kernighan & Ritchie', 'category': 'Non-fiction', 'genre': 'Computer Science', 
     'isbn': '9780131103627', 'year': '1988', 'copies_avail': '3', 'copies_rented': '0'},

    {'book_id': '004', 'book_name': 'Introduction to Algorithms', 'author': 'Cormen et al.', 'category': 'Non-fiction', 'genre': 'Computer Science', 
     'isbn': '9780262033848', 'year': '2009', 'copies_avail': '1', 'copies_rented': '0'}, 
    
    {'book_id': '005', 'book_name': 'Batman: The Killing Joke', 'author': 'Alan Moore', 'category': 'Comic', 'genre': 'Superhero', 
     'isbn': '0930289455', 'year': '1988', 'copies_avail': '1', 'copies_rented': '0'}, 
     
    {'book_id': '006', 'book_name': 'The Art of Listening', 'author': 'Erich Fromm', 'category': 'Non-fiction', 'genre': 'Psychology', 
     'isbn': '9780094738904', 'year': '1994', 'copies_avail': '3', 'copies_rented': '0'}, 

    {'book_id': '007', 'book_name': 'Fahrenheit 451', 'author': 'Ray Bradbury', 'category': 'Novel', 'genre': 'Dystopian', 
     'isbn': '9780743247221', 'year': '1953', 'copies_avail': '2', 'copies_rented': '0'} 
]

book_data_test = [
    {'book_id': '001', 'book_name': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'category': 'Novel', 'genre': 'Southern Gothic', 
     'isbn': '9780061120084', 'year': '1960', 'copies_avail': '2', 'copies_rented': '1'}, 

    {'book_id': '002', 'book_name': 'Crime and Punishment', 'author': 'Fyodor Dostoevsky', 'category': 'Novel', 'genre': 'Psychological Thriller', 
     'isbn': '9780140449136', 'year': '1866', 'copies_avail': '2', 'copies_rented': '0'}, 

    {'book_id': '003', 'book_name': 'The C Programming Language', 'author': 'Kernighan & Ritchie', 'category': 'Non-fiction', 'genre': 'Computer Science', 
     'isbn': '9780131103627', 'year': '1988', 'copies_avail': '3', 'copies_rented': '0'},

    {'book_id': '004', 'book_name': 'Introduction to Algorithms', 'author': 'Cormen et al.', 'category': 'Non-fiction', 'genre': 'Computer Science', 
     'isbn': '9780262033848', 'year': '2009', 'copies_avail': '1', 'copies_rented': '0'}, 
    
    {'book_id': '005', 'book_name': 'Batman: The Killing Joke', 'author': 'Alan Moore', 'category': 'Comic', 'genre': 'Superhero', 
     'isbn': '0930289455', 'year': '1988', 'copies_avail': '1', 'copies_rented': '0'}, 
     
    {'book_id': '006', 'book_name': 'The Art of Listening', 'author': 'Erich Fromm', 'category': 'Non-fiction', 'genre': 'Psychology', 
     'isbn': '9780094738904', 'year': '1994', 'copies_avail': '2', 'copies_rented': '1'}, 

    {'book_id': '007', 'book_name': 'Fahrenheit 451', 'author': 'Ray Bradbury', 'category': 'Novel', 'genre': 'Dystopian', 
     'isbn': '9780743247221', 'year': '1953', 'copies_avail': '1', 'copies_rented': '1'} 
]

# Borrow data:
# | Borrow ID | Customer Name | Book ID | Book Name | Copies Rented | Due Date (Days) |

borrow_data_regular = []

borrow_data_test = [
    {'borrow_id': '001', 'customer': 'Ahmad Ramadhan', 'book_id': '001', 'book_name': 'To Kill a Mockingbird', 
     'copies_rented': 1, 'due_date': 5},
    
    {'borrow_id': '002', 'customer': 'Nanda Hakim', 'book_id': '006', 'book_name': 'The Art of Listening', 
     'copies_rented': 1, 'due_date': 3},

    {'borrow_id': '003', 'customer': 'Gita Lestari', 'book_id': '007', 'book_name': 'Fahrenheit 451', 
     'copies_rented': 1, 'due_date': 7}
]

barlength = 149

user = {
    'username': ['admin'], 
    'password': ['123456']
    }

book_data = book_data_regular
borrow_data = borrow_data_regular

##############################################################################################################################################################

def show(name):
    for item in name:
        print(item)

def middle_text(name):
    return str((' '*((barlength//2)-(len(name)//2))) + name)

def header():
    print('='*barlength)
    print(middle_text('Welcome to our library!'))
    print('='*barlength)
    print()

def footer():
    print()
    print('='*barlength)

def int_book_id(book_id):
    int_book_id = 0
    count = len(book_id)
    for i in book_id:
        int_book_id += (int(i)*(10**(count-1)))
        count -= 1
    return int_book_id

# | Book ID | Name | Author | Category | Genre | ISBN | Publication Year | Copies | Rented | 

def print_book_data(all=True, index=None): 
    if all == True: 
        print('-'*barlength)
        print(f'| {'Book ID':<7} | {'Name':<30} | {'Author':<19} | {'Category':<11} | {'Genre':<22} | {'ISBN':<13} | {'Year':<4} | {'Available':<9} | {'Rented':<6} |')
        print('-'*barlength)
        for i in range(len(book_data)):
            print(f'| {book_data[i]['book_id']:<7} | {book_data[i]['book_name']:<30} | {book_data[i]['author']:<19} | {book_data[i]['category']:<11} | {book_data[i]['genre']:<22} | {book_data[i]['isbn']:<13} | {book_data[i]['year']:<4} | {book_data[i]['copies_avail']:<9} | {book_data[i]['copies_rented']:<6} |')
        print('-'*barlength)
        print()
        return
    else:
        if type(index) == int:
            if abs(index) > len(book_data):
                print('Index untuk print_book_data terlalu besar')
                return
            else: 
                print('-'*barlength)
                print(f'| {'Book ID':<7} | {'Name':<30} | {'Author':<19} | {'Category':<11} | {'Genre':<22} | {'ISBN':<13} | {'Year':<4} | {'Available':<9} | {'Rented':<6} |')
                print('-'*barlength)
                print(f'| {book_data[index]['book_id']:<7} | {book_data[index]['book_name']:<30} | {book_data[index]['author']:<19} | {book_data[index]['category']:<11} | {book_data[index]['genre']:<22} | {book_data[index]['isbn']:<13} | {book_data[index]['year']:<4} | {book_data[index]['copies_avail']:<9} | {book_data[index]['copies_rented']:<6} |')
                print('-'*barlength)
                print()
                return       

# | Borrow ID | Customer Name | Book ID | Book Name | Copies Rented | Due Date (Days) |

def print_borrow_data(all=True, index=None):
    if all == True: 
        if borrow_data == []:
            print('-'*barlength)
            print(middle_text('Borrow list is empty'))
            print('-'*barlength)
            print()
            return
        else:
            print('-'*barlength)
            print(f'| {'Borrow ID':<9} | {'Customer':<47} | {'Book ID':<7} | {'Book Name':<39} | {'Copies Rented':<13} | {'Due Date (Days)':<15} |')
            print('-'*barlength)
            for i in range(len(borrow_data)):
                print(f'| {borrow_data[i]['borrow_id']:<9} | {borrow_data[i]['customer']:<47} | {borrow_data[i]['book_id']:<7} | {borrow_data[i]['book_name']:<39} | {borrow_data[i]['copies_rented']:<13} | {borrow_data[i]['due_date']:<15} |')
            print('-'*barlength)
            print()
            return
    else:
        if type(index) == int:
            if abs(index) > len(borrow_data):
                print('Index untuk print_borrow_data terlalu besar')
                return
            else: 
                print('-'*barlength)
                print(f'| {'Borrow ID':<9} | {'Customer':<47} | {'Book ID':<7} | {'Book Name':<39} | {'Copies Rented':<13} | {'Due Date (Days)':<15} |')
                print('-'*barlength)
                print(f'| {borrow_data[index]['borrow_id']:<9} | {borrow_data[index]['customer']:<47} | {borrow_data[index]['book_id']:<7} | {borrow_data[index]['book_name']:<39} | {borrow_data[index]['copies_rented']:<13} | {borrow_data[index]['due_date']:<15} |')
                print('-'*barlength)
                print()
                return 

##############################################################################################################################################################

def program():
    program_input = 0
    while True: 
        header()
        print(middle_text('Main Menu'))
        print()
        print(str((' '*61) + '1. Login'))
        print(str((' '*61) + '2. See our book collection!'))
        print(str((' '*61) + '3. Exit'))
        print()
        while True:
            program_input = input(middle_text('Please choose a selection: '))
            if program_input == '1':
                footer()
                login_page()
                break
            elif program_input == '2':
                footer()
                viewmenu_logout()
                break
            elif program_input == '3':
                print(middle_text('Thank you for visiting!'))
                footer()
                return
            else:
                print(middle_text('Please choose within the selection'))
            

def viewmenu_logout():
    viewmenu_top = [
            '='*barlength,
            middle_text('View Book Collection'),
            '='*barlength,
            ' '
            ]
    show(viewmenu_top)
    print_book_data()
    print(middle_text('-'*17))
    print(middle_text('View Menu: '))
    print(str((' '*66) + '1. Exit'))
    print()
    print(middle_text('-'*17))
    print()
    while True:
        viewmenu_logout_input = input(middle_text('Please choose a selection: '))
        if viewmenu_logout_input == '1':
            footer()
            return
        else:
            print(middle_text('Please choose within the selection'))


def login_page():
    while True: 
        header()
        print(middle_text('Login'))
        user_input = str(input((' '*59) + f'{'Username':<17} : '))
        pass_input = str(input((' '*59) + f'{'Password':<17} : '))
        if (user_input in user['username']): 
            if (pass_input in user['password']): 
                username = user_input
                footer()
                mainmenu_login(username)
                break
            else:
                print(middle_text('Login failed'))
                continue_input = str(input((' '*55) + f'{'Do you still wish to login (Yes/No)':<35} : ')).capitalize()
                if continue_input == 'Yes':
                    footer()
                elif continue_input == 'No':
                    footer()
                    return
                else:
                    print(middle_text('Please enter either Yes or No'))
                    footer()
        else: 
            print(middle_text('Login failed'))
            continue_input = str(input((' '*55) + f'{'Do you still wish to login (Yes/No)':<35} : ')).capitalize()
            if continue_input == 'Yes':
                footer()
            elif continue_input == 'No':
                footer()
                return
            else:
                print(middle_text('Please enter either Yes or No'))
                footer()


def mainmenu_login(username):
    while True:
        global using_regulardata
        global book_data
        global borrow_data

        header()
        print(middle_text('Main Menu'))
        print()
        print(middle_text('Welcome, ' + str(username)))
        print()
        print(str((' '*62) + '1. View book collection'))
        print(str((' '*62) + '2. Edit book collection'))
        print(str((' '*62) + '3. Borrow data'))

        if using_regulardata == True:
            print(str((' '*62) + '4. Switch to test collection'))
        else:
            print(str((' '*62) + '4. Switch to real library collection'))

        print(str((' '*62) + '5. Logout'))
        print()
        while True:
            mainmenu_input = input(middle_text('Please choose a selection: '))
            if mainmenu_input == '1':
                footer()
                viewmenu_login()
                break
            elif mainmenu_input == '2':
                footer()
                editmenu()
                break
            elif mainmenu_input == '3':
                footer()
                borrowmenu()
                break
            elif mainmenu_input == '4':
                
                if using_regulardata == False:
                    book_data = book_data_regular
                    borrow_data = borrow_data_regular
                    print(middle_text('Switched from test data to real library collection data'))
                    using_regulardata = True
                    dummy_input = input(middle_text('Press any key to continue '))
                else:
                    book_data_regular = book_data
                    book_data = book_data_test
                    borrow_data_regular = borrow_data
                    borrow_data = borrow_data_test
                    print(middle_text('Switched from real library collection data to test data'))
                    using_regulardata = False
                    dummy_input = input(middle_text('Press any key to continue '))
                   
                footer()
                break
            elif mainmenu_input == '5':
                footer()
                return
            else:
                print(middle_text('Please choose within the selection')) 


def viewmenu_login():
    viewmenu_login_top = [
            '='*barlength,
            middle_text('View Book Collection'),
            '='*barlength,
            ' '
            ]
    show(viewmenu_login_top)
    print_book_data()
    print(middle_text('-'*17))
    print(middle_text('View Menu: '))
    print(str((' '*66) + '1. Exit'))
    print()
    print(middle_text('-'*17))
    print()
    while True:
        viewmenu_login_input = input(middle_text('Please choose a selection: '))
        if viewmenu_login_input == '1':
            footer()
            return
        else:
            print(middle_text('Please choose within the selection'))


def editmenu():
    while True:
        editmenu_top = [
                '='*barlength,
                middle_text('Edit Book Collection'),
                '='*barlength,
                ' '
                ]
        show(editmenu_top)
        print_book_data()
        print(middle_text('-'*29))
        print(middle_text('Edit Menu: '))
        print(str((' '*60) + '1. Add books to storage'))
        print(str((' '*60) + '2. Delete books from storage'))
        print(str((' '*60) + '3. Edit book data'))
        print(str((' '*60) + '4. Exit Edit Menu'))
        print()
        print(middle_text('-'*29))
        print()
        while True:
            editmenu_input = input(middle_text('Please choose a selection: '))
            if editmenu_input == '1':
                footer()
                editmenu_add()
                break
            elif editmenu_input == '2':
                footer()
                editmenu_del()
                break
            elif editmenu_input == '3': 
                footer()
                editmenu_edit()
                break
            elif editmenu_input == '4': 
                footer()
                return
            else:
                print(middle_text('Please choose within the selection'))


def editmenu_add():
    editmenu_add_top = [
            '='*barlength,
            middle_text('Add Book to Collection'),
            '='*barlength,
            ' '
            ]
    show(editmenu_add_top)
    print_book_data()

    while True:      
        # | Book ID | Name | Author | Category | Genre | ISBN | Publication Year | Available | Rented | 
        print(middle_text('-'*31))
        last_book_id = int_book_id(book_data[-1]['book_id'])

        print(middle_text('Please add the following data: '))
        new_book_id = '0'*(3-len(str(last_book_id))) + str(last_book_id+1)
        new_book_name = str(input((' '*59) + f'{'Book Name':<17} : '))

        while len(new_book_name) > 30:
            print(middle_text('The names of the books stored within this database must have 30 or less characters'))
            new_book_name = str(input((' '*59) + f'{'Book Name':<17} : '))

        is_duplicate = False
        dupli_confirm = 'No'
        for i in range(len(book_data)):
            if book_data[i]['book_name'] == new_book_name:
                is_duplicate = True
                break
        
        while is_duplicate == True:
            print(middle_text('This book shares a name with another book within the collection'))
            dupli_confirm = str(input(middle_text('Did you intend to add another copy of a pre-existing book to the collection? (Yes/No) '))).title()
            while True:
                if dupli_confirm == 'Yes':
                    print(middle_text('Please use the "Edit book data" option instead'))
                    break
                elif dupli_confirm == 'No':
                    print(middle_text('Please add the name of the book you wish to add,'))
                    print(middle_text('or if you are trying to add a different version or edition of a pre-existing book,'))
                    print(middle_text('please add the version or edition of that book to differentiate it from the book already in this collection'))
                    old_book_name = new_book_name
                    new_book_name = str(input((' '*59) + f'{'Book Name':<17} : '))
                    if new_book_name == old_book_name:
                        break
                    else:
                        is_duplicate = False
                        break
                else:
                    print(middle_text('Please answer with Yes or No'))
                    dupli_confirm = str(input(middle_text('Did you intend to add another copy of a pre-existing book to the collection? (Yes/No) '))).title()
            if dupli_confirm == 'Yes':
                break
        
        if is_duplicate == False:
            new_author = str(input((' '*59) + f'{'Author':<17} : '))
            new_category = str(input((' '*59) + f'{'Category':<17} : '))
            new_genre = str(input((' '*59) + f'{'Genre':<17} : '))

            while True:
                new_isbn = str(input((' '*59) + f'{'ISBN':<17} : '))
                avail_input = '0123456789'
                isbn_confirm = True
                if len(new_isbn) == 10 or len(new_isbn) == 13:
                    for item in new_isbn:
                        if item not in avail_input:
                            isbn_confirm = False
                            break
                    if isbn_confirm == True:
                        break
                    else:
                        print(middle_text('Please insert proper ISBN (10 or 13 characters)'))
                else:
                    print(middle_text('Please insert proper ISBN (10 or 13 characters)'))

            new_year = str(input((' '*59) + f'{'Publication Year':<17} : '))

            while True:
                new_copies_avail = input((' '*59) + f'{'Available Copies':<17} : ')
                avail_input = '0123456789'
                new_copies_avail_confirm = True
                for item in new_copies_avail:
                    if item not in avail_input:
                        new_copies_avail_confirm = False
                        break
                if new_copies_avail_confirm == True:
                    new_copies_avail = int(new_copies_avail)
                    break
                else:
                    print(middle_text('Please insert an integer'))

            while True:
                new_copies_rented = input((' '*59) + f'{'Rented Copies':<17} : ')
                avail_input = '0123456789'
                new_copies_rented_confirm = True
                for item in new_copies_rented:
                    if item not in avail_input:
                        new_copies_rented_confirm = False
                        break
                if new_copies_rented_confirm == True:
                    new_copies_rented = int(new_copies_rented)
                    break
                else:
                    print(middle_text('Please insert an integer'))

            book_data.append({})
            book_data[-1]['book_id'] = new_book_id
            book_data[-1]['book_name'] = new_book_name
            book_data[-1]['author'] = new_author
            book_data[-1]['category'] = new_category
            book_data[-1]['genre'] = new_genre
            book_data[-1]['isbn'] = new_isbn
            book_data[-1]['year'] = new_year
            book_data[-1]['copies_avail'] = new_copies_avail
            book_data[-1]['copies_rented'] = new_copies_rented

            print_book_data(all=False,index=-1)
            while True:
                add_confirm = str(input(middle_text('Do you wish to add this book (Yes/No) '))).title()
                if add_confirm == 'Yes':
                    break
                elif add_confirm == 'No':
                    del book_data[-1]
                    break
                else:
                    print(middle_text('Please answer with Yes or No'))          

            print()
            print(middle_text('-'*31))
            print()
            print_book_data()

        while True:
            more_confirm = str(input(middle_text('Do you wish to add more books (Yes/No) '))).title()
            if more_confirm == 'Yes':
                break
            elif more_confirm == 'No':
                footer
                return
            else:
                print(middle_text('Please answer with Yes or No'))


def editmenu_del():
    editmenu_del_top = [
            '='*barlength,
            middle_text('Delete Book from Collection'),
            '='*barlength,
            ' '
            ]
    show(editmenu_del_top)
    print_book_data()
    
    id_del = ' '
    del_confirm = 'No'
    more_confirm = 'Yes'
    while True: 
        avail_confirm = False
        id_del = str(input(middle_text('Enter the ID of the book you wish to delete: ')))
        print()
        id_count = 0
        for i in range((len(book_data))):
            if book_data[i]['book_id'] == id_del:
                print_book_data(all=False, index=i)
                avail_confirm = True
                while True:
                    del_confirm = str(input(middle_text('Do you wish to delete this book (Yes/No) '))).title()
                    if del_confirm == 'Yes':
                        del book_data[i]
                        break
                    elif del_confirm == 'No':
                        break
                    else:
                        print(middle_text('Please answer with Yes or No'))                    
                print()
                print_book_data()     
            if del_confirm == 'Yes':
                break

        if avail_confirm == False:
            print(middle_text('There is no book with that ID in this collection')) 

        while True:
            more_confirm = str(input(middle_text('Do you still wish to delete a book (Yes/No) '))).title()
            if more_confirm == 'Yes':
                break
            elif more_confirm == 'No':
                footer()
                return
            else:
                print(middle_text('Please answer with Yes or No'))


def editmenu_edit():
    editmenu_edit_top = [
            '='*barlength,
            middle_text('Edit Book Data'),
            '='*barlength,
            ' '
            ]
    show(editmenu_edit_top)
     
    while True:
        print_book_data()
        book_id_find = False
        id_edit = str(input(middle_text('Enter the ID of the book whose data you wish to edit: ')))
        for i in range((len(book_data))):
            if book_data[i]['book_id'] == id_edit:
                while book_data[i]['book_id'] == id_edit:
                    print(middle_text(f'Edit book: {book_data[i]['book_name']}'))
                    while True:
                        print(middle_text('Book data: Name, Author, Category, Genre, ISBN, Publication Year, Available, Rented')) 
                        data_edit = str(input(middle_text('Enter the data you wish to edit: '))).title()
                        if data_edit == 'Book Id':
                            print('Book ID cannot be edited')
                        elif data_edit == 'Name' :
                            book_name_edit = str(input(middle_text('Enter new book name: '))).title()
                            book_name_old = book_data[i]['book_name']
                            book_data[i]['book_name'] = book_name_edit
                            print()
                            print_book_data(all=False, index=i)
                            while True:
                                edit_confirm = str(input(middle_text('Is this edit correct (Yes/No) '))).title()
                                if edit_confirm == 'Yes':
                                    break
                                elif edit_confirm == 'No':
                                    book_data[i]['book_name'] = book_name_old
                                    break
                                else:
                                    print(middle_text('Please answer with Yes or No'))  
                            break
                        elif data_edit == 'Author' :
                            author_edit = str(input(middle_text('Enter new book author: '))).title()
                            author_old = book_data[i]['author']
                            book_data[i]['author'] = author_edit
                            print()
                            print_book_data(all=False, index=i)
                            while True:
                                edit_confirm = str(input(middle_text('Is this edit correct (Yes/No) '))).title()
                                if edit_confirm == 'Yes':
                                    break
                                elif edit_confirm == 'No':
                                    book_data[i]['author'] = author_old
                                    break
                                else:
                                    print(middle_text('Please answer with Yes or No'))  
                            break
                        elif data_edit == 'Category' :
                            category_edit = str(input(middle_text('Enter new book category: '))).title()
                            category_old = book_data[i]['category']
                            book_data[i]['category'] = category_edit
                            print()
                            print_book_data(all=False, index=i)
                            while True:
                                edit_confirm = str(input(middle_text('Is this edit correct (Yes/No) '))).title()
                                if edit_confirm == 'Yes':
                                    break
                                elif edit_confirm == 'No':
                                    book_data[i]['category'] = category_old
                                    break
                                else:
                                    print(middle_text('Please answer with Yes or No'))
                            break
                        elif data_edit == 'Genre' :
                            genre_edit = str(input(middle_text('Enter new book genre: '))).title()
                            genre_old = book_data[i]['genre']
                            book_data[i]['genre'] = genre_edit
                            print()
                            print_book_data(all=False, index=i)
                            while True:
                                edit_confirm = str(input(middle_text('Is this edit correct (Yes/No) '))).title()
                                if edit_confirm == 'Yes':
                                    break
                                elif edit_confirm == 'No':
                                    book_data[i]['genre'] = genre_old
                                    break
                                else:
                                    print(middle_text('Please answer with Yes or No'))
                            break
                        elif data_edit == 'Isbn' :
                            while True:
                                isbn_edit = str(input(middle_text('Enter new book ISBN: ')))
                                avail_input = '0123456789'
                                isbn_confirm = True
                                if len(isbn_edit) == 10 or len(isbn_edit) == 13:
                                    for item in isbn_edit:
                                        if item not in avail_input:
                                            isbn_confirm = False
                                            break
                                    if isbn_confirm == True:
                                        break
                                    else:
                                        print(middle_text('Please insert proper ISBN (10 or 13 characters)'))
                                else:
                                    print(middle_text('Please insert proper ISBN (10 or 13 characters)'))
                            isbn_old = book_data[i]['isbn']
                            book_data[i]['isbn'] = isbn_edit
                            print()
                            print_book_data(all=False, index=i)
                            while True:
                                edit_confirm = str(input(middle_text('Is this edit correct (Yes/No) '))).title()
                                if edit_confirm == 'Yes':
                                    break
                                elif edit_confirm == 'No':
                                    book_data[i]['isbn'] = isbn_old
                                    break
                                else:
                                    print(middle_text('Please answer with Yes or No'))
                            break
                        elif data_edit == 'Publication Year' :
                            year_edit = str(input(middle_text('Enter new book publication year: ')))
                            year_old = book_data[i]['year']
                            book_data[i]['year'] = year_edit
                            print()
                            print_book_data(all=False, index=i)
                            while True:
                                edit_confirm = str(input(middle_text('Is this edit correct (Yes/No) '))).title()
                                if edit_confirm == 'Yes':
                                    break
                                elif edit_confirm == 'No':
                                    book_data[i]['year'] = year_old
                                    break
                                else:
                                    print(middle_text('Please answer with Yes or No'))
                            break
                        elif data_edit == 'Available' :
                            while True:
                                copies_avail_edit = input(middle_text('Enter number of available books: '))
                                avail_input = '0123456789'
                                copies_avail_confirm = True
                                for item in copies_avail_edit:
                                    if item not in avail_input:
                                        copies_avail_confirm = False
                                        break
                                if copies_avail_confirm == 'True':
                                    copies_avail_edit = int(copies_avail_edit)
                                    break
                                else:
                                    print(middle_text('Please insert an integer'))
                            copies_avail_old = book_data[i]['copies_avail']
                            book_data[i]['copies_avail'] = copies_avail_edit
                            print()
                            print_book_data(all=False, index=i)
                            while True:
                                edit_confirm = str(input(middle_text('Is this edit correct (Yes/No) '))).title()
                                if edit_confirm == 'Yes':
                                    break
                                elif edit_confirm == 'No':
                                    book_data[i]['copies_avail'] = copies_avail_old
                                    break
                                else:
                                    print(middle_text('Please answer with Yes or No'))
                            break
                        elif data_edit == 'Rented' :
                            while True:
                                copies_rented_edit = input(middle_text('Enter number of rented books: '))
                                avail_input = '0123456789'
                                copies_rented_confirm = True
                                for item in copies_rented_edit:
                                    if item not in avail_input:
                                        copies_rented_confirm = False
                                        break
                                if copies_rented_confirm == 'True':
                                    copies_rented_edit = int(copies_rented_edit)
                                    break
                                else:
                                    print(middle_text('Please insert an integer'))
                            copies_rented_old = book_data[i]['copies_rented']
                            book_data[i]['copies_rented'] = copies_rented_edit
                            print()
                            print_book_data(all=False, index=i)
                            while True:
                                edit_confirm = str(input(middle_text('Is this edit correct (Yes/No) '))).title()
                                if edit_confirm == 'Yes':
                                    break
                                elif edit_confirm == 'No':
                                    book_data[i]['copies_rented'] = copies_rented_old
                                    break
                                else:
                                    print(middle_text('Please answer with Yes or No'))
                            break
                        else: 
                            print(middle_text('Please choose from the selection'))

                    print_book_data()

                    while True: 
                        continue_confirm = str(input(middle_text('Is there anything you still wish to edit? (Yes/No) '))).capitalize()
                        if continue_confirm == 'Yes':
                            break
                        elif continue_confirm == 'No':
                            break
                        else: 
                            print(middle_text('Please enter either Yes or No'))

                    if continue_confirm == 'No':
                        break

                book_id_find = True
                break

        if book_id_find == False: 
            print(middle_text('There is no book with that ID in this collection'))

        while True:
            if book_id_find == True:
                more_confirm = str(input(middle_text('Is there any other book in the collection that you wish to edit? (Yes/No) '))).title()
            else:
                more_confirm = str(input(middle_text('Are there any books in the collection that you wish to edit? (Yes/No) '))).title()
            
            if more_confirm == 'Yes':
                break
            elif more_confirm == 'No':
                return
            else: 
                print(middle_text('Please enter either Yes or No'))


def borrowmenu():
    while True:
        borrowmenu_top = [
                '='*barlength,
                middle_text('Book Borrowing'),
                '='*barlength,
                ' '
                ]
        show(borrowmenu_top)
        print(middle_text('-'*29))
        print(middle_text('Borrow Menu: '))
        print(str((' '*60) + '1. Check borrow data'))
        print(str((' '*60) + '2. Edit borrow data'))
        print(str((' '*60) + '3. Exit Borrow Menu'))
        print()
        print(middle_text('-'*29))
        print()
        while True: 
            borrowmenu_input = input(middle_text('Please choose a selection: '))
            if borrowmenu_input == '1':
                footer()
                viewmenu_borrow()
                break
            elif borrowmenu_input == '2':
                footer()
                editmenu_borrow()
                break
            elif borrowmenu_input == '3': 
                footer()
                return
            else:
                print(middle_text('Please choose within the selection'))


def viewmenu_borrow():
    viewmenu_borrow_top = [
            '='*barlength,
            middle_text('View Borrow List'),
            '='*barlength,
            ' '
            ]
    show(viewmenu_borrow_top)
    print_borrow_data()
    print(middle_text('-'*17))
    print(middle_text('View Menu: '))
    print(str((' '*66) + '1. Exit'))
    print()
    print(middle_text('-'*17))
    print()
    while True:
        viewmenu_borrow_input = input(middle_text('Please choose a selection: '))
        if viewmenu_borrow_input == '1':
            footer()
            return
        else:
            print(middle_text('Please choose within the selection'))


def editmenu_borrow():
    while True:
        editmenu_borrow_top = [
                '='*barlength,
                middle_text('Edit Borrow List'),
                '='*barlength,
                ' '
                ]
        show(editmenu_borrow_top)
        print_borrow_data()
        print(middle_text('-'*29))
        print(middle_text('Edit Menu: '))
        print(str((' '*60) + '1. Add entry to borrow list'))
        print(str((' '*60) + '2. Delete entry from borrow list'))
        print(str((' '*60) + '3. Edit borrow list'))
        print(str((' '*60) + '4. Exit Edit Menu'))
        print()
        print(middle_text('-'*29))
        print()
        while True:
            editmenu_borrow_input = input(middle_text('Please choose a selection: '))
            if editmenu_borrow_input == '1':
                print(middle_text('WIP'))
                footer()
                editmenu_borrow_add()
                break
            elif editmenu_borrow_input == '2':
                print(middle_text('WIP'))
                footer()
                editmenu_borrow_del()
                break
            elif editmenu_borrow_input == '3': 
                print(middle_text('WIP'))
                footer()
                editmenu_borrow_edit()
                break
            elif editmenu_borrow_input == '4': 
                footer()
                return
            else:
                print(middle_text('Please choose within the selection'))


def editmenu_borrow_add(): 
    editmenu_borrow_add_top = [
            '='*barlength,
            middle_text('Add Book to Collection'),
            '='*barlength,
            ' '
            ]
    show(editmenu_borrow_add_top)

    while True:      
#         Borrow data:
#       | Borrow ID | Customer Name | Book ID | Book Name | Copies Rented | Due Date (Days) |
#        'borrow_id'    'customer'   'book_id' 'book_name' 'copies_rented'    'due_date'

        print_book_data()
        print(middle_text('-'*31))

        if borrow_data == []:
            new_borrow_id = '001'
        else:
            last_borrow_id = int_book_id(borrow_data[-1]['borrow_id'])
            new_borrow_id = '0'*(3-len(str(last_borrow_id))) + str(last_borrow_id+1)

        print(middle_text('Please add the following data: '))
        while True:
            new_book_id = str(input((' '*59) + f'{'Book ID':<17} : '))
            book_id_list = []
            for item in book_data:
                book_id_list.append(item['book_id'])
            if new_book_id not in book_id_list:
                print(middle_text('There is no book with this ID in this collection'))
            else:
                break

        new_book_name = None
        for item in book_data:
            if item['book_id'] == new_book_id:
                new_book_name = item['book_name']
        print((' '*59) + f'{'Book Name':<17} : {new_book_name}')

        while True:
            new_copies_rented = input((' '*59) + f'{'Rented Copies':<17} : ')
            avail_input = '0123456789'
            new_copies_rented_confirm = True
            for item in new_copies_rented:
                if item not in avail_input:
                    new_copies_rented_confirm = False
                    break
            if new_copies_rented_confirm == True:
                new_copies_rented = int(new_copies_rented)
                break
            else:
                print(middle_text('Please insert an integer'))

        while True:
            new_due_date = input((' '*59) + f'{'Due Date (Days)':<17} : ')
            avail_input = '0123456789'
            new_due_date_confirm = True
            for item in new_due_date:
                if item not in avail_input:
                    new_due_date_confirm = False
                    break
            if new_due_date_confirm == True:
                new_due_date = int(new_due_date)
                break
            else:
                print(middle_text('Please insert an integer'))

        new_customer = str(input((' '*59) + f'{'Customer Name':<17} : '))
        
        borrow_data.append({})
        borrow_data[-1]['borrow_id'] = new_borrow_id
        borrow_data[-1]['customer'] = new_customer
        borrow_data[-1]['book_id'] = new_book_id
        borrow_data[-1]['book_name'] = new_book_name
        borrow_data[-1]['copies_rented'] = new_copies_rented
        borrow_data[-1]['due_date'] = new_due_date

        print_borrow_data(all=False,index=-1)
        while True:
            add_confirm = str(input(middle_text('Do you wish to add this transaction (Yes/No) '))).title()
            if add_confirm == 'Yes':
                break
            elif add_confirm == 'No':
                del book_data[-1]
                break
            else:
                print(middle_text('Please answer with Yes or No'))          

        print()
        print(middle_text('-'*31))
        print()
        print_borrow_data()

        while True:
            more_confirm = str(input(middle_text('Do you wish to add more transactions (Yes/No) '))).title()
            if more_confirm == 'Yes':
                break
            elif more_confirm == 'No':
                footer
                return
            else:
                print(middle_text('Please answer with Yes or No'))


def editmenu_borrow_del():
    editmenu_borrow_del_top = [
            '='*barlength,
            middle_text('Delete Borrow Data'),
            '='*barlength,
            ' '
            ]
    show(editmenu_borrow_del_top)
    print_borrow_data()
    
    id_del = ' ' 
    del_confirm = 'No'
    more_confirm = 'Yes'
    while True: 
        avail_confirm = False
        id_del = str(input(middle_text('Enter the ID of the borrow transaction you wish to delete: ')))
        for i in range(len(borrow_data)):
            if borrow_data[i]['borrow_id'] == id_del:
                avail_confirm = True
                print()
                print_borrow_data(all=False, index=i)
                while True:
                    del_confirm = str(input(middle_text('Do you wish to delete this transaction (Yes/No) '))).title()
                    if del_confirm == 'Yes':
                        del borrow_data[i]
                        break
                    elif del_confirm == 'No':
                        break
                    else:
                        print(middle_text('Please answer with Yes or No'))                    
                print()
                print_borrow_data()     
            if del_confirm == 'Yes':
                break

        if avail_confirm == False:
            print(middle_text('There is no transaction with that ID in this collection')) 

        while True:
            more_confirm = str(input(middle_text('Do you still wish to delete a transaction (Yes/No) '))).title()
            if more_confirm == 'Yes':
                break
            elif more_confirm == 'No':
                footer()
                return
            else:
                print(middle_text('Please answer with Yes or No'))


def editmenu_borrow_edit():
    editmenu_borrow_edit_top = [
            '='*barlength,
            middle_text('Edit Book Data'),
            '='*barlength,
            ' '
            ]
    show(editmenu_borrow_edit_top)
     
    while True:
        print_borrow_data()
        borrow_id_find = False
        id_edit = str(input(middle_text('Enter the ID of the transaction whose data you wish to edit: ')))
        for i in range(len(borrow_data)):
            if borrow_data[i]['borrow_id'] == id_edit:
                print_borrow_data(all=False, index=i)
                while True:
                    while True:
#                        Borrow data:
#                      | Borrow ID | Customer Name | Book ID | Book Name | Copies Rented | Due Date (Days) |
#                       'borrow_id'    'customer'   'book_id' 'book_name' 'copies_rented'    'due_date'
                        print(middle_text('Borrow data: Borrow ID, Customer Name, Book ID, Book Name, Copies Rented, Due Date')) 
                        data_edit = str(input(middle_text('Enter the data you wish to edit: '))).title()
                        if data_edit == 'Borrow Id':
                            print(middle_text('Borrow ID cannot be edited'))
                        elif data_edit == 'Customer Name' :
                            customer_edit = str(input(middle_text('Enter new customer name: '))).title()
                            customer_old = borrow_data[i]['customer']
                            borrow_data[i]['customer'] = customer_edit
                            print()
                            print_borrow_data(all=False, index=i)
                            while True:
                                edit_confirm = str(input(middle_text('Is this edit correct (Yes/No) '))).title()
                                if edit_confirm == 'Yes':
                                    break
                                elif edit_confirm == 'No':
                                    borrow_data[i]['customer'] = customer_old
                                    break
                                else:
                                    print(middle_text('Please answer with Yes or No'))  
                            break
                        elif data_edit == 'Book Id' :
                            print(middle_text('Changing Book ID will change the book borrowed in this transaction'))
                            print(middle_text('This will change Book Name'))
                            while True:
                                edit_confirm = str(input(middle_text('Are you sure you want to change books? (Yes/No) '))).title()
                                if edit_confirm == 'Yes':
                                    book_id_edit = str(input(middle_text('Enter new book ID: ')))
                                    book_id_find = False
                                    book_id_old = borrow_data[i]['book_id']
                                    book_name_old = borrow_data[i]['book_name']

                                    for item in book_data:
                                        if item['book_id'] == book_id_edit:
                                            book_id_find = True

                                    if book_id_find == True:
                                        for item in book_data:
                                            if item['book_id'] == book_id_edit:
                                                book_name_edit = item['book_name']
                                        for item in borrow_data:
                                            if item['book_id'] == book_id_old:        
                                                item['book_id'] = book_id_edit
                                                item['book_name'] = book_name_edit
                                                
                                        print()
                                        print_borrow_data(all=False, index=i)
                                        while True:
                                            edit_confirm = str(input(middle_text('Is this edit correct (Yes/No) '))).title()
                                            if edit_confirm == 'Yes':
                                                break
                                            elif edit_confirm == 'No':
                                                borrow_data[i]['book_id'] = book_id_old
                                                borrow_data[i]['book_name'] = book_name_old
                                                break
                                            else:
                                                print(middle_text('Please answer with Yes or No'))
                                    else:
                                        print(middle_text('There is no book with that ID in this collection')) 
                                    break

                                elif edit_confirm == 'No':
                                    break
                                else:
                                    print(middle_text('Please answer with Yes or No')) 
                            break
                        elif data_edit == 'Book Name' :
                            print(middle_text('Changing Book Name will change the book borrowed in this transaction'))
                            print(middle_text('This will change Book ID'))
                            while True:
                                edit_confirm = str(input(middle_text('Are you sure you want to change books? (Yes/No) '))).title()
                                if edit_confirm == 'Yes':
                                    book_name_edit = str(input(middle_text('Enter new book name: ')))
                                    book_name_find = False
                                    book_name_old = borrow_data[i]['book_name']
                                    book_id_old = borrow_data[i]['book_id']
                                    
                                    for item in book_data:
                                        if item['book_name'] == book_name_edit:
                                            book_name_find = True
                                    
                                    if book_name_find == True:
                                        for item in book_data:
                                            if item['book_name'] == book_name_edit:
                                                book_id_edit = item['book_id']
                                        print(middle_text(book_name_old))
                                        print(middle_text(book_id_old))
                                        print(middle_text(book_name_edit))
                                        print(middle_text(book_id_edit))
                                        for item in borrow_data:
                                            if item['book_name'] == book_name_old:        
                                                item['book_name'] = book_name_edit
                                                item['book_id'] = book_id_edit
                                                
                                        print()
                                        print_borrow_data(all=False, index=i)
                                        while True:
                                            edit_confirm = str(input(middle_text('Is this edit correct (Yes/No) '))).title()
                                            if edit_confirm == 'Yes':
                                                break
                                            elif edit_confirm == 'No':
                                                borrow_data[i]['book_name'] = book_name_old
                                                borrow_data[i]['book_id'] = book_id_old
                                                break
                                            else:
                                                print(middle_text('Please answer with Yes or No'))
                                    else:
                                        print(middle_text('There is no book with that name in this collection')) 
                                    break

                                elif edit_confirm == 'No':
                                    break
                                else:
                                    print(middle_text('Please answer with Yes or No'))
                            break
                        elif data_edit == 'Copies Rented' :
                            while True:
                                copies_rented_edit = input(middle_text('Enter number of rented books: '))
                                avail_input = '0123456789'
                                copies_rented_confirm = True
                                for item in copies_rented_edit:
                                    if item not in avail_input:
                                        copies_rented_confirm = False
                                        break
                                if copies_rented_confirm == True:
                                    copies_rented_edit = int(copies_rented_edit)
                                    break
                                else:
                                    print(middle_text('Please insert an integer'))
                            copies_rented_old = borrow_data[i]['copies_rented']
                            borrow_data[i]['copies_rented'] = copies_rented_edit
                            print()
                            print_borrow_data(all=False, index=i)
                            while True:
                                edit_confirm = str(input(middle_text('Is this edit correct (Yes/No) '))).title()
                                if edit_confirm == 'Yes':
                                    break
                                elif edit_confirm == 'No':
                                    borrow_data[i]['copies_rented'] = copies_rented_old
                                    break
                                else:
                                    print(middle_text('Please answer with Yes or No'))
                            break
                        elif data_edit == 'Due Date' or data_edit == 'Due Date (Days)' :
                            while True:
                                due_date_edit = input(middle_text('Enter the new due date: '))
                                avail_input = '0123456789'
                                due_date_confirm = True
                                for item in due_date_edit:
                                    if item not in avail_input:
                                        due_date_confirm = False
                                        break
                                if due_date_confirm == True:
                                    due_date_edit = int(due_date_edit)
                                    break
                                else:
                                    print(middle_text('Please insert an integer'))
                            due_date_old = borrow_data[i]['due_date']
                            borrow_data[i]['due_date'] = due_date_edit
                            print()
                            print_borrow_data(all=False, index=i)
                            while True:
                                edit_confirm = str(input(middle_text('Is this edit correct (Yes/No) '))).title()
                                if edit_confirm == 'Yes':
                                    break
                                elif edit_confirm == 'No':
                                    borrow_data[i]['due_date'] = due_date_old
                                    break
                                else:
                                    print(middle_text('Please answer with Yes or No'))
                            break
                        else: 
                            print(middle_text('Please choose from the selection'))

                    print_borrow_data()

                    while True: 
                        continue_confirm = str(input(middle_text('Is there anything you still wish to edit? (Yes/No) '))).capitalize()
                        if continue_confirm == 'Yes':
                            break
                        elif continue_confirm == 'No':
                            break
                        else: 
                            print(middle_text('Please enter either Yes or No'))

                    if continue_confirm == 'No':
                        break

                borrow_id_find = True
                break

        if borrow_id_find == False: 
            print(middle_text('There is no transaction with that ID in this collection'))

        while True:
            if borrow_id_find == True:
                more_confirm = str(input(middle_text('Is there any other transaction that you wish to edit? (Yes/No) '))).title()
            else:
                more_confirm = str(input(middle_text('Are there any transactions that you wish to edit? (Yes/No) '))).title()
            
            if more_confirm == 'Yes':
                break
            elif more_confirm == 'No':
                return
            else: 
                print(middle_text('Please enter either Yes or No'))

##############################################################################################################################################################

using_regulardata = True
program()

##############################################################################################################################################################


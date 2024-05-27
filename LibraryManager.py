# initialize empty lists, set, and dictionary
Books_list=[]
Authors_set=set()
Book_dict={}

#Add Books
Books_list.append("python Programming")
Authors_set.add("John Smith")
Book_dict["python programming"]= "John Smith"

Books_list.append("Data Structures and Algorithms")
Authors_set.add("Jane Doe")
Book_dict["Data Structures and Algorithms"] = "Jane Doe"

Books_list.append("machine Learning BAsics")
Authors_set.add("Alice Johnson")
Book_dict["Machine Learning Basics"] = "Alis Johnson"

#Search for a books
Search_title=input("Enter the title of the book to search:")
if Search_title in Books_list:
    print(f"Book found Author: {Book_dict[Search_title]}")
else:
    print("Book not found")

#Display all books
print("Lists of books:") 
for book in Books_list:
    print(book)

# Remove a book
remove_title= input("Enter the name of the book to remove or elde ent") 
if remove_title in Books_list:
    remove_author= Book_dict[remove_title]
    Books_list.remove(remove_title)
    Authors_set.remove(remove_author) 
    del Book_dict[remove_title]
    print("Book removed successfully")
    print("Books available:", Books_list)

else:
    print("Book not found") 
       
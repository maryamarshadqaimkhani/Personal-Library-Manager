import streamlit as st 
import json

#load and save library data 

def load_library():
    try:
            with open("library.json", "r") as file:
                 return json.load(file)
    except FileNotFoundError:
        return []

def save_library():
     with open("library.json", "w") as file:
          json.dump(library, file, indent=4)

        # initialize library ss
library = load_library()
     
st.title("Personal Library Manager")
menu = st.sidebar.radio("Select an option", ["View Library", "Add book", "Remove Book", "Search Book", "Save and Exit"])
if menu == "View Library":
        st.sidebar.title("Your Library")
        if library:
                st.table(library)
        else:
                st.write("No Books in your library. Add some books!")

# Add Books
elif menu == "Add Book":      
      st.sidebar("Add a new Book 📗")
      title = st.text_input("Title")
      author = st.text_input("Author")
      year = st.number_input("Year", min_value=2020, max_value=2100, step=1)
      genre = st.text_input("Genre")
      read_status = st.checkbox("Mark as Read ✅")

if st.button("Add Book 📙"):
        library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
        save_library()
        st.success("Book added Successfully!🎉")
        st.rerun()

# Remove books
elif menu == "Remove Book":
      st.sidebar("Remove a book 📖")
      book_titles = [book[title] for book in library]

      if book_titles:
            selected_book = st.selectbox("Select a book to remove", book_titles)
            if st.button("Remove Book"):
                  library = [book for book in library if book["title"] != selected_book]
                  save_library()
                  st.success("Book remove successfully 🎉")
                  st.rerun()
            else:
                  st.warning("No book in your library. Add some books!")

# search book
elif menu == "Search Book":
      st.sidebar("Search a book!")
      search_term = st.text_input("Enter title or author name")

      if st.button("Search"):
            results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
            if results:
                  st.table(results)
            else:
                  st.warning("No book found ❌")

#save and exit 
elif menu == "Save and Exit":
      save_library()
      st.success("Library saved successfully! 🎉")
import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('books.csv', sep=';')

# Link our dataset books with book_titles and isbn_titles
book_titles = df['title'].tolist()  # Column with the book title
isbn_titles = df['isbn'].tolist()  # Column with the book ISBN

# Title of our app
st.title('Rating Prediction')

# Initialize st.session_state if necessary
if 'selected_books' not in st.session_state:
    st.session_state['selected_books'] = []
if 'selected_isbns' not in st.session_state:
    st.session_state['selected_isbns'] = []
if 'input_key' not in st.session_state:
    st.session_state['input_key'] = 0

# Text field to add a new book
new_book = st.text_input('Choose a book:', key=f'book_input_{st.session_state["input_key"]}')

# Button to add the new book to the list
if st.button('Add book') and new_book:
    if new_book not in book_titles:
        st.write(f'Error: The book "{new_book}" is not in the dataset.')
    else:
        st.session_state['selected_books'].append(new_book)

# Text field to add an ISBN (optional)
new_isbn = st.text_input('Enter an ISBN (optional):', key=f'isbn_input_{st.session_state["input_key"]}')

# Button to add the new ISBN to the list
if st.button('Add ISBN') and new_isbn:
    if new_isbn not in isbn_titles:
        st.write(f'Error: The ISBN "{new_isbn}" is not in the dataset.')
    else:
        st.session_state['selected_isbns'].append(new_isbn)

# Display selected books
for book in st.session_state['selected_books']:
    st.write(book)

# Display selected ISBNs
for isbn in st.session_state['selected_isbns']:
    st.write(isbn)

# Prediction button
if st.button('Predict'):
    for book in st.session_state['selected_books']:
        # Model prediction code
        result = "Prediction result"  
        st.write(f'The prediction for the book "{book}" is {result}')
    for isbn in st.session_state['selected_isbns']:
        # Model prediction code
        result = "Prediction result"  
        st.write(f'The prediction for the ISBN "{isbn}" is {result}')

# Refresh button
if st.button('Refresh'):
    st.session_state['selected_books'] = []
    st.session_state['selected_isbns'] = []
    st.session_state['input_key'] += 1

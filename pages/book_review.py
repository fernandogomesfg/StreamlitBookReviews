# Importar as bibliotecas necessárias
import streamlit as st
import pandas as pd

# Configuração da página Streamlit
st.set_page_config(
    page_title="Bestseller Book Reviews",  
    page_icon=":books:",  
    layout="wide",  
    initial_sidebar_state="expanded"  
)

# Carregar os datasets
df_reviews = pd.read_csv('datasets/customer reviews.csv')  
df_top100_books = pd.read_csv('datasets/Top-100 Trending Books.csv')  

# Obter a lista única de títulos de livros
books = df_top100_books['book title'].unique()

# Criar um seletor de caixa de seleção na barra lateral para escolher um livro
book = st.sidebar.selectbox('Livros', books)

# Filtrar o DataFrame do livro selecionado
df_book = df_top100_books[df_top100_books['book title'] == book]

# Filtrar o DataFrame de avaliações para o livro selecionado
df_reviews_f = df_reviews[df_reviews['book name'] == book]

# Obter informações do livro selecionado
book_title = df_book['book title'].iloc[0]
book_genre = df_book['genre'].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"  
book_rating = df_book['rating'].iloc[0]
book_year = df_book['year of publication'].iloc[0]

# Título principal e subtitulo
st.title(book_title)
st.subheader(book_genre)

# Layout em três colunas para exibir as informações do livro
col1, col2, col3 = st.columns(3)

# Exibir as informações do livro em forma de métrica
col1.metric('Preço', book_price)
col2.metric('Classificação', book_rating)
col3.metric('Ano de publicação', book_year)

# Divisor
st.divider()

# Iterar sobre as avaliações do livro e exibir na interface
for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")  
    message.write(row[5])  

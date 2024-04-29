# Importar as bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar a página Streamlit
st.set_page_config(
    page_title="Bestseller Book Reviews",
    page_icon=":books:",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Carregar os datasets
df_reviews = pd.read_csv('datasets/customer reviews.csv')
df_top100_books = pd.read_csv('datasets/Top-100 Trending Books.csv')

# Determinar os valores mínimo e máximo para o controle deslizante de preço
price_min = df_top100_books['book price'].min()
price_max = df_top100_books['book price'].max()

# Adicionar um controle deslizante na barra lateral para filtrar os livros por preço
max_price = st.sidebar.slider('Intervalo de Preço', price_min, price_max, price_max)

# Filtrar os livros com base no preço máximo selecionado pelo usuário
df_books = df_top100_books[df_top100_books['book price'] <= max_price]

# Exibir o DataFrame filtrado na interface Streamlit
# df_books[['book title', 'author', 'year of publication', 'genre', 'book price']]

# Exibir DataFrame df_books com nomes de colunas em maiúsculas e estilização
styled_df_books = df_books[['book title', 'author', 'year of publication', 'genre', 'book price']].rename(columns=str.capitalize).style \
    .set_properties(subset=['Book title', 'Author', 'Genre'], **{'text-align': 'left'}) \
    .set_properties(subset=['Year of publication', 'Book price'], **{'text-align': 'center'}) \
    .bar(subset=['Book price'], color='#5fba7d') \
    .highlight_max(subset=['Year of publication'], color='#7b68ee') \
    .highlight_min(subset=['Year of publication'], color='#cd5c5c') \
    .set_table_styles([{
        'selector': 'th',
        'props': [('text-align', 'center')]
    }])

# Exibir a tabela estilizada na interface Streamlit
st.write(styled_df_books)


# Criar um gráfico de barras mostrando a contagem de livros por ano de publicação
fig = px.bar(df_books['year of publication'].value_counts(), title='Contagem de Livros por Ano de Publicação')

# Criar um histograma mostrando a distribuição de preços dos livros
fig2 = px.histogram(df_books['book price'], title='Distribuição de Preços dos Livros')

# Dividir a tela em duas colunas
col1, col2 = st.columns(2)

# Exibir o gráfico de barras na primeira coluna
col1.plotly_chart(fig)

# Exibir o histograma na segunda coluna
col2.plotly_chart(fig2)

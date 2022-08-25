import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title='Devon Sistemas', page_icon="https://devonsistemas.com.br/manutencao/img/devon-sistemas-favicon.ico", layout = 'wide', initial_sidebar_state = 'auto')

def show_qt_lines(dataframe):
    qt_lines = st.sidebar.slider('Quantas linhas gostaria de visualizar?', min_value = 1, max_value = len(dataframe), step = 1)
    st.write(dataframe.head(qt_lines).style.format(subset = ['Valor'], formatter='{:.2f}'))

def stock_plot(dataframe, category):
    with st.spinner('Carregando'):
        time.sleep(2)
        data_graphic = dataframe.query('Categoria == @category')
        #sns.set(rc={'axes.facecolor':'#87CEEB', 'figure.facecolor':'#87CEEB'})
        #sns.set_theme(style='whitegrid')
        fig, ax = plt.subplots(figsize=(8,6))
        ax = sns.barplot(x = 'Produto', y = 'Quantidade', data = data_graphic)
        ax.set_title(f'Quantidade em estoque dos produtos de {category}', fontsize = 16)
        ax.set_xlabel('Produtos', fontsize = 12)
        ax.tick_params(rotation = 20, axis = 'x')
        ax.set_ylabel('Quantidade', fontsize = 12)
    #st.success('Concluído!')
    
    return fig

#import od data
data = pd.read_csv('estoque.csv')

st.title('Gestão De Estoque\n')
st.write('Analise os produtos em estoque, filtrando por categoria')

#filters for table

checkbox_show_table = st.sidebar.checkbox('Mostrar Tabela')

if checkbox_show_table:
    st.sidebar.markdown('## Filtro para tabela')
    
    categories = list(data['Categoria'].unique())
    categories.append('Todas')
    
    category = st.sidebar.selectbox('Selecione a categoria para apresentar na tabela', options = categories)
    
    if category != 'Todas':
        df_category = data.query('Categoria == @category')
        show_qt_lines(df_category)
    else:
        show_qt_lines(data)

st.sidebar.markdown('## Filtro para gráfico')
category_graphic = st.sidebar.selectbox('Selecione a categoria para apresentar no gráfico', options = data['Categoria'].unique())
graphic = stock_plot(data, category_graphic)
st.pyplot(graphic)
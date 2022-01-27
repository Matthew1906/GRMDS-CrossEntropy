import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

def app():
    funds = pd.read_csv('./dataset/funds.csv')
     # The second one in the .ipynb
    st.write('''
        ### Relationship between Fund Size and it's aspect of return
    ''')

    xs2 = funds.loc[:, 'YTD Return (%)':'10 Years Annualized (%)']
    xs2_option = st.selectbox(
        label = 'Choose the X axis!',
        options = xs2.columns
    )
    ys2 = funds['Fund Size (Mil)'].apply(lambda x:float(''.join(x.replace(',',''))))

    fig2, ax2 = plt.subplots()
    ax2.scatter(xs2[xs2_option], ys2)
    ax2.set_xlabel(xs2_option)
    ax2.set_ylabel('Fund Size (Mil)')

    st.pyplot(fig2)
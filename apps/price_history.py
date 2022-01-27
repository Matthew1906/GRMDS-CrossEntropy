import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

def app():
    prices = pd.read_csv('./dataset/prices_per_day.csv', index_col=[0], parse_dates=True)

    st.write('''
        ### Price history of selected stock
    ''')

    fig4, ax4 = plt.subplots(figsize=(12,6))

    select_stock = st.selectbox(
        label = 'Which stock do you want to check?',
        options = prices['stock_name'].unique()
    )

    selected = prices[prices['stock_name']==select_stock]
    ax4.plot(selected['stock_price'])
    ax4.set_xlabel('Time')
    ax4.set_ylabel('Price')
    ax4.set_title('Stock Price history of' + ' ({})'.format(select_stock))
    st.pyplot(fig4)
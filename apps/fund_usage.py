import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

def app():
    
    # Get Dataframe
    funds = pd.read_csv('./dataset/funds.csv')
    
    # The first one in the .ipynb
    st.write('''
        ### Relationship between Fund usage and it's aspect of return
    ''')

    xs1 = funds.loc[:, '% Alcohol':'% Tobacco']
    ys1 = funds.loc[:, 'YTD Return (%)':'10 Years Annualized (%)']

    xs1_option = st.selectbox(
        label = 'Choose the X axis!',
        options = xs1.columns
    )

    ys1_option = st.selectbox(
        label = 'Choose the Y axis!',
        options = ys1.columns
    )

    fig1, ax1 = plt.subplots()
    not_zero1 = xs1[xs1_option]>0
    ax1.scatter(xs1.loc[not_zero1, xs1_option], ys1.loc[not_zero1, ys1_option])
    ax1.set_xlabel(xs1_option)
    ax1.set_ylabel(ys1_option)
    st.pyplot(fig1)

    # The third one I guess
    cols = ['% Alcohol','% Fossil Fuels','% Small Arms','% Thermal Coal','% Tobacco']
    # Actually imma skip this
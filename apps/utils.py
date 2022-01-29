import pandas as pd
import streamlit as st

@st.cache
def get_funds():
    return pd.read_csv('./datasets/funds.csv')

@st.cache
def get_prices_per_day():
    return pd.read_csv('datasets/prices_per_day.csv', index_col=[0], parse_dates=True)

@st.cache
def get_prices_cats():
    df = pd.read_csv('./datasets/prices_per_cats.csv', parse_dates=['date_time'])
    df.set_index('date_time', inplace=True)
    return df
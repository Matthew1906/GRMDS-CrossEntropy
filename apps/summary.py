# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
    
def app(): 
    sns.set()
    # Get datas
    funds = pd.read_csv('./datasets/funds.csv')
    
    # Bar charts
    col_usage, col_inv = st.columns(2)

    # Fund Usage
    with col_usage:
        st.subheader('Fund Usage')
        st.caption("This graph shows the average percentage of fund allocations based on it's business type")
        fundallocs = ['% Alcohol','% Fossil Fuels','% Small Arms','% Thermal Coal','% Tobacco']
        fig_usage, ax_usage = plt.subplots(figsize=(8,4))
        sns.barplot(x=[1,2,3,4,5],
                y=funds[fundallocs].mean(),
                ax=ax_usage)
        ax_usage.set_xticklabels(fundallocs)
        ax_usage.set_xlabel('Business Type')
        st.pyplot(fig_usage)
    
    # Sustainable Investments
    with col_inv:
        st.subheader('Sustainable Investment')
        st.caption('This graph shows the average allocation of funds for each type of sustainable investments')
        fig_inv, ax_inv = plt.subplots(figsize=(8,4))
        sns.barplot(x=[1,2,3,4],
                y=funds[[
                    'Sustainable Investment by Prospectus',
                    'Sustainable Investment - ESG Fund',
                    'Sustainable Investment - Impact Fund',
                    'Sustainable Investment - Environmental Sector Fund'
                ]].sum(),
                ax=ax_inv)
        ax_inv.set_xticklabels(['Prospectus','ESG','Impact','Environmental'])
        ax_inv.set_xlabel('Sustainable Investment')
        st.pyplot(fig_inv)

    # Returns based on Credit Quality
    st.subheader('Average Credit Quality')
    st.caption('The average return based on credit quality')
    return_types = ['YTD Return (%)', '1 Year Annualized (%)',
        '3 Years Annualized (%)', '5 Years Annualized (%)',
        '10 Years Annualized (%)']
    return_aliases = dict(zip(return_types,['YTD','1Y','3Y','5Y','10Y']))
    returns_creds = funds.groupby('Average Credit Quality').mean()[return_types]
    quality_select = st.select_slider(
        label = 'Select Credit Card Quality!',
        options = returns_creds.index
    )
    returns_creds_cols = st.columns(len(returns_creds.columns))
    for idx, (returns_creds_col, return_type) in enumerate(zip(returns_creds_cols, returns_creds.columns)):
        returns_creds_col.metric('' if idx!=0 else 'Percentage Return',return_aliases[return_type], str(round(returns_creds.loc[quality_select, return_type],2)) +'%')

    # Average Fund growth by category
    prices_cats = pd.read_csv('./datasets/prices_per_cats.csv', parse_dates=['date_time'])
    prices_cats.set_index('date_time', inplace=True)
    st.subheader('Fund Growth by Category')
    st.caption('This graph compares average fund growth by category')
    fig_cats, ax_cats = plt.subplots(figsize=(12,6))
    categories_select = st.multiselect(
        label = 'Select Categories (You can select more than one for comparison!)',
        options = prices_cats.columns,
        default = ['US Equity Large Cap Growth', 'US Equity Large Cap Blend','Global Equity Large Cap', 'Moderate Allocation', 'Target Date']
    )
    plt.plot(prices_cats[categories_select])
    plt.legend(categories_select)
    ax_cats.set_xlabel('Date')
    ax_cats.set_ylabel('Average Stock Price')
    st.pyplot(fig_cats)
    

    


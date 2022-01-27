import streamlit as st
from multiapp import MultiApp
from apps import fund_usage, fund_size, price_history

dashboard = MultiApp()

st.markdown("""
    # GRMDS - Brace for Impact
    ###### by Kevin Bennett Haryono and Matthew Adrianus Mulyono
    This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

dashboard.add_app('Fund Usage vs Return', fund_usage.app)
dashboard.add_app('Fund Size vs Return', fund_size.app)
dashboard.add_app('Price History', price_history.app)
dashboard.run()

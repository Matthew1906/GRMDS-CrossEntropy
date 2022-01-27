import streamlit as st
from multiapp import MultiApp
from apps import fund_usage, fund_report, fund_size

dashboard = MultiApp()

st.markdown("""
    # GRMDS - Brace for Impact
    ## Responsible Investing Dashboard
    ###### by Team CrossEntropy
    This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

dashboard.add_app('Fund Report', fund_report.app)
dashboard.add_app('Fund Usage vs Return', fund_usage.app)
dashboard.add_app('Fund Size vs Return', fund_size.app)
dashboard.run()

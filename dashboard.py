import streamlit as st
import seaborn as sns
from multiapp import MultiApp
from apps import fund_report, summary

sns.set()

dashboard = MultiApp()

st.markdown("""
    # GRMDS - Brace for Impact
    ## Responsible Investing Dashboard
    ###### by Team CrossEntropy
    This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

dashboard.add_app('Summary', summary.app)
dashboard.add_app('Fund Report', fund_report.app)
dashboard.run()

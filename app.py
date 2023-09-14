import streamlit as st
import pandas as pd
view = [100, 150, 300]
sview = pd.Series(view)
st.write('# Youtube view')
st.write('## raw data')
view
st.write('## bar chart')
st.bar_chart(data=view)
sview
# st.bar_chart(data=view, *, x=None, y=None, color=None, width=0, height=0, use_container_width=True)


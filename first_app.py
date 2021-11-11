import streamlit as st
import numpy as np
import pandas as pd

st.title("this is my first streanlit app for galileo!")

x=4

## operaciones para imprimir a pantalla
st.write(x,'square is',x*x)

x,'square is',x*x

"""
# dataframe
"""


st.write('now using dataframes....')

df = pd.DataFrame({
    'column A': [1,2,3,4,5],
    'Column B':['A','B','c','d','e']
})

st.write(df)

"""
# titulo
## Subtitulo
### sub sub titulo
"""

df

"""
## lets use some graphs
"""

chart_df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['A','B','c']
)

st.line_chart(chart_df)

"""
## how about maps
"""
map_df = pd.DataFrame(
    np.random.randn(1000, 2) / [50,50]+[37.76, -122.4],
    columns=['lat','lon']
)
st.map(map_df)

"""
## show me some widgets
"""

"""
## a checkbox
"""

if st.checkbox("show me the dataframe"):
    map_df

"""
## slider test
"""

x=st.slider("select value for x")
x,'square is',x*x

"""
## option group
"""

option = st.selectbox(
    'Wich number do you like best?',
    [1,2,3,4,5,6,7,8,9,10]
)

'You selected option', option

"""
## progressbar
"""
import time
progress_bar_lablel = st.empty()
progress_bar = st.progress(0)
progress_bar2 = st.progress(0)

for i in range(101):
    progress_bar_lablel.text(f'Iteration {i}')
    progress_bar.progress(i)
    time.sleep(0.01)

for i2 in range(101):
    progress_bar2.progress(i2)
    time.sleep(0.01)

option_side = st.sidebar.selectbox('Choose your weapon,',[ 'headgun','machinegun','knife'])
st.sidebar.write('Your weapon of choice is:', option_side)

another_slider = st.sidebar.slider('select the range',
                           0.0,100.0 , (25.0,75.0))

st.sidebar.write('the range selected is:', another_slider)
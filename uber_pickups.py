import streamlit as st
import numpy as np
import pandas as pd
import math

st.title("Uber pickups test")

DATA_SOURCE='https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'



# carga de datos en cache


@st.cache
def download_data():
      datos= (pd.read_csv(DATA_SOURCE).rename(columns={'Lat':'lat', 'Lon':'lon', 'Date/Time':'date'}))
      datos['date'] = pd.to_datetime(datos.date)
      return datos
df= download_data()


# slider por rango de hora

#st.write(df.dtypes.astype(str))
st.sidebar.title("Slider")
slider_hour = st.sidebar.slider('select the hour range',0,23, (8,17))
maximo=max(slider_hour)
minimo=min(slider_hour)
st.sidebar.write('Your hour range is:', slider_hour)

# filtrar data segun slider


df = df[(df['date'].dt.hour >= minimo) & (df['date'].dt.hour <= maximo)]
df_sin_pagineo=df
#st.write(df['date'].hour.astype(str))


"""
## pagineo
"""
page_size=1000
total_pages=math.ceil((len(df)/page_size))
starting_value=0
slider = st.slider('Select the page',1, total_pages )
st.write('page selected',slider,'with limits',(((slider-1)*page_size), (slider*page_size)-1))
df = df.loc[((slider-1)*page_size):(slider*page_size)-1]
df

"""
## mapa
"""
st.map(df)

"""
## grafica de barras
"""
df_sin_pagineo['hour'] = df_sin_pagineo['date'].dt.hour

st.bar_chart(df_sin_pagineo['hour'].value_counts())

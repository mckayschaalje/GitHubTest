import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_kart = pd.read_csv('streamlit_template/data/kart_stats.csv')

# Dropping in the data as a datfram
st.dataframe(df_kart)

# Limiting the columns to five for visualization 1
df_kart_limited = df_kart[['Body','Weight','Acceleration','Ground Speed','Air Speed','Water Handling']]

# Giving Visualization 1 a tite to visually break up the page
st.header('Visualization One: 5 Kart Traits with Highlighting Rules')

# Visualization 1 - highlighting rules
st.dataframe(df_kart_limited.style
             .highlight_max(color='lightgreen', axis=0, subset=['Weight','Acceleration','Ground Speed','Air Speed','Water Handling'])
             .highlight_min(color='red', axis=0, subset=['Weight','Acceleration','Ground Speed','Air Speed','Water Handling'])
)

# Visualization 2 - Bar chart
st.header('Visualzation 2: Area Chart to Show the Relationship between Ground and Air Speed')
st.area_chart(df_kart_limited, x='Ground Speed',y='Air Speed')

# Visualization 3 - Line Chart
st.header('Visualzation 3: Bart Chart to show Acceleration by Kart Body')
st.bar_chart(df_kart_limited, x='Body',y='Acceleration')

# Dynamic Bar Chart
st.header('Visualzation 4: Dynamic Bar Chart')
chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]
df_single_kart = df_single_kart.drop(columns=['Body'])
df_unp_kart = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)
st.bar_chart(df_unp_kart, x='category', y='strength')
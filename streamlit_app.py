import streamlit as st
from functions import topic_search

st.set_page_config(page_title="ReviewAnalyzer Eliott BENOIT")

#sidebar

ModelType = st.sidebar.radio("Choose your model",["Write by hand", "Choose from Dataset"])
nb_topic = st.sidebar.number_input("Number of Topic",min_value=1,max_value=15)

if(ModelType=="Write by hand"):
  st.write("Write by hand")
else:
  st.write("Choose from Dataset")

#main

doc = st.text_area("write your comment below",height=510)

if st.button(label="Search"):
  st.write('OK')



#st.write(topic_search(TEXT, 3, model=model, vect=vect))

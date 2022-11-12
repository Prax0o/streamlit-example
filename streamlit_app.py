import streamlit as st
from functions import topic_search
import pickle as pk

st.set_page_config(page_title="ReviewAnalyzer Eliott BENOIT")

#sidebar

ModelType = st.sidebar.radio("Choose your model",["Write by hand", "Choose from Dataset"])
nb_topic = st.sidebar.number_input("Number of Topic",min_value=1,max_value=15)


if(ModelType=="Write by hand"):
  doc = st.text_area("write your comment below",height=510)
  st.write("Write by hand")
  TEXT = doc
else:
  st.write("Choose from Dataset")

#main

model = pk.load(open('model', 'rb'))
vect = pk.load(open('vect', 'rb'))


if st.button(label="Search"):
  list_topic = topic_search(TEXT, nb_topic, model=model, vectorizer=vect)
  st.write('The topic found are listed below (sort by possibilities) :')
  for topic in list_topic:
    st.write(topic)

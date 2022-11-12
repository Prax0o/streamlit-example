import streamlit as st
import numpy as np
from pandas import DataFrame
from keybert import KeyBERT
# For Flair (Keybert)
from flair.embeddings import TransformerDocumentEmbeddings
import seaborn as sns
# For download buttons
from functionforDownloadButtons import download_button
import os
import json

st.set_page_config(page_title="ReviewAnalyzer Eliott BENOIT")

ModelType = st.sidebar.radio("Choose your model",["write", "choose"])
nb_topic = st.sidebar.number_input("Number of Topic",min_value=1,max_value=15)


doc = st.text_area("rite your comment below",height=510)

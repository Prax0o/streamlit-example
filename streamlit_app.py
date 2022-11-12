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

ModelType = st.radio("Choose your model",["DistilBERT (Default)", "Flair"])

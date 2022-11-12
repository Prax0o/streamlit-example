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

st.title("ReviewAnalyzer")
st.header("")

'''


def _max_width_():
    max_width_str = f"max-width: 1400px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


_max_width_()

c30, c31, c32 = st.columns([2.5, 1, 3])

with c30:
    # st.image("logo.png", width=400)
    st.title("ReviewAnalyzer")
    st.header("")



with st.expander("ℹ️ - About this app", expanded=True):

    st.write("""     
-   texte1
-   texte2 """
    )
    st.markdown("")

st.markdown("## Analyzer")

with st.form(key="my_form"):
    ce, c1, ce, c2, c3 = st.columns([0.07, 1, 0.07, 5, 0.07])
    with c1:
        ModelType = st.radio("Choose your model",["DistilBERT (Default)", "Flair"])
        if ModelType == "Default (DistilBERT)":
            @st.cache(allow_output_mutation=True)
            def load_model():
                return KeyBERT(model=roberta)
            kw_model = load_model()

        else:
            @st.cache(allow_output_mutation=True)
            def load_model():
                return KeyBERT("distilbert-base-nli-mean-tokens")

            kw_model = load_model()

        top_N = st.slider("# of results",min_value=1,max_value=30,value=10)
	
        min_Ngrams = st.number_input("Minimum Ngram",min_value=1,max_value=4)

        StopWordsCheckbox = st.checkbox("Remove stop words")

        use_MMR = st.checkbox("Use MMR",value=True,
            help="You can use Maximal Margin Relevance (MMR) to diversify the results. It creates keywords/keyphrases based on cosine similarity. Try high/low 'Diversity' settings below for interesting variations.",
        )

        Diversity = st.slider("Keyword diversity (MMR only)",
			      value=0.5,min_value=0.0,max_value=1.0, step=0.1,
			      help="""The higher the setting, the more diverse the keywords.      
Note that the *Keyword diversity* slider only works if the *MMR* checkbox is ticked.
""",)

    with c2:
        doc = st.text_area("rite your comment below",height=510,)
        submit_button = st.form_submit_button(label="Search")

if not submit_button:
    st.stop()

if min_Ngrams > max_Ngrams:
    st.warning("min_Ngrams can't be greater than max_Ngrams")
    st.stop()

keywords = kw_model.extract_keywords(doc,keyphrase_ngram_range=(min_Ngrams, max_Ngrams),use_mmr=mmr,
				     stop_words=StopWords,top_n=top_N,diversity=Diversity,)
'''

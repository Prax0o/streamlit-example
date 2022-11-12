
MODEL_FILE = './model'
VECT_FILE = './vect'


#polarite


from textblob import TextBlob

def negative(text):
  negative = False
  testimonial1 = TextBlob(text)
  if testimonial1.sentiment.polarity < 0:
    negative = True
  return negative 


#pretraitement


import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import contractions

tokenizer = RegexpTokenizer(r'\w+')

def tokenize_text(text):
    text_processed = " ".join(tokenizer.tokenize(text))
    return text_processed

import en_core_web_sm
nlp = en_core_web_sm.load(disable=['parser', 'tagger', 'ner'])

lemmatizer = WordNetLemmatizer()

def lemmatize_text(text):
    tokens_tagged = nltk.pos_tag(nltk.word_tokenize(text))
    lemmatized_text_list = list()
    for word, tag in tokens_tagged:
        if tag.startswith('J'):
            lemmatized_text_list.append(lemmatizer.lemmatize(word,'a')) # Lemmatise adjectives. Not doing anything since we remove all adjective
        elif tag.startswith('V'):
            lemmatized_text_list.append(lemmatizer.lemmatize(word,'v')) # Lemmatise verbs
        elif tag.startswith('N'):
            lemmatized_text_list.append(lemmatizer.lemmatize(word,'n')) # Lemmatise nouns
        elif tag.startswith('R'):
            lemmatized_text_list.append(lemmatizer.lemmatize(word,'r')) # Lemmatise adverbs
        else:
            lemmatized_text_list.append(lemmatizer.lemmatize(word)) # If no tags has been found, perform a non specific lemmatisation
    return " ".join(lemmatized_text_list)

def normalize_text(text):
    return " ".join([word.lower() for word in text.split()])

def contraction_text(text):
    return contractions.fix(text)

negative_words = ['not', 'no', 'never', 'nor', 'hardly', 'barely']
negative_prefix = "NOT_"

def get_negative_token(text):
    tokens = text.split()
    negative_idx = [i+1 for i in range(len(tokens)-1) if tokens[i] in negative_words]
    for idx in negative_idx:
        if idx < len(tokens):
            tokens[idx]= negative_prefix + tokens[idx]
    
    tokens = [token for i,token in enumerate(tokens) if i+1 not in negative_idx]
    
    return " ".join(tokens)

from spacy.lang.en.stop_words import STOP_WORDS

def remove_stopwords(text):
    english_stopwords = stopwords.words("english") + list(STOP_WORDS) + ["tell", "restaurant"]
    
    return " ".join([word for word in text.split() if word not in english_stopwords])

def preprocess_text(text):
    text = tokenize_text(text)
    text = lemmatize_text(text)
    text = normalize_text(text)
    text = contraction_text(text)
    text = get_negative_token(text)
    text = remove_stopwords(text)
    return text


#vectorization


import pickle as pk
import numpy as np

topic_nuns = ['atmosphere_sound', 'chicken_menu', 'bad_service', 'pizza_menu', 'delivery', 'long_wait', 'drinks', 'wrong_marketing', 'dirty', 'rude_staff', 'burger_menu', 'over_priced', 'not_tasty', 'not_accessible', 'seasoning']

model = pk.load(open(MODEL_FILE, 'rb'))
vect = pk.load(open(VECT_FILE, 'rb'))

def topic_search(text, nb_topic, model=model, vectorizer=vect):
  text = [text]
  my_vertorizer = vect.transform(text)
  my_model = model.transform(my_vertorizer)
  topics = []
  for i in np.argsort(my_model):
    for j in range(nb_topic):
      topics.append(topic_nuns[i[-j-1]])
  return topics


# 3.2 More Advanced Methods
    # 3.2.1 K-fold Cross Validation
        # Extend the basic train/test split over multiple classifier models

import numpy as np
from sklearn . datasets import fetch_20newsgroups
from sklearn . model_selection import cross_val_score , StratifiedKFold
from sklearn . feature_extraction . text import TfidfVectorizer
from sklearn . naive_bayes import MultinomialNB
from sklearn . pipeline import make_pipeline
from sklearn . svm import SVC
from sklearn . ensemble import RandomForestClassifier

# Load one of the scikit - learn default datasets
data = fetch_20newsgroups ( subset ='all ', categories =[ 'sci . space ', 'comp . graphics '
])
X , y = data . data , data . target

# Define classifiers to evaluate
classifiers = {
" Multinomial Naive Bayes ": MultinomialNB () ,
" Support Vector Machine ": SVC () ,
" Random Forest ": RandomForestClassifier ()
}

# Define the ( stratified ) k- fold cross - validation (k =10)
kfold = StratifiedKFold ( n_splits =10 , shuffle = True , random_state =42)

# Iterate over classifiers
for name , classifier in classifiers . items () :
    pipeline = make_pipeline ( TfidfVectorizer ( stop_words ='english ') , classifier )
    scores = cross_val_score ( pipeline , X , y , cv = kfold , scoring ='accuracy ')
    print (f"{ name }:")
    print (" Cross - validation scores :", scores )
    print (" Average accuracy :", np . mean ( scores ))
    print ()
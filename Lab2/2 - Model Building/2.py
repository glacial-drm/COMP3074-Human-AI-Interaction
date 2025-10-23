# 2 - Model Building
    # First build bag-of-words representation
    # Applying CountVectoriser and TfidTransformer to training data stored in X_train (dataset is split into training and testing first)

    # We train a Logistic Regression model
        # Good form NLP as it's failty simple, relies on strong statistical foundations and is quite fast to train
    # We can use other classifiers, such as MLPClassifier, KNeighboursClassifier and SVC

import os
from sklearn . model_selection import train_test_split
from nltk . corpus import stopwords
from sklearn . feature_extraction . text import CountVectorizer
from sklearn . feature_extraction . text import TfidfTransformer
from sklearn . linear_model import LogisticRegression

# import all data first
label_dir = {
" positive ": " data / positive ",
" negative ": " data / negative "
}

data = []
labels = []

for label in label_dir . keys () :
    for file in os . listdir ( label_dir [ label ]) :
        filepath = label_dir [ label ] + os . sep + file
        with open ( filepath , encoding ='utf8 ', errors ='ignore ', mode ='r') as review:
            content = review . read ()
            data . append ( content )
            labels . append ( label )

X_train , X_test , y_train , y_test = train_test_split ( data , labels , stratify = labels , test_size =0.25 , random_state =42)

count_vect = CountVectorizer ( stop_words = stopwords . words ('english '))
X_train_counts = count_vect . fit_transform ( X_train )

tfidf_transformer = TfidfTransformer ( use_idf = True , sublinear_tf = True ). fit (
X_train_counts )
X_train_tf = tfidf_transformer . transform ( X_train_counts )

classifier = LogisticRegression ( random_state =0) . fit ( X_train_tf , y_train )
# 3.3 Performance Metrics
    # We use accuracy_score and f1_score methods to measure how our model is doing
    # 1. We only apply transform (instead of fit_transform) on the X_new_counts as we fit our TF-IDF scores on the training data, making it part of the model. Now, since we only need to use the TF-IDF weights to transform the new data in the same format, we just use transform
    # 2. We store the results in a varaible called predicted, this will let us compute multiple quality metrics

import os
from sklearn . model_selection import train_test_split
from nltk . corpus import stopwords
from sklearn . feature_extraction . text import CountVectorizer
from sklearn . feature_extraction . text import TfidfTransformer
from sklearn . linear_model import LogisticRegression
from sklearn . metrics import accuracy_score , f1_score , confusion_matrix

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


X_train , X_test , y_train , y_test = train_test_split ( data , labels , stratify = labels
, test_size =0.25 , random_state =42)

count_vect = CountVectorizer ( stop_words = stopwords . words ('english '))
X_train_counts = count_vect . fit_transform ( X_train )

tfidf_transformer = TfidfTransformer ( use_idf = True , sublinear_tf = True ). fit (
X_train_counts )
X_train_tf = tfidf_transformer . transform ( X_train_counts )

clf = LogisticRegression ( random_state =0) . fit ( X_train_tf , y_train )

X_new_counts = count_vect . transform ( X_test )
X_new_tfidf = tfidf_transformer . transform ( X_new_counts )

predicted = clf . predict ( X_new_tfidf )

print ( confusion_matrix ( y_test , predicted ))
print ( accuracy_score ( y_test , predicted ))
print ( f1_score ( y_test , predicted , pos_label ='positive ') )
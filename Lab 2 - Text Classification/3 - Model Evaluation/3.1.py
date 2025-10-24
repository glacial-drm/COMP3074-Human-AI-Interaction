# 3.1 - The Train/Test Paradigm
    # Train-test to make sure the model is learning generalisable knowledge
    # Get more data (IMDB dataset)

# 

import os
from sklearn . model_selection import train_test_split

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

# Stratify is keeping the proportion of classes the same in training and testing 
X_train , X_test , y_train , y_test = train_test_split ( data , labels , stratify = labels
, test_size =0.25 , random_state =1)
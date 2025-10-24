# 4.4 What about stemming/lemmatising
    # CountVectorizer has an additional argument, analyzer, allowing for stems to be changed between words/chars etc. (read pdf)


# The following script stems the input before feeding it into the COuntVectorizer vocabulary, using the Porter stemmer
from sklearn . feature_extraction . text import CountVectorizer
from nltk . stem . snowball import PorterStemmer

p_stemmer = PorterStemmer ()
analyzer = CountVectorizer () . build_analyzer ()

def stemmed_words ( doc ):
    return ( p_stemmer . stem (w ) for w in analyzer ( doc ))

stem_vectorizer = CountVectorizer ( analyzer = stemmed_words )
print ( stem_vectorizer . fit_transform ([ "This sentence should get seriously mangled the stemming process , but it is fine ."]) )
print ( stem_vectorizer . get_feature_names () )

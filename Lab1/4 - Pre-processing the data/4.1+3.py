# 4.0 - Getting data
    # Getting data from Gutenberg: short stories 

from urllib import request

doc_urls = {
"Russia":"http://www.gutenberg.org/cache/epub/13437/pg13437.txt",
"France":"http://www.gutenberg.org/cache/epub/10577/pg10577.txt",
"England":"http://www.gutenberg.org/cache/epub/10135/pg10135 .txt",
"USA":"http://www. gutenberg .org/cache/epub/10947/pg10947.txt",
"Spain":"http://www.gutenberg.org/cache/epub/9987/pg9987.txt",
"Scandinavia":"http://www.gutenberg.org/cache/epub/5336/pg5336.txt",
"Iceland":"http://www.gutenberg.org/cache/epub/5603/pg5603.txt"
}

documents = {}

for country in doc_urls.keys():
    content = request.urlopen(doc_urls[country]).read().decode("utf8", errors ="ignore")
    documents [country] = content

# 4.1 Simple counts
    # Using scikit-learn's CountVectorizer which handles tokenising, filtering (stopwords and low-frequency words) and counting terms in documents
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

all_text = documents.values()

# CountVectorizer can be instantiated with paramaters to modify the vocabulary, listed in doc
count_vect = CountVectorizer(stop_words = stopwords.words("english"))

# fit_transform function feeds documents in the CountVectorizer, returning a term-document matrix
X_train_counts = count_vect.fit_transform(all_text)

# Shape output is (7, 24,128)
    # Vocabulary with 24,128 terms over 7 documents
    # 24,128 dimensions
print(X_train_counts.shape)

# 4.2 Term Weighting Methods
    # TfidTransformer can apply transformation functions on the counts of the CountVectorizer, letting us cahnge the way it generates term weights (shown in doc) 

from sklearn.feature_extraction.text import TfidfTransformer

count_vect = CountVectorizer ( stop_words = stopwords . words("english"))
X_train_counts = count_vect . fit_transform(all_text )
tf_transformer = TfidfTransformer(use_idf = True , sublinear_tf = True ). fit(
X_train_counts )
X_train_tf = tf_transformer . transform(X_train_counts )
print ( X_train_tf . shape )

# Document is now in a matrix form for almost any ML algo to understand

# 4.3 A note about fit, transform and fit_transform
    # read the pdf
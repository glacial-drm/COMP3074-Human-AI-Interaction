# 4.2 Making New Predictions 
    # Example application, assuming we have an already built classifier in the classifier variable.
    # COde should result in a prediction of 'positive'
new_data = ['this is new data , and it is fantastic ']
processed_newdata = count_vect . transform ( new_data )
processed_newdata = tfidf_transformer . transform ( processed_newdata )
print ( classifier . predict ( processed_newdata ))
# 2.1 Making sure Numpy and Scipy are installed
 # Fundamental Python libs used to implement linalg and scientific functions
import numpy
import scipy

# 2.2 Pickling Objects
    # Set of functions used to save and load objects 
    # pickle is the standard library
    # joblib is a newer alternative
    # Objects are any sort of instantiated data structure in this case

# With pickle
import pickle
with open ("filename.pickle", "wb") as f:
    pickle.dump(someobject, f)
with open ("filename.pickle", "rb") as f:
    someobject = pickle.load(f)

# With joblib
1 from joblib import dump, load
2 dump(someobject, "filename.joblib")
3 loaded_object = load("filename.joblib")
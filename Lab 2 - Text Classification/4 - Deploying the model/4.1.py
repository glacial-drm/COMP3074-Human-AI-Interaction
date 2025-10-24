# 4.1 Saving and Loading a model
    # using pickle and joblib

# pickle
import pickle
with open (" filename . pickle ", "wb") as f:
    pickle . dump ( someobject , f)
with open (" filename . pickle ", "rb") as f:
    someobject = pickle . load (f)

# joblib
from joblib import dump , load
dump ( someobject , 'filename . joblib ')
loaded_object = load ('filename . joblib ')
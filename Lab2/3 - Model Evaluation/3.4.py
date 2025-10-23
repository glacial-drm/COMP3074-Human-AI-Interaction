# 3.4 Visualising Experiment Results

import seaborn as sns
import matplotlib . pyplot as plt
import pandas as pd
import numpy as np

# Artificial data for three classifiers
np . random . seed (10) # For reproducibility
data = {
" Classifier A": np . array ([0.75 , 0.75 , 0.74 , 0.92 , 0.69 , 0.39 , 0.85 , 0.69 ,
0.79 , 0.68]) , # 10 - fold CV scores
" Classifier B": np . array ([0.34 , 0.43 , 0.34 , 0.24 , 0.15 , 0.32 , 0.43 , 0.22 ,
0.45 , 0.44]) ,
" Classifier C": np . array ([0.13 , 0.53 , 0.14 , 0.13 , 0.15 , 0.16 , 0.18 , 0.31 ,
0.21 , 0.41])
}

# Convert data to a Pandas DataFrame
df = pd . DataFrame ( data )

# Long format for Seaborn
df_long = pd . melt ( df , var_name ='Classifier ', value_name ='Accuracy ')

# Create the boxplot
sns . boxplot ( x='Classifier ', y ='Accuracy ', data = df_long )

# Add title and labels
plt . title ('Cross - Validation Accuracy of Three Classifiers ')
plt . ylabel ('Accuracy ')
plt . xlabel ('Classifier ')

# Show the plot
plt . show ()

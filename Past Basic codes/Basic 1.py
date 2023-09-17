'''
Basic 1 : Intro to colab and python 
'''

import pandas as pd
df = pd.read_csv('/content/sample_data/california_housing_test.csv')
df['age25Plus'] = df.housing_median_age>25
df['population'] = df.population.astype(int)

# create a variable named "spam" and assign the value 42 to it.
spam = 42
print(spam)
eggs = 2
spam + eggs


# Eclat is similar to Apriori, where you are finding basket similarities, people who bought also bought
# Support in Eclat is the % of sales of total transactions for a specific item

# Import the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
# header = none because there are no headers
dataset = pd.read_csv('Machine Learning Association Learning\Market_Basket_Optimisation.csv', header = None)
transactions = []
# creates lists within the list and include blank values as 'nan'
for i in range(0, 7501):
  transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

# Train the Eclat model on the dataset (length is the number of items in each comparison, Lift = Confidence/Support)
from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

# Visualize the results
results = list(rules)
print(results)

# Organize the results in a dataframe
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    return list(zip(lhs, rhs, supports))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Product 1', 'Product 2', 'Support'])

# print the results sorted by Support descending
print(resultsinDataFrame.nlargest(n = 10, columns = 'Support'))
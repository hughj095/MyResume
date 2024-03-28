# Identify the best association product purchases 
#  of a list of baskets purchased from your grocery 
#  store in order to create deals (Buy 1 get 1)s


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

# Train the Apriori model on the dataset (length is the number of items in each comparison, Lift = Confidence/Support)
from apyori import apriori
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)


# Visualize the results
results = list(rules)
print(results)

# Put results into an organize Dataframe
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])

# Print and Print sorted by Lift descending
print(resultsinDataFrame)
print(resultsinDataFrame.nlargest(n = 100, columns = 'Lift'))
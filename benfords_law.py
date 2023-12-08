"""
Benfords law or the First-digit law, is a fascinating statistical phenomenon, that predicts the frequency distribution
of first digits in many but not all data sets.
"""
import pandas as pd
import numpy as np
#import matplotlib
import random
# for a given set of number calculate the frequency distribution
# for every num:
#   convert num to string
#   check if the number in num_dict:
#       increatment the value in num_dict
#   else:
#       add num in num_dict with value of 1
nums = np.random.randint(1, 10, 5000)
num_dict = {}
for num in nums:
    val = str(num)[0]
    if val in num_dict:
        num_dict[val] += 1
    else:
        num_dict[val] = 1
print(num_dict)
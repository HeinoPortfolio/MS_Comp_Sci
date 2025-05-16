# -*- coding: utf-8 -*-
"""
Created on Fri May 16 18:39:31 2025

@author: ntcrw
"""

import pandas as pd
import numpy as np

# Sample DataFrame
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)

# Convert DataFrame to NumPy array
np_array = df.to_numpy()

print(type(np_array))
print(np_array)
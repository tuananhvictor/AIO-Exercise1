# -*- coding: utf-8 -*-
"""btap3_module2_week1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BNWPCd0FXBLE-OEBe7vOj3kgabALCuQ5
"""

import pandas as pd
import numpy as np

df = pd.read_csv("/content/advertising.csv")

data = df.to_numpy()

max_value_Sale = np.max(data[:, 3])
max_index_Sale = np.argmax(data[:, 3])

mean_value_TV = np.mean(data[:, 0])

count_Sale = np.count_nonzero(data[:, 3] >= 20)

selected_radio = df['Radio'][df['Sales'] >= 15]

average_radio = np.mean(selected_radio)

mean_Newspaper = np.mean(data[:, 2])

selected_Sales = df['Sales'][df['Newspaper'] > mean_Newspaper]

total_sales = np.sum(selected_Sales)

mean_Sales = np.mean(data[:,3])
Sales = data[:,3]
scores = np.empty_like(Sales, dtype=str)
for i in range(len(Sales)):
  if Sales[i] > mean_Sales:
    scores[i] = "Good"
  elif Sales[i] < mean_Sales:
    scores[i] = "Bad"
  else:
    scores[i] = "Average"




closest_value = Sales[np.abs(Sales - mean_Sales).argmin()]


scores1 = np.empty_like(Sales,dtype = str)

# Sử dụng vòng lặp for để đi qua từng phần tử trong sales
for i in range(len(Sales)):
  if Sales[i] > closest_value:
    scores1[i] = "Good"
  elif Sales[i] < closest_value:
    scores1[i] = "Bad"
  else:
    scores[i] = "Average"
scores1[7:10]
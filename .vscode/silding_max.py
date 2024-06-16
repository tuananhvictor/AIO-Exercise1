# -*- coding: utf-8 -*aa
import copy

def sliding_max(number_list, k1):


  results = []
  n = copy.deepcopy(number_list)

  for i in range(len(number_list) - k1+1 ):
    window = n[i:i + k1]
    results.append((window))

  return results
number_list = list(map(int, input().split()))
k1 = int(input())
max_values = sliding_max(number_list, k1)
print(max_values)
# -*- coding: utf-8 -*-
"""đếm_số_chữ_trong1string

Automatically generated by Colab.

Original file is located ata
    https://colab.research.google.com/drive/139ZwMLd-17fVpmsBFVZ7TqJJ4mLdXzqT
"""

string = input()
character = [i for i in string]
count ={}
for j in string:
    count[j] = character.count(j)
print(count)

